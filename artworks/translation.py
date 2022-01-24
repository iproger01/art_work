from modeltranslation.translator import register, TranslationOptions
from .models import Artworks, Artists, Category, Comment, Technic

@register(Artists)
class ArtistsTranslationOptions(TranslationOptions):
    fields = ('name','surname','patronymic','location','description','education')

@register(Artworks)
class ArtworksTranslationOptions(TranslationOptions):
    fields = ('name','description','country','location','owner','signature','certificate_of_auth')

@register(Technic)
class TechnicTranslationOptions(TranslationOptions):
    fields = ('name','description')

@register(Comment)
class CommentTranslationOptions(TranslationOptions):
    fields = ('name', 'text',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name','description')