#!/usr/bin/env python
import math
from gimpfu import *


def crop_down(image, drawable, num):
    # pdb.gimp_image_undo_group_start(image)


    first_layer = image.active_layer

    sizes = [[5,7],[8,10],[11,14]]

    non_empty, x1, y1, x2, y2 = pdb.gimp_selection_bounds(image)


    if non_empty > 0:
        width = pdb.gimp_image_width(image)
        height = pdb.gimp_image_height(image)

        # pdb.gimp_message(non_empty)
        # pdb.gimp_message(x1)
        # pdb.gimp_message(y1)
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

        # new_width = width - left - right
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
        pdb.gimp_message("height: " + str(height))

    # pdb.gimp_image_crop(image, new_width, new_height, offx, offy)
    #
    #
    # pdb.gimp_edit_copy(image.active_layer)
    # i = 1
    # layer_num = int(num)+1
    # # layer_num = 5
    # while i < layer_num:
    #   fsel = pdb.gimp_edit_paste(drawable, False)
    #   pdb.gimp_floating_sel_to_layer(fsel)
    #   prev_layer = image.active_layer
    #
    #   low_threshold = round(.5+.5*(math.log(i)/math.log(layer_num)),2)
    #
    #   fsel = pdb.gimp_edit_paste(drawable, False)
    #   pdb.gimp_floating_sel_to_layer(fsel)
    #   pdb.gimp_drawable_edit_clear(image.active_layer)
    #
    #
    #   i += 1
    # image.active_layer = first_layer

    # pdb.gimp_image_undo_group_end(image)


register(
    "python_fu_crop",
    "Create new layer from selection and auto crop layer",
    "Create new layer from selection and auto crop layer",
    "https://github.com/fre-sch",
    "https://github.com/fre-sch",
    "2016",
    "<Image>/Filters/Test/Crop",
    "RGB*, GRAY*",
    [
    (PF_INT, "layer_name", "Number of layers", ""),
    ],
    [],
    crop_down
)

main()
