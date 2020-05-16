#!/usr/bin/env python
import math
from gimpfu import *

# def crop_down():
#     print("potato")

def crop_down(orig_image, drawable, image_name):
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

# firstImage = gimp.image_list()[0]
# imageName = pdb.gimp_image_get_name(firstImage)
imageName = "george"
saveLocation = "C:\\Users\\mathu\\Google Drive\\Art\\python-fu\\"
register(
    "python_fu_crop",
    "Make multiple cropped copies",
    "Make multiple cropped copies ",
    "https://github.com/math-yew",
    "https://github.com/math-yew",
    "2016",
    "<Image>/Filters/Test/CropDown",
    "RGB*, GRAY*",
    [
    (PF_STRING, "image_name", "Image Name", imageName),
    (PF_RADIO, "orient", "Orientation: ", LANDSCAPE,
            (
                 ("Portrait", Portrait),
                 ( "Landscape", LANDSCAPE)
            )
         ),
    (PF_TOGGLE,  "y_center",    "Center Vertically:", FALSE),
    # (PF_STRING, "save_location", "Save Location", saveLocation),
    (PF_FILE, "pf_afile", _("Choose File:"), "/home/jbaker")
    ],
    [],
    crop_down
)

main()
