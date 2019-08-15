#!/bin/env python3

from conf import TS_DIR, MP4_DIR

import subprocess
import glob
import json

ts_files = glob.glob(TS_DIR + '/*.m2ts')
ts_files.sort()

def check_streams(streams):
    print(json.dumps(streams, indent=2))
    cn = []
    for stream in streams.values():
        if 'codec_name' in stream:
            cn.append(stream['codec_name'])
    if len(streams) != 10:
        print(len(streams), cn)
        return True
    return True

for i, ts_file in enumerate(ts_files):
    if not '190726-2200' in ts_file:
        continue
    cmd = ['ffprobe', '-i', ts_file, '-loglevel', 'quiet', '-show_streams', '-print_format', 'json']
    output = subprocess.check_output(cmd)
    streams = {}
    for stream in json.loads(output.decode('utf-8'))['streams']:
        streams[int(stream['index'])] = stream
    if check_streams(streams):
        print('{}/{} {} {}'.format(i + 1, len(ts_files), ts_file, streams[0]['codec_name']))

