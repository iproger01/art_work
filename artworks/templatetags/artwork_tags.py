from django import template
from artworks.models import Category, Artworks

register = template.Library()

@register.simple_tag()
def get_categories():
    """Вывод всех категорий в header"""
    return Category.objects.all()

@register.inclusion_tag('artworks/tags/last_artwork.html')
def get_last_artwork(count=5):
    """Вывод последних """
    artworks = Artworks.objects.order_by("id")[:count]
    return {"last_artwork":artworks}