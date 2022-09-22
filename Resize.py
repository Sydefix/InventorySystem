

from PIL import Image
import glob

image_list = glob.glob("./assets/*.png")

for i in image_list:
    test = Image.open(i)
    max_size = max(test.size)
    print( test.size, end=" ")
    new_test = test.resize((max_size, max_size))
    print( new_test.size, end=" ")

    print()
    new_test.save(i.replace("assets", "modified_assets"))