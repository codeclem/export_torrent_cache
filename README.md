Most torrent clients maintain a directory containing all the torrents that are currently loaded in the client.
However they are unorganized and typically have been renamed to the infohash of the torrent. This script processes these torrents
and restores them to their original name and organized by tracker based on the announce URL. It was written with private torrents in mind, which
generally only have one announce URL. If the script encounters a torrent with multiple announce URLs,
it will only consider the first URL for organization.

This has only been tested with qBittorrent, but it should work with any directory containing a flat list of valid torrents. Subdirectories are not traversed.

## Dependencies:
* [torrent_parser](https://github.com/7sDream/torrent_parser)

## Usage:
```
$ export_torrent_cache <source_dir> <destination_dir>
```

## Examples:
```
$ ls ~/.local/share/data/qBittorrent/BT_backup/
[lots of .torrent files with unhelpful names]

$ export_torrent_cache ~/.local/share/data/qBittorrent/BT_backup/ ~/torrents_backup
Processing ~/.local/share/data/qBittorrent/BT_backup/[infohash].torrent 
All torrents processed succesfully

$ tree ~/torrents_backup
~/torrents_backup
├── Tracker URL
│   ├── Original_Filename.torrent

```

## Installation
### From PyPI
```
$ pip install export_torrent_cache
```

### From source repository
```
$ git clone https://github.com/codeclem/export_torrent_cache
$ cd export_torrent_cache
```
From here you can manually install `torrent_parser` and run the `export_torrent_cache.py` script directly, or build and install a package like so:
```
$ python setup.py sdist
$ pip install dist/export_torrent_cache-0.1.tar.gz
```
Which will also fetch and install `torrent_parser` as a dependency for you.
