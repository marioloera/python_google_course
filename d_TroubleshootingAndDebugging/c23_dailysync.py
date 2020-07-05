

#!/usr/bin/env python3
import subprocess
from multiprocessing import Pool
import os

src = "data/prod/"
dest = "data/prod_backup/"

#subsrcs = []
for root, dirs, files in os.walk(src, topdown=False):
   # for name in files:
      # print(os.path.join(root, name))
   # for name in dirs:
      # print('\t', os.path.join(root, name))
   subsrcs = dirs
print(subsrcs)

def run(subsrc):
        # Do something with task here
        # print("Handling {}".format(task))
        src = "data/prod/" + subsrc
        print(src)
        dest = "data/prod_backup/" + subsrc
        #print(dest)
        subprocess.call(["rsync", "-arq", src, dest])

p = Pool(len(subsrcs))
p.map(run, subsrcs)

print('done!')

