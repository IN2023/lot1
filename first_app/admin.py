from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Goods, Brands


class GoodsAdmin(admin.ModelAdmin):
    list_display = ("id", "img", "brand", "title", "number_of_servings", "price")  # список полів які ми хочемо бачити в адмінці
    search_fields = ("title", )  # за цими полями можна здійснювати пошук в адмінці

    def img(self, obj):
        return mark_safe(f'<img src={obj.icon.url} width="50" height="90"')


admin.site.register(Brands)
admin.site.register(Goods, GoodsAdmin)
