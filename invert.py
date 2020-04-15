from gimpfu import *

def invert_layer(img, layer) :
    ''' Inverts the colors of the selected layer.
    
    Parameters:
    img : image The current image.
    layer : layer The layer of the image that is selected.
    '''
    pdb.gimp_invert(layer)

register(
    "python_fu_test_invert_layer",
    "Invert layer",
    "Inverts the colors of a layer",
    "JFM",
    "Open source (BSD 3-clause license)",
    "2013",
    "<Image>/Filters/Test/Invert layer",
    "*",
    [],
    [],
    invert_layer)

main()