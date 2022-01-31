from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from django import forms
from modeltranslation.admin import TranslationAdmin
# Register your models here.

from artworks.models import Artworks

class ArtworksAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label='Описание',widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label='Описание',widget=CKEditorUploadingWidget())

    class Meta:
        model = Artworks
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("id","name","url")
    list_display_links = ("name",)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ("email", "name")

@admin.register(Artworks)
class ArtworkAdmin(TranslationAdmin):
    list_display = ("name", "url", "draft", "get_image")
    list_filter = ("year","category__name")
    search_fields = ("name", "category__name")
    readonly_fields = ("get_image",)
    inlines = [CommentInline]
    save_on_top = True
    list_editable = ("draft",)
    form = ArtworksAdminForm
    actions = ["unpublish","publish"]

    fieldsets = (
        (None, {
            "fields": (("name",),)
        }),

        (None, {
            "fields": (( "description"),)
        }),

        ("Files", {
            "fields": (("poster","get_image", "quality_image"),)
        }),

        (None, {
            "fields": (("country", "location", "year", ),)
        }),

        (None, {
            "fields": (("artist", "owner"),)
        }),

        (None, {
            "fields": (("category"),)
        }),

        (None, {
            "fields": (("price", "in_sale"),)
        }),

        (None, {
            "fields":(("signature","certificate_of_auth"),)
        }),

        (None, {
            "fields": (("size", "frame"),)
        }),

        ("Options", {
            "classes": ("collapse",),
            "fields": (("tags", "url", "draft"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="55" height="60">')

    def unpublish(self,request,queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish(self,request,queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)



    get_image.short_description = "Изображение"

# class TechnicInline(admin.):
#     model = Technic
#     extra = 1

# class TechnicInline(admin.TabularInline):
#     model = Technic

@admin.register(Artists)
class ArtistAdmin(TranslationAdmin):
    list_display = ( "surname", "name", "patronymic", "get_image")
    readonly_fields = ("get_image",)
    search_fields = ("name", "surname", "description")
    list_filter = ("location",)
    # filter_horizontal = ('technic_favorite',)
    # inlines = [TechnicInline]

    fieldsets = (
        (None, {
            "fields": (("surname","name","patronymic"),)
        }),

        (None, {
            "fields": (("image", "get_image"),)   #show group in page
        }),

        (None, {
            "fields": (("age", "education","description","location"),)
        }),

        (None, {
            "fields": (("technic_favorite",),)
        }),

        ("Contacts", {
            "fields": (("nft_platform", "site"),)
        }),

        (None, {
            "fields": (("facebook", "instagram","phone"),)
        })
    )
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="55" height="60">')

    get_image.short_description = "Изображение"


@admin.register(Technic)
class TechnicAdmin(TranslationAdmin):
    list_display = ("name", "url", )
    search_fields = ("name", "description")
    list_filter = ("name", )


@admin.register(Comment)
class CommentAdmin(TranslationAdmin):
    list_display = ("name","email","artworks")
    search_fields = ("name", "artworks", "email")

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("label_ru", "domain", )
    search_fields = ("label_ru", "domain", )

@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    '''Рейтинг'''
    list_display = ("star","artworks", "ip")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("text", "poster")

# admin.site.register(Category)
# admin.site.register(Artworks)
# admin.site.register(Artists)
# admin.site.register(Technic)
# admin.site.register(Comment)
# admin.site.register(Country)
admin.site.register(Raitingstar)


admin.site.site_title = "Django - GALERY"
admin.site.site_header = "Django - GALERY"


