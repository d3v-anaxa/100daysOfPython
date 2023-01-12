# using os module to do system level tasks

import os

if (not os.path.exists(f"folders")):
    for folder in range(100):
        os.system(
            f"mkdir -p folders/day_{folder+1};cd folders/day_{folder+1};touch main.py README.md;cd ../../")

else:
    os.system("rm -rf folders")
