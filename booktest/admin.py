from django.contrib import admin

from .models import BookInfo, HeroInfo
# Register your models here.
# 如果相让某个模型在admin站点中进行展示 需要装展示的模型注册到admin站点

# 如果想要调整admin站点样式需要定义模型站点管理类

class BookInfoAdmin(admin.ModelAdmin):
    """调整书籍数据在站点界面显示"""

    """调整列表界面样式"""
    actions_on_bottom = True  # 设置列表界面底部是否显示操作选项
    actions_on_top = False

    list_per_page = 2  # 默认每页只显示两条数据

    # list_display = ('bread') # 在Django中如果可以赋值为元组都可以给它列表
    list_display = ['id', 'btitle', 'bread', 'bcomment', 'bpub_date_format'] # 控制列表界面显示那些列 [元素可以是模型中的方法名, 字段名]



@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    """调整英雄数据在站点展示"""

    list_display = ['id', 'hname', 'hcomment', 'hgender', 'hbook', 'read']


admin.site.register(BookInfo, BookInfoAdmin)  # 将模型站点管理类和相应模型关联到一起
# admin.site.register(HeroInfo, HeroInfoAdmin)