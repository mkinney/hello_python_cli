"""
Usage:
  hello [options] [NAME]

Options:
  -d, --debug         Print debug info
  -h, --help          Print help info
  -t, --title TITLE   Title to use (ex: Mr.)
  --version           Print version

"""
from docopt import docopt

from hello import Hello

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')

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
