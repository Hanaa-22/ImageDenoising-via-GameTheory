import cv2
import numpy as np
import os
import random

# Paths
BASE_DATASET_DIR = "datasetTHJ"
INPUT_DIR  = os.path.join(BASE_DATASET_DIR, "OG")
OUTPUT_DIR = os.path.join(BASE_DATASET_DIR, "noisy")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Fixed-parameter noise functions
def gaussian_noise_fixed(image):
    sigma = 25
    gauss = np.random.normal(0, sigma, image.shape)
    noisy = image.astype(np.float32) + gauss
    return np.clip(noisy, 0, 255).astype(np.uint8)

def poisson_noise_fixed(image):
    scale = 1.0
    noisy = np.random.poisson(image.astype(np.float32) * scale) / scale
    return np.clip(noisy, 0, 255).astype(np.uint8)

def salt_pepper_noise_fixed(image, amount=0.02):
    noisy = image.copy()
    num_pixels = int(amount * image.shape[0] * image.shape[1])

    # Salt (white)
    coords = (
        np.random.randint(0, image.shape[0], num_pixels),
        np.random.randint(0, image.shape[1], num_pixels)
    )
    noisy[coords] = 255

    # Pepper (black)
    coords = (
        np.random.randint(0, image.shape[0], num_pixels),
        np.random.randint(0, image.shape[1], num_pixels)
    )
    noisy[coords] = 0

    return noisy

# Noise configuration 
NOISE_TYPES = [
    ("Gaussian",   gaussian_noise_fixed,   "sigma25"),
    ("SaltPepper", salt_pepper_noise_fixed, "amt0.02"),
    ("Poisson",    poisson_noise_fixed,    "scale1.0"),
]

# Process images
count = 0
for filename in os.listdir(INPUT_DIR):
    if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    image_path = os.path.join(INPUT_DIR, filename)
    image = cv2.imread(image_path)
    if image is None:
        continue

    # Choose one noise type
    noise_name, noise_fn, level_str = random.choice(NOISE_TYPES)

    # Apply the noise
    noisy_image = noise_fn(image)

    base, ext = os.path.splitext(filename)
    new_filename = f"{base}_{noise_name}_{level_str}{ext}"

    # Save
    save_path = os.path.join(OUTPUT_DIR, new_filename)
    cv2.imwrite(save_path, noisy_image)
    count += 1

    print(f"Generated: {new_filename}")

print(f"\nDone. Created {count} noisy images in folder: {OUTPUT_DIR}")