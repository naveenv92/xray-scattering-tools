# X-Ray Scattering Tools
A collection of programs in Python to process and analyze data from sychrotron X-ray diffraction  

### Dependencies:  
`PyQt5`, `sys`, `numpy`, `matplotlib`, `tifffile`, and `pathlib`  

## Tools  
### Convert Binary to TIFF  
To save output from CCDs, data from sychrotrons are often saved as binary files. These streams of bytes must be decoded and reshaped to produced a tractable image. This program does batch conversion of binary files to TIFF image files, provided you know the output image resolution and the number precision of the encoded bytes.  

<img align="center" src="https://user-images.githubusercontent.com/6731730/77806869-373bb100-7043-11ea-8d59-bec3e95d86d9.png" width=600>

