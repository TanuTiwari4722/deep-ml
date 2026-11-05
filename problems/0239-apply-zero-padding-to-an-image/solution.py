import numpy as np

def zero_pad_image(img, pad_width):
    """
    Add zero padding around a grayscale image.
    
    Args:
        img: 2D list or numpy array of pixel values
        pad_width: integer number of pixels to pad on each side
    
    Returns:
        Padded image as 2D list with integer values,
        or -1 if input is invalid
    """
    # Write your code here
    if not isinstance(pad_width, (int, np.integer)) or isinstance(pad_width, (bool, np.bool_)) or pad_width < 0:
        return -1
    
    try:
        img = np.asarray(img)
    except (ValueError, TypeError):
        return -1

    if img.ndim!=2:
        return -1

    if img.shape[0]==0 or img.shape[1]==0:
        return -1

    padded_img = np.pad(img, pad_width=((pad_width, pad_width), (pad_width, pad_width)),mode="constant", constant_values = 0)
    
    return padded_img.astype(int).tolist()