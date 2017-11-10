---
layout: page
title: TemPy Objects
permalink: /usage/objects/
---
## Tag Creation
```python
page = Html()
div = Div()

new_page = page.clone()

new_page_2 = page + div
new_page_3 = new_page_2 - div
list_of_5_divs = div * 5
```

Create DOM elements by instantiating tag classes. Those elements are nodes in the DOM tree and can be attached, detached, moved and composed together dynamically.

There are other 2 ways to create TemPy objects:

* using the `clone()` API
* adding subtracting or multiplying TemPy objects


## Tag Attributes

```python
div = Div(id='my_html_id', klass='someHtmlClass') # 'klass' because 'class' is a Python's buildin keyword
>>> <div id="my_dom_id" class="someHtmlClass"></div>

a = A(klass='someHtmlClass')('text of this link')
a.attr(id='another_dom_id')
a.attr({'href': 'www.thisisalink.com'})
>>> <a id="another_dom_id" class="someHtmlClass" href="www.thisisalink.com">text of this link</a>
```

```python
div2.css(width='100px', float='left')
div2.css({'height': '100em'})
div2.css('background-color', 'blue')
>>> <div id="another_dom_id" class="someHtmlClass comeOtherClass" style="width: 100px; float: left; height: 100em; background-color: blue"></div>
```

HTML tag attributes can be managed in two ways: you can add attributes to every element at definition time (TemPy object instantiation) `Div(my_html_attribute='my_html_attribute_value')` or later using the API.

TemPy supports normal and boolean (attributes with no explicit value) HTML attributes. To define a boolean attribute just assign `bool`, `True` or `False` to the attribute in TemPy: `Div(normal_attribute='foo', boolean_attribute=bool)` (a boolean attribute with `False` value will not be rendered).

TemPy supports multiple, space separated, attributes like the HTML `class` attribute. In TemPy these are attributes that should contain iterables.

Few exceptions are needed, for some common HTML attributes names (i.e: 'class', 'type', etc..) are Python native keyword and can not be used as argument names, those are mapped to custom TemPy names:

* `klass` -> 'class'
* `typ` -> 'type'
* `_for` -> 'for'

Another kind of managed attributes are the mapping kind, like the `style` tag attribute. Style can be managed using passing a dictionary to the `style` attribute directly (`Div(style={'background-color': 'blue'})`), or can be edited in the jQuery fashion with the `.css()` method.

The `css` method mimic the jQuery's brother behavior:

* called with no arguments returns the style dictionary: `Div(style={'color': 'white'}).css() -returns-> {'color': 'white'}`
* called with a dict as the only unnamed argument will `dict.update` the element's style with the given imput: `Div().css({'color': 'white'})`
* called with kwargs will `dict.update` the element's style with the given kwargs: `Div().css(color='white')`


## Building the DOM

```python
page = Html()

# single insertion
page(Head())
>>> <html><head></head></html>

# list insertion
page([Div() for _ in range(2)])
>>> <html><head></head><div></div><div></div></html>

# insertion from generator
page(Span() for _ in range(2))
>>> <html><head></head><div></div><div></div><span></span><span></span></html>

# named insertion
page(some_name='some content')
>>> <html><head></head><div></div><div></div><span></span><span></span>some content</html>
page.some_content = 'some other content'
>>> <html><head></head><div></div><div></div><span></span><span></span>some other content</html>

# mixing up
Html()(
    Head()(
        Title()('Page title')
    ),
    body=Body()(
        'Hello world!',
        'Here some multiplications! ',
        interesting_data=[Div()(n * n2 for n2 in range(10)) for n in range(10)]
    )
)
```

```python
body = Body()
page.append(body)
>>> <html><head></head><body></body></html>
div = Div().append_to(body)
>>> <html><head></head><body><div></div></body></html>
div.append('This is some content', Br(), 'And some Other')
>>> <html><head></head><body><div>This is some content<br>And some Other</div></body></html>
```

```python
head.remove()
>>> <html><body><div></div></body></html>
body.empty()
>>> <html><body></body></html>
page.pop()
>>> <html></html>
```

Add TemPy elements end content to a TemPy object by calling this objects like a function. Every call will place the elements at the end of the container's children list.

It's possible to feed a TemPy object with a single element, a list of element, or a generator of elements. Insertion can also be done giving names to a particular child, so it can be accessed later by name like an attribute of his container element.

<aside class="warning">
Correct ordering with named Tag insertion is ensured with Python >= 3.6 (because kwargs are ordered)
</aside>

Insertion can be mixed, but named insertion can not be before an unnamed insertion.

Another way to manipulate the DOM is to use one of the jQuery-like api.

api | action
-------------- | --------------
div1.after(div2) | div1 will be the sibling next to div2 inside div2's container | div1
div1.before(div2) | div1 will be the sibling before div2 inside div2's container | div1
div1.prepend(div2) | div2 will be the first child of div1 | div1
div1.prepend_to(div2) | div1 will be the first child of div2 | div1
div1.append(div2) | div2 will be the last child of div1 | div1
div1.append_to(div2) | div1 will be the list child of div2 | div1
div1.wrap(div2) | div1 will be the only child of div2
div1.wrap_inner(div2) | div1 will be added between div2 and his previous parent
div1.replace_with(div2) | elements will be swapped
div1.remove(div2) | div2 will be removed from div1
div1.move_childs(div2) | all the children of div1 will be moved to div2
div1.move(div2) | div1 will be detached from his father and moved inside div2
div1.pop() | pop by index from div1 children
div1.empty() | deletes all div1 children.

## Traversing the DOM
```python
container = Div()(Span() for _ in range(2))
for span in container:
    span('some text')
>>> <div><span>some text</span><span>some text</span></div>
```

```python
container = Div()(Span() for _ in range(2))
container[1]('some text')
>>> <div><span></span><span>some text</span></div>
```

```python
container_div = Div()
container_div(content_div=Div())

container_div.content_div('Some content')
>>> <div><div>Some content</div></div>
```

Every TemPy Tag is iterable and accessible like a Python list, iteration over a TemPy object is an iteration over his children.

It's also possible to access some child by name, as if they're attributes of the parent.

A jQuery-ish is given to access TemPy instance's children:
<code id='lefty-code'>container_div.children()
container_div.first()
container_div.last()
container_div.next()
container_div.next_all()
container_div.prev()
container_div.prev_all()
container_div.parent()
container_div.slice(from_index, to_index)
</code>