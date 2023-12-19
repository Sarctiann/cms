import sys
from os import path

from PIL import Image

ASSETS_FOLDER = path.join(path.dirname(__file__), "..", "..", "assets")

print(ASSETS_FOLDER)

try:
    file_name = sys.argv[1].replace(".png", "")
except:
    print("Please specify a file name.")
    sys.exit()

source_file = path.join(ASSETS_FOLDER, f"{file_name}.png")
target_file = path.join(ASSETS_FOLDER, "favicon.ico")


assert path.exists(source_file), FileNotFoundError("The file does not exist.")

img = Image.open(source_file)
img.save(target_file)
