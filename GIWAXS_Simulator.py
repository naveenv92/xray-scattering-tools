## Import required packages
import sys
import numpy as np
import matplotlib.pyplot as plt
from tifffile import imshow, imsave

## Check if file is passed to script - if not, exit with error
if len(sys.argv) < 3:
	sys.exit('ERROR: Did not pass enough input files!')

## Get filenames from command line arguments
cif_filename = sys.argv[1]
sf_filename = sys.argv[2]

## Get unit cell parameters from .cif file
# Open .cif file
with open(cif_filename) as cif_data:
	
	# Iterate through lines in file
	for line in cif_data:
		
		# Unit cell parameters
		if '_cell_length_a' in line:
			a = float(line.replace('_cell_length_a', '').replace(' ', '').replace('(', '').replace(')', ''))
		if '_cell_length_b' in line:
			b = float(line.replace('_cell_length_b', '').replace(' ', '').replace('(', '').replace(')', ''))
		if '_cell_length_c' in line:
			c = float(line.replace('_cell_length_c', '').replace(' ', '').replace('(', '').replace(')', ''))

		# Unit cell angles
		if '_cell_angle_alpha' in line:
			alpha = float(line.replace('_cell_angle_alpha', '').replace(' ', '').replace('(', '').replace(')', ''))
		if '_cell_angle_beta' in line:
			beta = float(line.replace('_cell_angle_beta', '').replace(' ', '').replace('(', '').replace(')', ''))
		if '_cell_angle_gamma' in line:
			gamma = float(line.replace('_cell_angle_gamma', '').replace(' ', '').replace('(', '').replace(')', ''))

## Convert angles to radians
alpha = alpha*np.pi/180
beta = beta*np.pi/180
gamma = gamma*np.pi/180

## Calculate reciprocal lattice parameters
V = (a*b*c)*np.sqrt(1 - (np.cos(alpha))**2 - (np.cos(beta))**2 - (np.cos(gamma))**2 + 2*np.cos(alpha)*np.cos(beta)*np.cos(gamma))
a_r = (b*c*np.sin(alpha))/V
b_r = (c*a*np.sin(beta))/V
c_r = (a*b*np.sin(gamma))/V

## Calculate reciprocal lattice angles
alpha_r = np.arccos((np.cos(beta)*np.cos(gamma) - np.cos(alpha))/(np.sin(beta)*np.sin(gamma)))
beta_r = np.arccos((np.cos(alpha)*np.cos(gamma) - np.cos(beta))/(np.sin(alpha)*np.sin(gamma)))
gamma_r = np.arccos((np.cos(alpha)*np.cos(beta) - np.cos(gamma))/(np.sin(alpha)*np.sin(beta)))

## Prompt for preferred orientation direction
# pref_orientation = input('Enter preferred orientation direction (e.g. 111): ')
# h_pref = int(pref_orientation[0])
# k_pref = int(pref_orientation[1])
# l_pref = int(pref_orientation[2])

print('Enter preferred orientation direction (e.g. 111)')
pref_h = input('Enter h-value: ')
h_pref = int(pref_h)
pref_k = input('Enter k-value: ')
k_pref = int(pref_k)
pref_l = input('Enter l-value: ')
l_pref = int(pref_l)
pref_orientation = str(h_pref) + str(k_pref) + str(l_pref)

## Calculate d-spacing of the preferred orientation plane
d_pref = 1/(np.sqrt((h_pref*a_r)**2 + (k_pref*b_r)**2 + (l_pref*c_r)**2 + 2*k_pref*l_pref*b_r*c_r*np.cos(alpha_r)
                   + 2*l_pref*h_pref*c_r*a_r*np.cos(beta_r) + 2*h_pref*k_pref*a_r*b_r*np.cos(gamma_r)))

## Import structure factor data
h, k, l, d, I = np.loadtxt(sf_filename, unpack=True, usecols=(0, 1, 2, 3, 6), skiprows=1) 

# Intensity is given by the square of the structure factor
I = np.multiply(I,I)

# Sort reflections based on intensity
h = [x for (y,x) in sorted(zip(I,h), reverse=True)]
k = [x for (y,x) in sorted(zip(I,k), reverse=True)]
l = [x for (y,x) in sorted(zip(I,l), reverse=True)]
d = [x for (y,x) in sorted(zip(I,d), reverse=True)]
I = sorted(I, reverse=True)

# Calculate momentum transfer vector values (q)
q = (2*np.pi)/np.array(d)

## Calculate angles between lattice planes and preferred orientation direction
# Initialize array of zeros
phi = np.zeros(len(q))

## Iterate through lattice planes and calculate angle between planes
for i in range(0, len(q)):
    phi[i] = (d_pref*d[i])*(h[i]*h_pref*(a_r**2) + k[i]*k_pref*(b_r**2) + l[i]*l_pref*(c_r**2) + 
                           (k[i]*l_pref + l[i]*k_pref)*b_r*c_r*np.cos(alpha_r) + 
                           (h[i]*l_pref + l[i]*h_pref)*a_r*c_r*np.cos(beta_r) + 
                           (h[i]*k_pref + k[i]*h_pref)*a_r*b_r*np.cos(gamma_r))
    
    # Make sure input to arccos is between 0 and 1
    if phi[i] > 1:
        phi[i] = 1
    elif phi[i] < 0:
        phi[i] = 0
    
    phi[i] = np.arccos(phi[i])

## Calculate components of q-vector in-plane and out-of-plane
q_xy = np.multiply(q, np.sin(phi))
q_z = np.multiply(q, np.cos(phi))

## Save list of reflections and q-vector components
refl_filename = cif_filename.replace('.cif', '_') + pref_orientation + '_reflections.csv'
head = 'h, k, l, Q_xy (1/A), Q_z (1/A)'
np.savetxt(refl_filename, np.c_[h, k, l, q_xy, q_z], fmt=['%i', '%i', '%i', '%.3f', '%.3f'], delimiter=',', comments='', header=head)

## Get X-ray energy (keV) and convert it to wavelength
en = input('Enter X-ray energy (keV): ')
lam = 12.4/float(en)

## Get range of Q values for GIXRD simulation
q_xy_max = input('Enter max value of Q_xy (1/A): ')
q_xy_max = float(q_xy_max)
q_z_max = input('Enter max value of Q_z (1/A): ')
q_z_max = float(q_z_max)

## Get incidence angle
om = input('Enter incidence angle (Deg): ')
om = float(om)*np.pi/180

## Only use reflections that are in the set q limits
q_xy_GIWAXS = np.array([])
q_z_GIWAXS = np.array([])
I_GIWAXS = np.array([])

for i in range(0, len(q_xy)):
  if q_xy[i] <= q_xy_max and q_z[i] <= q_z_max:
    q_xy_GIWAXS = np.append(q_xy_GIWAXS, q_xy[i])
    q_z_GIWAXS = np.append(q_z_GIWAXS, q_z[i])
    I_GIWAXS = np.append(I_GIWAXS, I[i])


## Calculate GIXRD image and save data
# Get FWHM values in the x and y directions
fwhm_x = input('Enter FWHM in x-direction (1/A): ')
sigma_x = float(fwhm_x)/2.355
fwhm_y = input('Enter FWHM in y-direction (1/A): ')
sigma_y = float(fwhm_y)/2.355

# Create meshgrid for GIWAXS plot
q_xy_points = int(1000*(q_xy_max/2.5))
q_z_points = int(1000*(q_z_max/2.5))
X, Y = np.meshgrid(np.linspace(0, q_xy_max, q_xy_points), np.linspace(0, q_z_max, q_z_points))

# Calculate Gaussian peaks for Bragg reflections
Z = np.ones([len(X), len(Y)])

for i in range(len(q_xy_GIWAXS)):

	# Print iteration to keep track of progress
	print('Iteration ' + str(i) + ' of ' + str(len(q_xy_GIWAXS) - 1))
	
	# Calculate angle of diffraction spot
	if q_xy_GIWAXS[i] == 0:
		ang = np.pi/2
	elif q_z_GIWAXS[i] == 0:
		ang = 0
	else:
		ang = np.arctan(q_z_GIWAXS[i]/q_xy_GIWAXS[i])

	# Calculate constants for elliptical gaussian
	a = (np.cos(ang)**2)/(2*sigma_x**2) + (np.sin(ang)**2)/(2*sigma_y**2)
	b = -(np.sin(2*ang))/(4*sigma_x**2) + (np.sin(2*ang))/(4*sigma_y**2)
	c = (np.sin(ang)**2)/(2*sigma_x**2) + (np.cos(ang)**2)/(2*sigma_y**2)

	# Calculate gaussian and add to meshgrid
	Z = Z + I_GIWAXS[i]*np.exp(-(a*(X - q_xy_GIWAXS[i])**2 - 2*b*(X - q_xy_GIWAXS[i])*(Y - q_z_GIWAXS[i]) + c*(Y - q_z_GIWAXS[i])**2))

# Save GIXRD image
gixrd_filename = refl_filename.replace('_reflections.csv', '') + '_qxy_' + str(q_xy_max) + '_qz_' + str(q_z_max) + '_GIXRD.tif'
imsave(gixrd_filename, np.flipud(Z))

# Show image
imshow(np.flipud(Z), cmap='RdBu_r')
plt.show()