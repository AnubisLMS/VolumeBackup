import os
import time

jobs = os.listdir('jobs')
N = 5

for index, job in enumerate(jobs):
    cmd = f'kubectl apply -f jobs/{job}'
    print(index, '::', cmd)
    os.system(cmd)

    if (index+1) % N == 0:
        print('waiting')
        time.sleep(2*60)

