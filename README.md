# dictcc
A simple, nearly trivial, offline interface for [dict.cc](http://dict.cc), receiving words on stdin and outputting translations to stdout.

Written to scratch an itch. I'm often deliberately without Internet for a day or two, but sometimes I can't remember a word and need a dictionary. Should also come in handy for various other offline situations you find yourself in, for example long train rides.<br>
It's also faster than the online version once the database is in your cache.<br>
The code and output quality aren't the best, I know. I'll improve this whenever I think my pain outweighs the effort. Pull requests welcome.<br>
This tool wouldn't be possible if dict.cc didn't publish their dataset for free, so hats off to them! (Or whatever your headwear of choice may be)

## Requirements
Python and SQLite 3, optionally rlwrap.

## Installation
1. Download dictcc to somewhere.
2. Get and import the database, for instructions see `data/dictcc-import.sh`.
3. Symlink dictcc.py from your $PATH or call it from a wrapper script and things should work (it's my setup)

## Usage
dictcc.py accepts words on stdin and outputs possible translations.<br>
Call like so (recommended):<br>
`rlwrap dictcc.py`

## License
AGPLv3. I would usually use something more permissive but the [Terms of Use](http://www1.dict.cc/translation_file_request.php) mandate use of the GPL and the program isn't supposed to be internet-facing either. (Can you even legally demand that? I doubt it, but don't look the gift horse in the mouth)

