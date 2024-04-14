from matplotlib import image as img
from typing import List, Tuple

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