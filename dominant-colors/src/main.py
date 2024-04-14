import pandas as pd

from matplotlib import image as img
from typing import List, Tuple
from scipy.cluster.vq import whiten
from sklearn.metrics import silhouette_score
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

def find_optimal_k(dataframe: pd.DataFrame) -> int:
    k_values = range(2, 10)
    silhouette_scores = []

    best_k = None
    best_silhouette_score = -1

    # Iterate through different K values
    for k in k_values:
        k_means = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=100, random_state=42)
        k_means.fit(dataframe)
        
        # Calculate the average silhouette score
        silhouette_avg = silhouette_score(dataframe, k_means.labels_)  
        silhouette_scores.append(silhouette_avg)
        
        # Update the best K value if a higher silhouette score is found
        if silhouette_avg > best_silhouette_score:
            best_k = k
            best_silhouette_score = silhouette_avg

    return best_k


