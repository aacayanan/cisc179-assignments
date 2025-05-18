from PIL import Image
import os


def grayscale_image(input_path, output_path):
    # open the image
    image = Image.open(input_path)

    # convert to grayscale
    grayscale = image.convert("L")

    # save the grayscale image
    grayscale.save(output_path)


images = ["Picture1.jpg", "Picture2.jpg", "Picture3.jpg", "Picture4.jpg"]
output_path = "./grayscale/"

# create output directory if it doesn't exist
if not os.path.exists(output_path):
    os.makedirs(output_path)

for image in images:
    grayscale_image(image, output_path + image)
