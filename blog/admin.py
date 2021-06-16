from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")   # mostrar os campos em que vai ser mostrado
    prepopulated_fields = {"slug": ("title",)}  # preencher automaticamente o slug (url description do post)