#!/usr/bin/env python3
"""
usage: export_torrent_cache.py [-h] [--version] source_dir destination_dir

Export/backup the cache directory of a torrent client, restoring original filenames and organized by tracker

positional arguments:
  source_dir       Directory containing cached torrents
  destination_dir  Directory to place the new organized torrents. Will be created if it does not exist.

optional arguments:
  -h, --help       show this help message and exit
  --version, -v    print version and exit

"""

import argparse
import torrent_parser
import os
import shutil
import sys
from urllib.parse import urlsplit


VERSION = 0.1

unhandled_torrents = []

def export_torrent(torrent, destination_dir):
    print('Processing ' + torrent)

    try:
        with open(torrent, 'rb') as file:
            # I had some torrent files with an sha1 field that torrent_parser did not expect
            # https://github.com/7sDream/torrent_parser/issues/4 is relevant
            data = torrent_parser.TorrentFileParser(file).hash_field('sha1').parse()
    except Exception as e:
        print('Error parsing ' + torrent)
        print(e)
        unhandled_torrents.append([torrent, e])
        return

    name = data['info']['name']
    tracker = urlsplit(data['announce']).hostname

    dest = os.path.join(destination_dir, tracker)
    if not os.path.exists(dest):
        os.makedirs(dest)

    shutil.copy(torrent, os.path.join(dest, name + '.torrent'))


def main():
    parser = argparse.ArgumentParser(description='Export/backup the cache directory of a torrent client, restoring original filenames and organized by tracker')

    parser.add_argument('--version', '-v', action='version', version='%(prog)s ' + str(VERSION), default=False,
                        help='print version and exit')

    parser.add_argument('source_dir', type=str,
                        help='Directory containing cached torrents')

    parser.add_argument('destination_dir', type=str,
                        help='Directory to place the new organized torrents. Will be created if it does not exist.')

    args = parser.parse_args()

    for file in os.listdir(args.source_dir):
        if file.endswith('.torrent'):
            export_torrent(os.path.join(args.source_dir, file), args.destination_dir)

    if unhandled_torrents:
        print('Unable to process the following torrents:')
        for torrent in unhandled_torrents:
            print(torrent[0])
            print(torrent[1])
            sys.exit(1)
    else:
        print('All torrents processed succesfully')


if __name__ == '__main__':
    main()
