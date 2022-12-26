import numpy as np
import open3d
from glob import glob
import os
import argparse

parser = argparse.ArgumentParser(description='NPY processing')
parser.add_argument('obj_dir', default="./obj_modesl/train/", type=str, help='NOCS .obj dictionary.')
parser.add_argument('npy_dir', default="./NOCS_npy/", type=str, help='.npy output dictionary.')
args = parser.parse_args()

obj_dir = args.obj_dir
npy_dir = args.npy_dir

cate_dirs = glob(obj_dir+'/*')
all_categories = ['02876657', '02880940', '02942699', '02946921', '03642806', '03797390']

for cate_dir in cate_dirs:
    cate = cate_dir.split('/')[-1]
    obj_files = glob(cate_dir+'/*/*.obj')
    if(cate not in all_categories):
        continue
    print('{}/{}'.format(npy_dir, cate))
    os.makedirs('{}/{}'.format(npy_dir, cate), exist_ok=True)
    for obj in obj_files:
        mesh = open3d.io.read_triangle_mesh(obj)
        vertices = np.array(mesh.vertices)
        triangle = np.array(mesh.triangles)
        #print(triangle.shape, vertices.shape)
        obj_name = obj.split('/')[-2]
        obj_npy = vertices[triangle]
        #print(obj_npy.shape)
        np.save('{}/{}/{}.npy'.format(npy_dir, cate, obj_name),obj_npy)
        
print('DONE')
    
