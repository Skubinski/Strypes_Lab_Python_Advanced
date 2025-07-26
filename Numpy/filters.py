import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
def blur_effect(file_path):
    image = Image.open(file_path).convert("L")

    img_arr = np.array(image)

    kernel = np.ones((3,3)) / 9.0

    rows, cols = img_arr.shape

    padded = np.pad(img_arr, ((1, 1), (1, 1)), mode='edge')

    blurred = np.zeros_like(img_arr)

    for i in range(rows):
        for j in range(cols):
            region = padded[i:i+3, j:j+3]
            blurred[i, j] = np.sum(region * kernel)

    return blurred.astype(np.uint8)


def median(file_path):
    image = Image.open(file_path).convert('L')

    img_arr = np.array(image)

    rows, cols = img_arr.shape

    padded = np.pad(img_arr, ((1, 1), (1, 1)), mode='edge')

    filtered = np.zeros_like(img_arr)

    for i in range(rows):
        for j in range(cols):
            region = padded[i:i+3, j:j+3]
            flattened_arr = sorted(region.flatten())
            median = np.median(flattened_arr)
            filtered[i][j] = median

    return filtered.astype(np.uint8)


def edge(file_path, kernel):
    image = Image.open(file_path).convert('RGB')

    img_arr = np.array(image)

    rows, cols,_ = img_arr.shape

    window_size = kernel.shape[0]

    pad = window_size // 2

    padded = np.pad(img_arr,((pad,pad), (pad,pad), (0, 0)), mode='edge')

    edged = np.zeros_like(img_arr)

    for i in range(rows):
        for j in range(cols):
            r, g, b = 0, 0, 0
            region = padded[i:i + window_size, j:j + window_size]
            for k in range(window_size):
                for l in range(window_size):
                    pixel = region[k, l]
                    weight = kernel[k, l]
                    r += pixel[0] * weight
                    g += pixel[1] * weight
                    b += pixel[2] * weight


            edged[i, j, 0] = np.clip(r, 0, 255)
            edged[i, j, 1] = np.clip(g, 0, 255)
            edged[i, j, 2] = np.clip(b, 0, 255)
    return edged.astype(np.uint8)



def warm_filter(file_path):
    image = Image.open(file_path).convert('RGB')

    img_arr = np.array(image)

    rows, cols,_ = img_arr.shape

    warmed = np.zeros_like(img_arr)

    for i in range(rows):
        for j in range(cols):
            r, g, b = 0, 0, 0
            pixel = img_arr[i][j].astype(int)
            r = max(0, min(255, pixel[0] + 30))
            g = max(0, min(255, pixel[1] + 10))
            b = max(0, min(255, pixel[2] - 20))

            warmed[i][j] = [r, g, b]
    return warmed.astype(np.uint8)



warm = warm_filter('dog.jpeg')
# kernel = np.zeros((1,1))
#
#
# edged = edge('dog.jpeg', kernel)
#
#
plt.imshow(warm)

plt.show()