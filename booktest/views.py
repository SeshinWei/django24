from django.shortcuts import render

# Create your views here.


from booktest.models import BookInfo, HeroInfo


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