#!/bin/env python3

# ディレクトリにあるTSファイルをすべてMP4ファイルに変換する
# すでに変換後ファイルがある場合はスキップ

import subprocess
import glob
import json
import os.path

M2TS_DIR = r'\\hs2500k\m2ts'
DEST_DIR = r'd:/tv'

m2ts_files = glob.glob(M2TS_DIR + '/*.m2ts')
m2ts_files.sort()

for i, m2ts_file in enumerate(m2ts_files):

    # 特定のファイルのみエンコード (開発用)
    # if not '181230-1505' in m2ts_file:
    #   continue

    # ディレクトリ名を削除し、ファイル名のみ取得
    name = os.path.basename(m2ts_file)

    # 保存先ファイル名の決定
    dest_file = DEST_DIR + "/" + name[:-5] + ".mp4"

    # すでに保存先にファイルがあればスキップ
    if os.path.exists(dest_file):
        continue

    # 変換オプション
    cmd = [
        'ffmpeg5',
        # '-analyzeduration', '30M', '-probesize', '30M',
        # '-deint', '2', '-drop_second_field', '1',
        '-i', m2ts_file,
        '-vcodec', 'h264_nvenc',
        '-vsync', '1', '-async', '1',
        dest_file
    ]
    
    print('{}/{} {}'.format(i + 1, len(m2ts_files), name))
    # print(cmd)
    subprocess.call(cmd)

# 画質調整の参考に
# http://yellowyallow.blogspot.com/2015/07/ffmpeg-h265hevc-nvidia-gpu.html
