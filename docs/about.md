---
layout: page
title: Project Info
permalink: /about/
---

## Compatibility

**Python >= 3 is a must**, there is no intention to backport this project to Python 2.7.

**Python >= 3.3 is needed**, for TemPy uses the delegation to subgenerator (the `yield from` statement) proposed in [PEP 380](https://www.python.org/dev/peps/pep-0380/).

This form of yielding is used for speed and can be easily removed if you plan to use TemPy in Python 3.0 to 3.2.x , you'll just need to substitute the `yield from` with a loop on the inner generator yielding single values.


**Python >= 3.6 is preferred**, some useful features depends on the preserved order of kwargs proposed in [PEP 468](https://www.python.org/dev/peps/pep-0468/).

The main feature is the possibility to have named child tags in the correct order. Naming child tags is possible in Python < 3.6, but the tag's order will probably not be correct.

<aside class="success"><b>It it very reccomended to use TemPy with Python >= 3.6.</b></aside>

## Status

Current [PyPi](https://pypi.org/project/tem-py/) version

[![PyPI version](https://badge.fury.io/py/tem-py.svg)](https://badge.fury.io/py/tem-py)

[Coveralls](https://coveralls.io/github/Hrabal/TemPy?branch=master) CI Test coverage

[![Coverage Status](https://coveralls.io/repos/github/Hrabal/TemPy/badge.svg?branch=master)](https://coveralls.io/github/Hrabal/TemPy?branch=master)

[Travis](https://travis-ci.org/Hrabal/TemPy) CI Build status

[![Build Status](https://travis-ci.org/Hrabal/TemPy.svg?branch=master)](https://travis-ci.org/Hrabal/TemPy)

# Apache 2.0
See [licence](licence) for details.

# Credits

## Made and maintained by Federico Cerchiari

Get in touch on GitHub: [Hrabal](https://github.com/Hrabal)

Get in touch using Slack: [tempy-dev.slack.com](https://tempy-dev.slack.com/messages)

## Contribute
Any contribution is welcome. Please refer to the [contributing page](https://github.com/Hrabal/TemPy/blob/master/CONTRIBUTING.md) on the master GitHub repo.