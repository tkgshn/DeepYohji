import better_exceptions
import os
import glob
from PIL import Image

files = glob.glob('/Users/shunsuketakagi/opt/anaconda3/envs/py/GAN/input_photos/*.jpg')
a = 0
for f in files:
    a += 1
    img = Image.open(f)
    img_resize = img.resize((128, 128))
    ftitle, fext = os.path.splitext(f)
    img_resize.save('/Users/shunsuketakagi/opt/anaconda3/envs/py/GAN/output_photos' + str(a) + '_(300x300)' + fext)
print(a, end=", ")