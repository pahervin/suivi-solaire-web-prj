# monitoring/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Accède à un élément d'un dictionnaire avec une clé dynamique."""
    return dictionary.get(key, 0)