#!/usr/bin/env python3

from config import CONN, CURSOR
from lib.song import Song


if __name__ == '__main__':
    import pdb; pdb.set_trace()

    # Call the create_table method
    Song.create_table()
