from django import template

register = template.Library()

@register.filter(name='dict_key')
def dict_key(dictionary, key):
    # Fetch the dictionary item by key
    value = dictionary.get(key)
    # Return 'approved' status if it exists in the nested dictionary
    return value.get('approved') if isinstance(value, dict) else None