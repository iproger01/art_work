from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name","url")
    list_display_links = ("name",)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ("email", "name")

@admin.register(Artworks)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "url", "draft", "get_image")
    list_filter = ("category", "year")
    search_fields = ("name", "category__name")
    readonly_fields = ("get_image",)
    inlines = [CommentInline]
    save_on_top = True
    list_editable = ("draft",)

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
            "fields": (("category", "technic_paint"),)
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

    get_image.short_description = "Изображение"

@admin.register(Artists)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ( "surname", "name", "patronymic", "technic_favorite", "get_image")
    readonly_fields = ("get_image",)
    search_fields = ("name", "surname", "description")
    list_filter = ("technic_favorite","location")
    fieldsets = (
        (None, {
            "fields": (("surname","name","patronymic"),)
        }),

        (None, {
            "fields": (("image", "get_image"),)  #show group in page
        }),

        (None, {
            "fields": (("age", "education","description"),)
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
class TechnicAdmin(admin.ModelAdmin):
    list_display = ("name", "url", )
    search_fields = ("name", "description")
    list_filter = ("name", )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name","email","artworks")
    search_fields = ("name", "artworks", "email")

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("label_ru", "domain", )
    search_fields = ("label_ru", "domain", )


# admin.site.register(Category)
# admin.site.register(Artworks)
# admin.site.register(Artists)
# admin.site.register(Technic)
# admin.site.register(Comment)
# admin.site.register(Country)
admin.site.register(Raitingstar)
admin.site.register(Raiting)

admin.site.site_title = "Django - GALERY"
admin.site.site_header = "Django - GALERY"


