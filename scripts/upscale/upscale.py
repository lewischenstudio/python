from super_image import EdsrModel, ImageLoader
from PIL import Image
import os

cwd = os.path.join(os.getcwd(), "upscale_images")
onlyfiles = [
    {"file_name": f.split(".")[0], "path": os.path.join(cwd, f)}
    for f in os.listdir(cwd)
    if os.path.isfile(os.path.join(cwd, f))
]
print(onlyfiles)
for item in onlyfiles:
    image = Image.open(item["path"])
    model = EdsrModel.from_pretrained("eugenesiow/edsr-base", scale=4)
    inputs = ImageLoader.load_image(image)
    preds = model(inputs)

    new_file_name = item["file_name"] + "_4k"
    ImageLoader.save_image(preds, f"./upscale_images/4k/{new_file_name}.png")
    os.remove(item["path"])
