# X-Ray Scattering Tools
A collection of programs in Python to process and analyze data from sychrotron X-ray diffraction  

### Dependencies:  
`PyQt5`, `sys`, `numpy`, `matplotlib`, `tifffile`, and `pathlib`  

## Tools  
### Convert Binary to TIFF  
To save output from CCDs, data from sychrotrons are often saved as binary files. These streams of bytes must be decoded and reshaped to produced a tractable image. This program does batch conversion of binary files to TIFF image files, provided you know the output image resolution and the number precision of the encoded bytes.  

