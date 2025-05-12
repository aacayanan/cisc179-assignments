import cv2
import os

images = [
    "./Picture1.jpg",
    "./Picture2.jpg",
    "./Picture3.jpg",
    "./Picture4.jpg",
]

output_dir = "./modified"
os.makedirs(output_dir, exist_ok=True)


def grayblur(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    grayblur_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur with radius 2 to the grayscale image
    grayblur_image = cv2.GaussianBlur(grayblur_image, (5, 5), 2)

    # Save the grayscale image
    filename = os.path.basename(image_path)
    grayblur_image_path = os.path.join(output_dir, f"grayblur_{filename}")
    cv2.imwrite(grayblur_image_path, grayblur_image)
    return grayblur_image_path


for image_path in images:
    grayblur(image_path)

with open("READ ME.txt", "w") as file:
    for image_path in images:
        processed_path = grayblur(image_path)
        file.write(f"Processed in {processed_path}\n")
