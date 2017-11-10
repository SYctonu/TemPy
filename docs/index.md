---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: page
---
# Overview

```python
from tempy.tags import Html, Head, Body, Meta, Link, Div, P, A
my_text_list = ['This is foo', 'This is Bar', 'Have you met my friend Baz?']
another_list = ['Lorem ipsum ', 'dolor sit amet, ', 'consectetur adipiscing elit']

page = Html()(  # add tags inside the one you created calling the parent
    Head()(  # add multiple tags in one call
        Meta(charset='utf-8'),  # add tag attributes using kwargs in tag initialization
        Link(href="my.css", typ="text/css", rel="stylesheet")
    ),
    body=Body()(  # give them a name so you can navigate the DOM with those names
        Div(klass='linkBox')(
            A(href='www.foo.com')
        ),
        (P()(text) for text in my_text_list),  # tag insertion accepts generators
        another_list  # add text from a list, str.join is used in rendering
    )
)
```

```
page.render()
>>> <html>
>>>     <head>
>>>         <meta charset="utf-8"/>
>>>         <link href="my.css" type="text/css" rel="stylesheet"/>
>>>     </head>
>>>     <body>
>>>         <div class="linkBox">
>>>             <a href="www.foo.com"></a>
>>>             <a href="www.bar.com"></a>
>>>             <a href="www.baz.com"></a>
>>>             <a href="www.python.org">This is a link to Python</a>
>>>         </div>
>>>         <p>This is foo</p>
>>>         <p>This is Bar</p>
>>>         <p>Have you met my friend Baz?</p>
>>>         Lorem ipsum dolor sit amet, consectetur adipiscing elit
>>>     </body>
>>> </html>
```

Build HTML without writing a single tag.

HTML is like SQL: we all use it, we know it works, we all recognize it's important, but our biggest dream is to never write a single line of it again. For SQL we have ORM's, but we're not there yet for HTML.

Templating systems are cool (Python syntax in html code) but not cool enough (you still have to write html somehow)..

..so the idea of TemPy.

TemPy let the developer build the DOM using only Python objects and classes. It provides a simple but complete API to dynamically create, navigate, modify and manage "HTML" templates and objects in a pure Python.

Navigating the DOM and manipulating tags is possible in a Python or jQuery-similar syntax. Then later your controllers can serve the page by just calling the `render()` method on the root element.

TemPy is designed to offer Object-Oriented Templating, giving the developer the ability to use and manage html templates following the OOP paradigms. Sublassing, overriding and all the other OOP techniques will make HTML templating more flexible and maintainable.

**Speed**

One of the main slow-speed factors when developing webapps are the template engines. TemPy have a different approach to the HTML generation resulting in a big speed gain.

No parsing and a simple structure makes TemPy fast. TemPy simply adds html tags around your data, and the actual html string exists only at render time.

# Installation

```shell
pip3 install tem-py
```

```shell
git clone https://github.com/Hrabal/TemPy.git
cd TemPy
python3 setup.py install
```

<aside class="notice">TemPy does not support Python 2.x. TemPy requires Python >= 3.3 to work.</aside>

TemPy is avaiable on PyPi, so you can pip him. [PyPi.org](https://pypi.org/project/tem-py/) page.

If you want to customize TemPy you can clone the main [GitHub repo](https://github.com/Hrabal/TemPy).