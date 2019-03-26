from django.contrib import admin

from .models import BookInfo, HeroInfo
# Register your models here.
# 如果相让某个模型在admin站点中进行展示 需要装展示的模型注册到admin站点

admin.site.register(BookInfo)
admin.site.register(HeroInfo)