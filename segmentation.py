
import numpy as np
from skimage.transform import resize
from skimage import measure
from skimage.measure import regionprops
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import cca

# The invert was done so as to convert the black pixel to white pixel and vice versa
license_plate = np.invert(cca.plate_like_objects[2])

labelled_plate = measure.label(license_plate)

fig, ax1 = plt.subplots(1)
ax1.imshow(license_plate, cmap="gray")

# assuming that width of license plate should be btwn 5-15% of license and height will be 35-60%
character_dimensions = (0.35*license_plate.shape[0], 0.60*license_plate.shape[0], 0.05*license_plate.shape[1], 0.15*license_plate.shape[1])
min_height, max_height, min_width, max_width = character_dimensions

characters = []
counter=0
column_list = []
for regions in regionprops(labelled_plate):
    y0, x0, y1, x1 = regions.bbox
    region_height = y1 - y0
    region_width = x1 - x0

    if region_height > min_height and region_height < max_height and region_width > min_width and region_width < max_width:
        roi = license_plate[y0:y1, x0:x1]

        # draw red bordered rectangle over the character
        rect_border = patches.Rectangle((x0, y0), x1 - x0, y1 - y0, edgecolor="red",linewidth=2, fill=False)
        ax1.add_patch(rect_border)

        # resize characters to 20X20 and append each character into the characters list
        resized_char = resize(roi, (20, 20))
        characters.append(resized_char)

        # this is to keep track of arrangement of characters
        column_list.append(x0)

plt.show()