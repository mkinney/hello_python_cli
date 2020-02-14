# Simple CLI python program using docopt with tests

```
virtualenv -p python3 venv
source venv/bin/activate
create .envrc
direnv allow
pip install docopt pytest flake8
```

Configure git to use pre-commit hook

```
flake8 --install-hook git
```

# To install 'hello':

```
python setup.py install
```

# To test:

```
pytest
```

# Notes:
1. A push will publish to test.pypi.org
2. If you tag a version, it will get pushed to pypi.org
  git commit -m 'bump to v0.0.5'
  git tag v0.0.5
  git push origin v0.0.5
  git push


# Want zsh completion?
1. add these lines to ~/.zshrc

```
fpath=($HOME/.zsh-completions $fpath)
autoload -U compinit
compinit
```

2. Copy script to something in fpath (run `echo $fpath` to see value)

```
cp _hello ~/.zsh-completions/
```

3. reload zsh

```
exec zsh
```

4. try it out...

```
hello --<tab>
```

# Want bash completion?
1. Install bash-completion (assuming mac):

```
brew install bash-completion
```

2. Add to bash startup file:

```
echo "[ -f /usr/local/etc/bash_completion ] && . /usr/local/etc/bash_completion" >> ~/.bash_profile
```

3. Reload bash profile (only need to do this once)

```
source ~/.bash_profile
```

4. Copy file

```
cp hello_completion.sh /usr/local/etc/bash_completion.d/hello
```

5. Try it out

```
hello --<tab>
```
