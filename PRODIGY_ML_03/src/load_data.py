import os
import cv2
import numpy as np
from tqdm import tqdm


def load_image_data(data_dir, img_size=64):
    X = []
    y = []

    print("Reading from:", os.path.abspath(data_dir))
    files = os.listdir(data_dir)
    print("Files found:", len(files))

    for file_name in tqdm(files):
        file_path = os.path.join(data_dir, file_name)

        if file_name.startswith("cat"):
            label = 0
        elif file_name.startswith("dog"):
            label = 1
        else:
            continue

        img = cv2.imread(file_path)
        if img is None:
            continue

        img = cv2.resize(img, (img_size, img_size))
        img = img / 255.0
        img = img.flatten()

        X.append(img)
        y.append(label)

    return np.array(X), np.array(y)
