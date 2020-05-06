#!/usr/bin/env python
import math
from gimpfu import *

# def crop_down():
#     print("potato")

def crop_down(orig_image, drawable, num):
    sizes = [[5,7],[8,10],[11,14]]
    non_empty, x1, y1, x2, y2 = pdb.gimp_selection_bounds(orig_image)
    i = 0
    while i < 3:
        # image = orig_image
        image = pdb.gimp_image_duplicate(orig_image)
        layer = image.active_layer
        if non_empty > 0:
            width = pdb.gimp_image_width(image)
            height = pdb.gimp_image_height(image)
            left = x1
            dright = width - x2
            top = y1
            bottom = height - y2
            center = (y1 + y2)/2
            if left > dright:
                left = left - dright
                right = width
            else:
                right = width - dright + left
                left = 0
            new_width = right - left
            pdb.gimp_message("left: " + str(left))
            pdb.gimp_message("right: " + str(right))
            pdb.gimp_message("new_width: " + str(new_width))
            new_height = height
            offx = left
            offy = 0
            pdb.gimp_image_crop(image, new_width, new_height, offx, offy)
            width = pdb.gimp_image_width(image)
            height = pdb.gimp_image_height(image)
            pdb.gimp_message("width: " + str(width))
            name = str(sizes[i][0]) + "x" + str(sizes[i][1])
            pdb.gimp_file_save(image, layer, 'C:\\Users\\mathu\\Google Drive\\Art\\python-fu\\'+name+'.jpg', '?')
            pdb.gimp_image_delete(image)
            pdb.gimp_message("height: " + str(height))
            i += 1
    x = "x"


register(
    "python_fu_crop",
    "Create new layer from selection and auto crop layer",
    "Create new layer from selection and auto crop layer",
    "https://github.com/fre-sch",
    "https://github.com/fre-sch",
    "2016",
    "<Image>/Filters/Test/CropDown",
    "RGB*, GRAY*",
    [
    (PF_INT, "layer_name", "Number of layers", ""),
    ],
    [],
    crop_down
)

main()
