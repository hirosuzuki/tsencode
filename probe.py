#!/bin/env python3

# フォルダにあるTSファイルの合計時間を算出する

from conf import M2TS_DIR, DEST_DIR

import subprocess
import glob
import json
import os.path

m2ts_files = glob.glob(M2TS_DIR + '/*.m2ts')
m2ts_files.sort()

all_duration = 0

for i, m2ts_file in enumerate(m2ts_files):

    name = os.path.basename(m2ts_file)
    dest_file = DEST_DIR + "/" + name[:-5] + ".mp4"

    cmd = ['ffprobe', '-i', m2ts_file, '-loglevel', 'quiet', '-show_streams', '-print_format', 'json']
    output = subprocess.check_output(cmd)
    info = {}
    for stream in json.loads(output.decode('utf-8'))['streams']:
        if 'codec_name' in stream:
            if stream['codec_name'] == 'mpeg2video':
                info['width'] = stream.get('width')
                info['height'] = stream.get('height')
                info['duration'] = float(stream.get('duration', 0))

    all_duration += info['duration']

    print('{}/{} {} {}'.format(i + 1, len(m2ts_files), name, info))

    # if i > 10: break

print('all_duration: {}'.format(all_duration))
