import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
from struct import unpack
from tifffile import imsave
import glob
from os import path
import numpy as np
from scipy import misc

## Required functions ##

def askOpenDir():
	dirChoice = filedialog.askdirectory(initialdir='./')
	imgDir.delete(0, len(imgDir.get()))
	imgDir.insert(0, dirChoice)

	# Make default save directory the same
	saveDir.delete(0, len(saveDir.get()))
	saveDir.insert(0, dirChoice)
	return

def askOpenDirSave():
	dirChoice = filedialog.askdirectory(initialdir='./')
	saveDir.delete(0, len(saveDir.get()))
	saveDir.insert(0, dirChoice)
	return

def convertGBtoTIF():
	currDir = imgDir.get()
	img_files = glob.glob(currDir + '/*.gb')

	for i in range(len(img_files)):

		# Convert binary file to TIFF #
		currFile = img_files[i]
		saveFileName = saveDir.get() + '/' + path.basename(currFile)[:-2] + 'tif'

		# Get image width and height
		imwidth = int(img_width.get())
		imheight = int(img_height.get())

		# Get string to unpack binary file (single-precision float)
		encode_str = str(imwidth*imheight) + 'f'

		bin_img = Path(currFile).read_bytes()
		new_img = unpack(encode_str, bin_img)
		new_img = np.reshape(new_img, (imheight,-1))
		new_img = new_img.astype(np.float32)
		imsave(saveFileName, new_img)

		# Update progress bar
		prog_bar['value'] = (i + 1)/len(img_files)
		prog_bar.update()

	return

## Create initial window ##

# Create window
root = tk.Tk()

# Get screen resolution
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Use relative screen ratio
ratio_width = 0.3
ratio_height = 0.35

# Get pixel offset to center window
offset_x = int(((1 - ratio_width)*screen_width)/2)
offset_y = int(((1 - ratio_height)*screen_height)/2)

# Determine size of window (and center on screen)
width = int(ratio_width*screen_width)
height = int(ratio_height*screen_height)
screen_dim = str(width) + 'x' + str(height) + '+' + str(offset_x) + '+' + str(offset_y) 

# Set the size and title of the window and make it not resizeable
root.geometry(screen_dim)
root.title('Convert .gb to .tif')
root.resizable(False, False)

# Set widget styles
ttk.Style().configure('header.TLabel', foreground='blue', font=('calibri', 18, 'bold'))
ttk.Style().configure('label.TLabel', font=('calibri', 14, 'bold'))
ttk.Style().configure('text.TLabel', font=('calibri', 12))
ttk.Style().configure('browse_entry.TEntry', font=('calibri', 12))
ttk.Style().configure('params_entry.TEntry', font=('calibri', 12))
ttk.Style().configure('calcs_entry.TEntry', font=('calibri', 12))
ttk.Style().configure('rad.TRadiobutton', font=('calibri', 12))
ttk.Style().configure('small_button.TButton', font=('calibri', 12, 'bold'))
ttk.Style().configure('big_button.TButton', font=('calibri', 16, 'bold'))
ttk.Style().configure('chk.TCheckbutton', font=('calibri', 12))

# Create frame for overall window
colPadSize = int(0.05*width)
colSize = int((width - 2*colPadSize)/4)
entrySize = int(0.02*width)
windowFrame = ttk.Frame(root, padding=[int(0.05*width), int(0.05*height)])
windowFrame.place(x=0, y=0, anchor='nw', width=width, height=height)

# Configure columns for grid
windowFrame.columnconfigure(0, minsize=colSize)
windowFrame.columnconfigure(1, minsize=colSize)
windowFrame.columnconfigure(2, minsize=colSize)
windowFrame.columnconfigure(3, minsize=colSize)

# Configure rows for grid
windowFrame.rowconfigure(0, pad=colPadSize)
windowFrame.rowconfigure(1, pad=colPadSize)
windowFrame.rowconfigure(2, pad=colPadSize)
windowFrame.rowconfigure(3, pad=colPadSize)
windowFrame.rowconfigure(4, pad=colPadSize)
windowFrame.rowconfigure(5, pad=colPadSize)

# Section header
ttk.Label(windowFrame, text='Convert General Binary Files to TIFF Images', style='header.TLabel').grid(row=0, column=0, columnspan=4)

# Conversion Directory
ttk.Label(windowFrame, text='Image Directory:', style='label.TLabel').grid(row=1, column=0, sticky='E')
imgDir = ttk.Entry(windowFrame, style='browse_entry.TEntry')
imgDir.grid(row=1, column=1, columnspan=2, sticky='WE')
ttk.Button(windowFrame, text='Browse...', style='small_button.TButton', command=askOpenDir).grid(row=1, column=3)

# Image Resolution
ttk.Label(windowFrame, text='Resolution:', style='label.TLabel').grid(row=2, column=0, sticky='E')
img_width = ttk.Entry(windowFrame, style='params_entry.TEntry', width=entrySize, justify='center')
img_width.grid(row=2, column=1)
img_height = ttk.Entry(windowFrame, style='params_entry.TEntry', width=entrySize, justify='center')
img_height.grid(row=2, column=2)

# Save Directory
ttk.Label(windowFrame, text='Save Directory:', style='label.TLabel').grid(row=3, column=0, sticky='E')
saveDir = ttk.Entry(windowFrame, style='browse_entry.TEntry')
saveDir.grid(row=3, column=1, columnspan=2, sticky='WE')
ttk.Button(windowFrame, text='Browse...', style='small_button.TButton', command=askOpenDirSave).grid(row=3, column=3)

# Add progress bar
ttk.Label(windowFrame, text='Progress:', style='label.TLabel').grid(row=4, column=0, sticky='E')
prog_bar = ttk.Progressbar(windowFrame, orient='horizontal', mode='determinate', value=0.0, maximum=1.0)
prog_bar.grid(row=4, column=1, columnspan=3, sticky='WE')

# Add button to convert files
ttk.Button(windowFrame, text='Convert Files', style='big_button.TButton', command=convertGBtoTIF).grid(row=5, column=0, columnspan=4, sticky='WE')

# Open program
root.mainloop()