from glob import glob
from PIL import Image

def get_png_path(tif_pth):
    basename = tif_pth.split("\\")[-1].split(".")[0]
    return f"dataset/dataset_labelme/imgs_png/{basename}.png"

imgs_pths_tif = glob("dataset/dataset_labelme/imgs_tif/*tif")

for img_pth_tif in imgs_pths_tif:
    img = Image.open(img_pth_tif)
    img_pth_png = get_png_path(img_pth_tif)
    img.save(img_pth_png)
    print(f"saved {img_pth_png}")
