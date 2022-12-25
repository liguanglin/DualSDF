import os
import argparse
import threading

class Workers(threading.Thread):
    def __init__(self, cmd, gpu):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.gpu = gpu
    def run(self):
        print("gpu:", self.gpu)
        print(self.cmd)
        os.system(f"export CUDA_VISIBLE_DEVICES={self.gpu};{self.cmd}")

parser = argparse.ArgumentParser(description='Train all')
parser.add_argument('--gpus', default=[0], nargs='+', help='vaild gpus.')
                    
args = parser.parse_args()

category_ids = ['02876657', '02880940', '02942699', '02946921', '03642806', '03797390']
category_names = ['bottle', 'bowl', 'camera', 'can', 'laptop', 'mug']
gpu_id = 0

workers = []
for cate in category_names:
    gpu = args.gpus[gpu_id]
    workers.append(Workers(f"python train.py ./config/dualsdf_{cate}_256.yaml", gpu))
    gpu_id = (gpu_id + 1)%len(args.gpus)

for worker in workers:
    worker.start()

