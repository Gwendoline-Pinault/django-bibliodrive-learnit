from django.contrib import admin
from backoffice.models import Author, Publisher, Title, Reservation
from django.utils.html import format_html

admin.site.register(Author)
admin.site.register(Publisher)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;">', obj.image.url)
        return "Aucune image"
    image_preview.short_description = "Aperçu de l'image"

    search_fields = ['title', 'authors__author']

admin.site.register(Title, TitleAdmin)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'return_date', 'user')

    search_fields = ['return_date', 'user__username']

admin.site.register(Reservation, ReservationAdmin)
