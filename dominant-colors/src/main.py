import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import image as img
from typing import List, Tuple
from scipy.cluster.vq import whiten
from sklearn.cluster import KMeans


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

def create_dataframe(r: List, g: List, b: List) -> pd.DataFrame:
    dataframe = pd.DataFrame({
        "scaled_R" : r,
        "scaled_G" : g,
        "scaled_B" : b
    })

    return dataframe


def display_dominant_colors(k: int, dataframe: pd.DataFrame) -> None:
    k_means = KMeans(n_clusters=k)
    k_means.fit(dataframe)

    # Retrieve the cluster centers
    cluster_centers = k_means.cluster_centers_

    # Get standard deviations of each color
    r_std, g_std, b_std = dataframe.std()

    # Scale the cluster centers' RGB values
    colors = []
    for cluster_center in cluster_centers:
        scaled_r, scaled_g, scaled_b = cluster_center
        # Convert each standardized value to scaled value
        colors.append((
            scaled_r * r_std / 255,
            scaled_g * g_std / 255,
            scaled_b * b_std / 255
        ))

    print("Colors:", colors)

    # Display the colors of cluster centers
    plt.imshow([colors])
    plt.show()

def pipeline(k:int, image_name: str) -> None:
    red, green, blue = extract_RGB_values(image_name)
    scaled_red, scaled_green, scaled_blue = standardize_RGB_values(red, green, blue)
    rgb_dataframe = create_dataframe(scaled_red, scaled_green, scaled_blue)
    display_dominant_colors(k, rgb_dataframe)


if __name__ == "__main__":
    pipeline(2, "example.jpg")

