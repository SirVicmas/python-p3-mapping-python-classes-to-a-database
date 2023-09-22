#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song


if __name__ == '__main__':
    import ipdb; ipdb.set_trace()


Song.create_table()
CURSOR.execute("PRAGMA table_info(songs)").fetchall()