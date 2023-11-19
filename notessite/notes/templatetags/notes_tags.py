from django import template
from ..models import *

register = template.Library()

# Необходимо для упрощенного отображения в шаблоне
@register.simple_tag(name='notes')
def get_notes():
    return Note.objects.all()