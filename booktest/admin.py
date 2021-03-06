from django.contrib import admin

from .models import BookInfo, HeroInfo
# Register your models here.
# 如果相让某个模型在admin站点中进行展示 需要装展示的模型注册到admin站点

# 如果想要调整admin站点样式需要定义模型站点管理类
class HeroInfoStack(admin.TabularInline):
    model = HeroInfo
    extra = 2  # 默认显示几个空格子


class BookInfoAdmin(admin.ModelAdmin):
    """调整书籍数据在站点界面显示"""

    """调整列表界面样式"""
    actions_on_bottom = True  # 设置列表界面底部是否显示操作选项
    actions_on_top = False

    list_per_page = 2  # 默认每页只显示两条数据

    # list_display = ('bread') # 在Django中如果可以赋值为元组都可以给它列表
    list_display = ['id', 'btitle', 'bread', 'bcomment', 'bpub_date_format'] # 控制列表界面显示那些列 [元素可以是模型中的方法名, 字段名]

    """调整编辑界面样式"""
    # fields = ['btitle', 'bpub_date']  # 设置编辑页面能编辑的字段

    # 设置编辑字段分组展示
    fieldsets = [
        ['基础组', {'fields': ['btitle', 'bpub_date', 'image']}],
        ['高级组', {
                    'fields': ['bread', 'bcomment'],
                    'classes': ['collapse']  # 设置组默认主折叠样式
                 }]
    ]

    inlines = [HeroInfoStack]  # 在书箱编辑页面关联展示 英雄数据




@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    """调整英雄数据在站点展示"""

    """调整列表界面样式"""
    list_display = ['id', 'hname', 'hcomment', 'hgender', 'hbook', 'read']

    # 设置右侧过滤栏
    list_filter = ['hbook', 'hgender']

    # 设置搜索框
    search_fields = ['hname', 'id']


admin.site.register(BookInfo, BookInfoAdmin)  # 将模型站点管理类和相应模型关联到一起
# admin.site.register(HeroInfo, HeroInfoAdmin)


# 以下三个设置可以放在任意子应用的admin中 只用写一次就行了
admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '欢迎使用传智书城MIS'