---
layout: page
title: Blocks
permalink: /usage/blocks/
---
```python
# --- file: base_elements.py
from tempy.tags import Div, Img, Ul, Li, A
from somewhere import links, foot_imgs
# define some common blocks
header = Div(klass='header')(title=Div()('My website'), logo=Img(src='img.png'))
menu = Div(klass='menu')(Ul()((Li()(A(href=link)) for link in links))
footer = Div(klass='coolFooterClass')(Img(src=img) for img in foot_imgs)
```

```python
# --- file: pages.py
from tempy.tags import Html, Head, Body
from base_elements import header, menu, footer

# import the common blocks and use them inside your page
home_page = Html()(Head(), body=Body()(header, menu, content='Hello world.', footer=footer))
content_page = Html()(Head(), body=Body()(header, menu, Content('header'), Content('content'), footer=footer))
```

```python
# --- file: my_controller.py
from tempy.elements import Content
from tempy.tags import Div
from pages import home_page, content_page

@controller_framework_decorator
def my_home_controller(url='/'):
    return home_page.render()

@controller_framework_decorator
def my_content_controller(url='/content'):
    header = Div()('This is my header!')
    content = "Hi, I'm a content"
    return content_page.render(header=header, content=content)
```

```python
from tempy import Escaped

_ = Div()(Escaped("""<p>
here is some html I had in my closet
</p>
"""))
```

TemPy lets you build blocks and put them together using the manipulation api, each TemPy object can be used later inside another TemPy object.

Static parts of pages can be created once an then used in different pages. Blocks can be created and imported as normal Python objects.

<aside class="warning">Depending on the web framework you use, TemPy instances can be shared between http requests. Keep in mind that if you modify a TemPy instance used in various pages, this will be modified in every page and in every subsequent request.</aside>


## Content

To make a Block a dynamic, so it can contain different contents each request/use, we can use TemPy's `Content` class.

Those elements are just containers with no html representation, at render time this children will be rendered inside the `Content`'s father. `Content` can have a fixed content so it can be used as 'html invisible box' (this fixed content can, however, be dynamic), or it can just have a name.

Every TemPy objects can contain extra data that will not be rendered, you can manage this extra data with the `TemPyClass.data()` api as if it's a common dictionary. At render time TemPy will search into the extra data of the `Content` container, and recursively into his parents, looking for a key matching the `Content`'s name. If it's found then it's value is used in rendering.

<code id='lefty-code'>container = Div()(
    Content(content='This is a fixed content')
)
container.render()
&gt;&gt;&gt; &lt;div&gt;This is a fixed content&lt;/div&gt;
</code>

<code id='lefty-code'>container = Div()(
    Content('a_content_name')
)
container.data({'a_content_name': 'This is dynamic content'})
container.render()
&gt;&gt;&gt; &lt;div&gt;This is dynamic content&lt;/div&gt;
</code>

<code id='lefty-code'>root_container = Span()
container = Div()(
    Content('a_content_name')
)
root_container.append(container)
root_container.inject({'a_content_name': 'This is dynamic content'})
root_container.render()
&gt;&gt;&gt; &lt;span&gt;&lt;div&gt;This is dynamic content&lt;/div&gt;&lt;/span&gt;
</code>

Another special TemPy class is the `Escaped` class. With this class you can add content that will not be html escaped, it's useful to inject plain html blocks (in string format) into a TemPy tree.
