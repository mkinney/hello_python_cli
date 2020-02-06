Simple python program

virtualenv -p python3 venv
source venv/bin/activate
create .envrc
direnv allow

pip install docopt pytest flake8

# Configure git to use pre-commit hook
flake8 --install-hook git
