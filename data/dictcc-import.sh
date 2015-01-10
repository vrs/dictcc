#!/bin/sh
# step 1: get the dictionary file
# http://www1.dict.cc/translation_file_request.php
# step 2: edit and run this script
rm -f dictcc.db deen-sanitized.txt
grep "^[^#	]\+	[^	]\+	[^	]*$" dict.cc-de-en-1382462239.txt |sed 's/"/\\"/g'> deen-sanitized.txt
sqlite3 dictcc.db <<EOF
create virtual table deen using fts4(de, en, type, tokenize=unicode61 "remove_diacritics=0");
.separator "\t"
.import deen-sanitized.txt deen
EOF
