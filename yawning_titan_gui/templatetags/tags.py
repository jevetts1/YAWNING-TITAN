import json

from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

register = template.Library()

# basic helper tags


@register.filter(is_safe=True)
def js(obj):
    """Return argument in javascript markup.

    Args:
        obj: An object to be converted to json format.

    Returns:
        Json formatted representation of `obj`
    """
    return mark_safe(json.dumps(obj))


@register.filter
def to_id(value: str):
    """Replaces spaces with dashes in string argument to form html formatted id.

    Args:
        value: A string value to be converted to an standard format html id.

    Returns:
        The original string with spaces replaced with '-'.

    Examples:
        >>{{'my object a'|to_id}}
        >>my-object-a
    """
    return value.replace(" ", "-")


@register.filter
def get_url(url_name: str):
    """
    Wrapped implementation of Django's reverse url.

    A lookup that returns the url by name
    or empty string when the url does not exist.

    Args:
        url_name: The name of the url string as defined
        in `urls.py`.

    Returns:
        The full url string as defined in `urls.py`
    """
    try:
        return reverse(url_name)
    except Exception:
        return ""
