# connected component analysis (identify all connected regions in the image)
# helps group and label connected regions on the foreground

from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import localization

label_image = measure.label(localization.binary_car_image)

plate_dimensions = (0.08*label_image.shape[0], 0.2*label_image.shape[0], 0.15*label_image.shape[1], 0.4*label_image.shape[1])
min_height, max_height, min_width, max_width = plate_dimensions
plate_objects_cordinates = []
plate_like_objects = []
fig, (ax1) = plt.subplots(1)
ax1.imshow(localization.gray_car_image, cmap="gray")

# regionprops creates list of properties of all labeled regions
for region in regionprops(label_image):
    # if region is too small, then its most likely not a license plate 
    if region.area < 50:
        continue

    # bounding box coords
    minRow, minCol, maxRow, maxCol = region.bbox
    region_height = maxRow - minRow
    region_width = maxCol - minCol
    # ensuring current region matches typical license plate sizing
    if region_height >= min_height and region_height <= max_height and region_width >= min_width and region_width > region_height:
        plate_like_objects.append(localization.binary_car_image[minRow:maxRow, 
                                                                minCol:maxCol])
        
        plate_objects_cordinates.append((minRow, minCol, maxRow, maxCol))
        rectBorder = patches.Rectangle((minCol, minRow), maxCol-minCol, maxRow-minRow, edgecolor="red", linewidth=2, fill=False)
        ax1.add_patch(rectBorder)
        # Drawing red rectangle over those regions

plt.show()