import os
import matplotlib.pyplot as plt
from PIL import Image

classes_dir = '<Train_Directory_Path>'

classes = os.listdir(os.path.join(classes_dir, 'train'))

for exp in classes:
    images_dir = os.path.join(classes_dir, 'train', exp)
    images = os.listdir(images_dir)
    for image in images:
        img = Image.open(os.path.join(images_dir, image))
        print(img)

        r_fliped = img.transpose(Image.FLIP_LEFT_RIGHT)
        rotate_l = img.rotate(90)
        rotate_r = img.rotate(-90)
        t_fliped = img.transpose(Image.FLIP_TOP_BOTTOM)
        
        
        r_fliped.save(os.path.join(images_dir, f'{image}_Flr.jpg'))
        rotate_r.save(os.path.join(images_dir, f'{image}_Rr.jpg'))
        rotate_l.save(os.path.join(images_dir, f'{image}_Rl.jpg'))
        t_fliped.save(os.path.join(images_dir, f'{image}_tb.jpg'))
            
            
        
