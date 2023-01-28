from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published','get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    # Список полей для вывода внутри новости
    fields = ('title', 'category','content','photo','get_photo','views','is_published',)
    #Поля только для чтения
    readonly_fields = ('get_photo','views','created_at', 'updated_at')
    save_on_top = True

    #Метод для получения html кода фото
    def get_photo(self,obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="190" >') #Помечает строку как html код и не экранирует её
        else:
            return 'Фото не установлено'

    get_photo.short_description = 'Миниатюра'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
