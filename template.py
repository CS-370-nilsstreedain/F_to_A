#!/usr/bin/env python2.7

import cv2

# --------------------------------------------------------------------------------
#   Modify the image of 'F' such that it can be recognized by a model as 'A'
#   (Note: be careful that the image of the dataset are rotated and flipped.)
# --------------------------------------------------------------------------------

# load the lower-case 'F'
fimg = cv2.imread('f.png', 0)


# TODO: manipulate the 'F' image in here, e.g., draw lines, flip, rotate, ...
#       (Tip: you can manually modify this 'F' by using some graphic apps.)
fimg = fimg


# Do not edit: the model takes an image flipped and rotated 90 degrees
#              (we provide an example image of 'F' in 'sample.png')
f_rot_img = cv2.rotate(fimg, cv2.ROTATE_90_COUNTERCLOCKWISE)

# store the manipulated image
cv2.imwrite('f_manipulated.png', f_rot_img)
