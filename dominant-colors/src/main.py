from matplotlib import image as img
from typing import List, Tuple
from scipy.cluster.vq import whiten

def extract_RGB_values(image_name: str) -> Tuple[List[float], List[float], List[float]]:
    image = img.imread(f'images/{image_name}')
    r = []
    g = []
    b = []

    # Store RGB values of all pixels in lists r, g and b
    for row in image:
        for temp_r, temp_g, temp_b in row:
            r.append(temp_r)
            g.append(temp_g)
            b.append(temp_b)

    return r, g, b

def standardize_RGB_values(r: List, g: List, b: List) -> Tuple[List[float], List[float], List[float]]:
    scaled_r = whiten(r)
    scaled_g = whiten(g)
    scaled_b = whiten(b)

    return scaled_r, scaled_g, scaled_b


