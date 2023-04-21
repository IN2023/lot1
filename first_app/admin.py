from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Goods, Brands


admin.site.register(Brands)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ("id", "img", "brand", "title", "number_of_servings", "price")  # список полів які ми хочемо бачити в адмінці
    search_fields = ("title", )  # за цими полями можна здійснювати пошук

    def img(self, obj):
        return mark_safe(f'<img src={obj.icon.url} width="50" height="60"')


admin.site.register(Goods, GoodsAdmin)
