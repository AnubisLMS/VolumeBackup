import json
import sys
import os
import multiprocessing as mp
import subprocess as sp
from parse import parse

backup_host = sys.argv[1]
backup_host_path = sys.argv[2]

volumes = json.load(open('./volumes.json'))
netids = [parse("ide-volume-{}", v)[0] for v in volumes]

template = open('job.yml.tmpl').read()

os.makedirs('jobs', exist_ok=True)
for netid in netids:
    print(netid)
    job_yaml = template.format(
        netid=netid,
        backup_host=backup_host,
        backup_host_path=backup_host_path,
    )
    with open(f'jobs/{netid}.yml', 'w') as f:
        f.write(job_yaml)
    



