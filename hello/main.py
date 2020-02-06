"""
Usage:
  hello [options] [NAME]

Options:
  -h, --help          Print help info
  -d, --debug         Print debug info
  -t, --title TITLE   Title to use (ex: Mr.)

"""
from docopt import docopt

from hello import Hello

if __name__ == '__main__':
    arguments = docopt(__doc__)

    debug = arguments['--debug']
    if debug:
        print('arguments:', arguments)

    name = arguments['NAME']
    if not name:
        name = 'world'
    title = arguments['--title']

    h = Hello(name)
    if title:
        h.title = title
    print(h.hello())
