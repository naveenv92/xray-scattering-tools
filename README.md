# X-Ray Scattering Tools
A collection of programs in Python 3 to process and analyze data from sychrotron X-ray diffraction. The GIWAXS Image Simulator program was used to generate the simulated GIWAXS images in the publication N. R. Venkatesan <i>et al</i>, <i>Chem. Mater.</i>, <b>2018</b> ([10.1021/acs.chemmater.8b03832](https://pubs.acs.org/doi/abs/10.1021/acs.chemmater.8b03832)). 

### Dependencies:  
`PyQt5`, `sys`, `numpy`, `matplotlib`, `tifffile`, and `pathlib`  

## Tools :hammer_and_wrench:  
### Convert Binary to TIFF  

#### `convert-binary-to-tiff.py`  

To save output from CCDs, data from sychrotrons are often saved as binary files. These streams of bytes must be decoded and reshaped to produced a tractable image. This program does batch conversion of binary files to TIFF image files, provided you know the output image resolution and the number precision of the encoded bytes.  

<img src="https://user-images.githubusercontent.com/6731730/77806869-373bb100-7043-11ea-8d59-bec3e95d86d9.png" width=600>  
&nbsp;  

### GIWAXS Image Simulator  

#### `giwaxs-image-simulator.py`  

This program allows you to simulate the GIWAXS (Grazing-Incidence Wide-Angle X-Ray Scattering) pattern of any fiber-textured thin film given that you have a CIF (Crystallographic Information File) file and knowledge of the out-of-plane crystallographic direction.  

<img src="https://user-images.githubusercontent.com/6731730/77809304-4f63fe00-704c-11ea-8f16-3bd91d431e56.png" width=600>  
&nbsp;  

### X-Ray Scattering Analyzer  

#### `xrs-analyzer.py`     

This program allows you to manipulate images collected from synchrotron X-ray diffraction. The beam center and sample-to-detector distance are calibrated using a diffraction image of a known calibrant (silver behenate or lanthanum hexaboride). The program has functions to calculate rotationally averaged diffraction patterns for isotropic samples, geometrically-corrected diffraction images for anisotropic GIWAXS measurements, and in-plane and out-of-plane intensity cuts.  

<img src="https://user-images.githubusercontent.com/6731730/77809478-137d6880-704d-11ea-9852-4dd336509fde.png" width=600>  

