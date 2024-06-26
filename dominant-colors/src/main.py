import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from typing import List, Tuple
from scipy.cluster.vq import whiten
from sklearn.cluster import KMeans
from PIL import Image

K_VALUE = 5
WIDTH = 250
HEIGHT = 250

def extract_RGB_values(image_name: str) -> Tuple[List[float], List[float], List[float]]:
    img = Image.open(image_name)
    
    # Resize the image for better performance
    resized_img = img.resize((WIDTH, HEIGHT))
    
    # Convert the resized image to a numpy array
    image = np.array(resized_img)
    
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


def display_dominant_colors(k: int, dataframe: pd.DataFrame, rgb: List) -> None:
    k_means = KMeans(n_clusters=k)
    k_means.fit(dataframe)

    # Retrieve the cluster centers
    cluster_centers = k_means.cluster_centers_

    # Get standard deviations of each color
    r_std = np.array(rgb[0]).std()
    g_std = np.array(rgb[1]).std()
    b_std = np.array(rgb[2]).std()


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


    # Display the colors of cluster centers
    plt.figure(figsize=(6, 2))
    plt.imshow([colors], aspect='auto')
    plt.axis('off')  # Turn off axis
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Adjust subplot to image boundaries
    plt.margins(0, 0)  # No margins
    plt.gca().xaxis.set_major_locator(plt.NullLocator())  # No ticks
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig('dominant_colors.png', bbox_inches='tight', pad_inches=0)  # Save the image

def pipeline(image_name: str, k=K_VALUE) -> None:
    red, green, blue = extract_RGB_values(image_name)
    scaled_red, scaled_green, scaled_blue = standardize_RGB_values(red, green, blue)
    rgb_dataframe = create_dataframe(scaled_red, scaled_green, scaled_blue)
    display_dominant_colors(k, rgb_dataframe, [red, green, blue])




