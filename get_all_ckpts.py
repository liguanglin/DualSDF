import os
import argparse

parser = argparse.ArgumentParser(description='Train all')
parser.add_argument('--logs', default="./logs")
                    
args = parser.parse_args()

category_ids = ['02876657', '02880940', '02942699', '02946921', '03642806', '03797390']
category_names = ['bottle', 'bowl', 'camera', 'can', 'laptop', 'mug']

new_dir = "./DualSDF_ckpts"
os.makedirs(new_dir, exist_ok=True)

for cate in category_names:
    os.makedirs(f"{new_dir}/{cate}/256/", exist_ok=True)
    os.system(f"cp {args.logs}/dualsdf_{cate}_256/checkpoints/epoch_9999*.pth {new_dir}/{cate}/256/epoch_9999.pth")



