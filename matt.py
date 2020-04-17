#!/usr/bin/env python
import math
from gimpfu import *


def python_selection_to_layer_cropped(image, drawable, num):
    pdb.gimp_image_undo_group_start(image)
    prev_layer = image.active_layer

    pdb.gimp_edit_copy(image.active_layer)
    i = 1
    layer_num = int(num)+1
    # layer_num = 5
    while i < layer_num:
      print(i)
      fsel = pdb.gimp_edit_paste(drawable, False)
      pdb.gimp_floating_sel_to_layer(fsel)
      # pdb.gimp_message(potato)
      low_threshold = round(.5+.5*(math.log(i)/math.log(layer_num)),2)
      pdb.gimp_drawable_threshold(image.active_layer, 0, low_threshold, 1)

pdb.plug_in_colortoalpha(image, drawable, color)
pdb.gimp_image_add_layer(image, layer, position)
position = pdb.gimp_image_get_item_position(image, item)
layer = pdb.gimp_image_merge_down(image, merge_layer, 0)
pdb.gimp_bucket_fill(drawable, 0, 0, 100, 255, FALSE, 1, 1)

      i += 1
    image.active_layer = prev_layer

    pdb.gimp_image_undo_group_end(image)


register(
    "python_fu_matt",
    "Create new layer from selection and auto crop layer",
    "Create new layer from selection and auto crop layer",
    "https://github.com/fre-sch",
    "https://github.com/fre-sch",
    "2016",
    "<Image>/Filters/Test/Matt",
    "RGB*, GRAY*",
    [
    (PF_INT, "layer_name", "Number of layers", ""),
    ],
    [],
    python_selection_to_layer_cropped
)

main()
