from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def nbsp(value):
    return mark_safe("<br>".join(("&nbsp;".join(value.split(' '))).split('\n')))