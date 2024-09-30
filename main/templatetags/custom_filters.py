from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_item2(dictionary, key):
    if isinstance(dictionary, dict):
        return dictionary.get(key, "не вказано")
    return "не вказано"