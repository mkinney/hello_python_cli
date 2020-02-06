"""
Usage:
  hello [-t TITLE ] [NAME]

Options:
  -h, --help          Print help info
  -t TITLE            Title to use (ex: Mr.)

"""
from docopt import docopt

from hello import Hello
#import Hello

if __name__ == '__main__':
    arguments = docopt(__doc__)

    print(arguments)

    name = arguments['NAME']
    if not name:
        name = 'world'
    title = arguments['-t']

    h = Hello(name)
    if title:
        h.title = title
    print(h.hello())
