#!/usr/bin/python
import sqlite3
import sys
import os

db = sqlite3.connect('%s/data/dictcc.db' % os.path.dirname(os.path.realpath(sys.argv[0])))

while True:
    try:
        query = raw_input('\33[30m\33[43mdictcc>\033[49m\33[39m ').strip()
        c = db.cursor()
        # you weren't going to stick this behind a http server were you?
        q='select de,en from deen where deen match "%s" order by (de like "%s %%") + (en like "%s %%") asc' % (query, query, query)
        print q
        c.execute(q)
        for (de,en) in c.fetchall():
            print u'{:<50}\t{}'.format(de, en)
    except EOFError:
        db.close()
        print
        sys.exit()
