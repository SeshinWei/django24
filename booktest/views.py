from django.shortcuts import render

# Create your views here.


from booktest.models import BookInfo, HeroInfo
from django.db.models import F, Q, Sum


"""演示数据新增  save  create"""
# book = BookInfo()
# book.btitle = '小三国'
# book.bpub_date = '1991-11-11'
#
# book.save()


# book = BookInfo(
#     btitle='大三国',
#     bpub_date='1990-11-11'
# )
# book.save()
#
# hero = HeroInfo(
#     hname='张三',
#     hbook=book,  # 外键=关联的模型对象
#     # hbook_id=book.id   # 外键_id=关联的模型对象.id
# )
# hero.save()

# BookInfo.objects.create(
#     btitle='西游记',
#     bpub_date='2001-11-11'
# )

"""演示基本查询  get all  count"""

# try:
#     BookInfo.objects.get(id=10)
# except BookInfo.DoesNotExist:
#     print('查询失败')

# book = BookInfo.objects.get(id=1)
# BookInfo.objects.all()

# BookInfo.objects.all().count()

"""演示过滤查询  filter exclude get
条件语法格式: 字段名__运算符=值
"""

# BookInfo.objects.get(id=1)  # 返回单一模型对象,查不到会报错
# BookInfo.objects.filter(id__exact=1)  # filter查询结果都是QuerySet类型,查询不到也不会报错(可以有任意个)

# BookInfo.objects.filter(btitle__contains='湖')

# BookInfo.objects.filter(btitle__endswith='部')

# BookInfo.objects.filter(btitle__isnull=False)

# BookInfo.objects.filter(id__in=[2, 4])
# > gt
# < lt
# >= gte
# <= lte

# BookInfo.objects.filter(id__gt=2)
# BookInfo.objects.exclude(id=3)

# BookInfo.objects.filter(bpub_date__year='1980')

# BookInfo.objects.filter(bpub_date__gt='1990-1-1')

# F 对象:两个字段之间的比较查询
# BookInfo.objects.filter(bread__gt=20)
# BookInfo.objects.filter(bread__gt=F('bcomment'))
# BookInfo.objects.filter(bread__gt=F('bcomment') * 2)


# Q: 逻辑与  逻辑或  逻辑非  and or not

# BookInfo.objects.filter(bread__gt=20, id__lt=3)  # 查询同时两个条件都满足的 (逻辑与 and)
# BookInfo.objects.filter(Q(bread__gt=20), Q(id__lt=3))  # 逻辑与 and  查询同时两个条件都满足的

# BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))  # 逻辑或 or  两个条件满足其中某一个的都查出来

# BookInfo.objects.filter(~Q(id=3))  # 逻辑非 表示查询满足条件以外 和exclude 一样
# BookInfo.objects.filter(Q(id=3))  # 查询id为3的

# BookInfo.objects.aggregate(Sum('bread'))  # {bread__max : xx}

# BookInfo.objects.all().order_by('bread')  # 默认升序
# BookInfo.objects.all().order_by('-bread')  # 默认升序




# 关联查询 ()
"""如果filter中的条件不是当前的模型类字段 而是关联的模型字段做条件时,需要在字段名前面多加 模型名"""
# 一查多/多查一

# 多查一 (一.objects.filter(多的模型名小写__多的那方模型属性=值))
# BookInfo.objects.filter(heroinfo__hname='郭靖')
# BookInfo.objects.filter(heroinfo__hname__contains='靖')

# 一查多 (多.objects.filter(外键__一的属性=值)
# HeroInfo.objects.filter(bookinfo__id__gt=1)
# HeroInfo.objects.filter(hbook__id=1)


# 多查一 ( 先把多查出来, 然后再利用多里面的外键 查到一)
# hero = HeroInfo.objects.get(hname='郭靖')
# book = hero.hbook  # 如果有外键直接当前模型对象.外键 代表获取外键模型对象

# 一查多 (先把一查出来, 然后得用一.多的那方模型名小写_set 查到多)
book = BookInfo.objects.get(id=1)
book.heroinfo_set.all()  # 如果当前没有外键的一方  应该是当前模型对象.多的一方模型旬小写_set
