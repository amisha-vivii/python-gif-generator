from PIL import Image
import os

folder = "images"
images = []

for file in sorted(os.listdir(folder)):
    if file.endswith(".png") or file.endswith(".jpg"):
        img = Image.open(os.path.join(folder, file))
        images.append(img)

images[0].save(
    "my_gif.gif",
    save_all=True,
    append_images=images[1:],
    duration=500,
    loop=0
)

print("GIF created successfully as my_gif.gif")
