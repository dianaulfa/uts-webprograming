from django.contrib import admin
from .models import Kategori
from .models import Berita

# Register your models here.
class BeritaAdmin(admin.ModelAdmin):
    list_display = ("kategori","judul", "isi_berita",)



admin.site.register(Berita, BeritaAdmin)
admin.site.register(Kategori)


