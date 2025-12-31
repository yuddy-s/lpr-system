# connected component analysis (identify all connected regions in the image)
# helps group and label connected regions on the foreground

from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import localization

label_image = measure.label(localization.binary_car_image)


fig, (ax1) = plt.subplots(1)
ax1.imshow(localization.gray_car_image, cmap="gray")

for region in regionprops(label_image):
    # if region is too small, then its most likely not a license plate 
    if region.area < 50:
        continue

    minRow, minCol, maxRow, maxCol = region.bbox
    rectBorder = patches.Rectangle((minCol, minRow), maxCol-minCol, maxRow-minRow, edgecolor="red", linewidth=2, fill=False)
    ax1.add_patch(rectBorder)
    # Drawing red rectangle over those regions

plt.show()