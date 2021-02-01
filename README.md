# Crank Shaft Detection
![header](.logo/header.png)

## Overview 
In order to detect crank shaft in an image, several image segmentation techniques are used on the source image.
This project uses several image segmentation techniques to detect crank shaft from an image and count the number.

## Tools
| Logo | Tool |
| --- | --- |
| <img src=".logo/OpenCV.png" height = "75px" width = "170px"> | OpenCV for image processing. |
| <img src=".logo/numpy.png" height = "75px" width = "170px"> | numpy for working with arrays. |

## Steps involved
| Title | Description |
| --- | --- |
| Colour masking | Colour masking technique is used to detect and mask the silver colours of connectors. |
| Morphological opening | Use Morphological Opening on the masked image to eliminate noise which consists of Erosion followed by Dilation. |
| Contouring | Drawing rectangular contours on the objects whose area is greater than the threshold value. |

## Applications
* Industrial robotic operations.
* Quantity check for crank shaft manufacturing.
* Saves time and reduces human effort.

## Future Scope
* Integration with large scale automated machines for industrial applicatoins.
 