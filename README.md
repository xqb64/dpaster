# dpaster

[![Build Status](https://travis-ci.org/xvm32/dpaster.svg?branch=master)](https://travis-ci.org/xvm32/dpaster) [![Coverage Status](https://coveralls.io/repos/github/xvm32/dpaster/badge.svg?branch=master)](https://coveralls.io/github/xvm32/dpaster?branch=master) [![PyPI version](https://badge.fury.io/py/thepaster.svg)](https://pypi.org/project/thepaster/1.1.1/) [![PyPI](https://img.shields.io/badge/status-stable-brightgreen.svg)](https://pypi.org/project/thepaster/1.1.1/) 

**dpaster** is a command-line client interface for [dpaste](https://dpaste.org/).

## Installing dpaster

```sh
pip install thepaster
```

## Using dpaster

```sh
$ dpaster --help
Usage: dpaster [OPTIONS] COMMAND [ARGS]...

  Client interface for https://dpaste.org/ pastebin

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  config  Configure available settings
  paste   Paste to dpaste.org
```

## Configuring dpaster

```sh
$ dpaster config --help
Usage: dpaster config [OPTIONS]

  Configure available settings

Options:
  --show                          View current settings
  --enable-autocp / --disable-autocp
                                  Automatically copy the URL to clipboard
  --default-lexer OPT             Choose default lexer (e.g. python, java,
                                  bash)

  --default-expires OPT           Choose default expiry time (e.g. onetime,
                                  hour, day, week)

  --help                          Show this message and exit.
```

## Licensing

Licensed under the [MIT License](https://opensource.org/licenses/MIT). For details, see [LICENSE](https://github.com/xvm32/dpaster/blob/master/LICENSE).


