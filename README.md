# Fluention

Providing [fluent interfaces](https://en.wikipedia.org/wiki/Fluent_interface)
for functions and methods for python.

Unlike what
[Guideo](https://mail.python.org/pipermail/python-dev/2003-October/038855.html)
discouraged, these functions are without side effects and therefore should be
rather obvious in intent. and usage.

## Example

```python
@fluent(arg="color", func_name="with_color")
@fluent(arg="long_ears", func_name="with_long_ears", default_value=True)
@fluent(arg="long_ears", func_name="with_short_ears", default_value=False)
def new_dog(name, long_ears, color):
  ...
new_dog().with_long_ears().with_color(color.BROWN)
```
