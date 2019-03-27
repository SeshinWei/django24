from rest_framework import serializersfrom .models import BookInfo# class BookInfoSerializer(serializers.ModelSerializer):#     """定义序列化器"""#     class Meta:#         model = BookInfo  # 指定序列化从那个模型映射字段#         fields = '__all__'  # 映射那些字段class HeroInfoSerializer(serializers.Serializer):    """英雄数据序列化器"""    GENDER_CHOICES = (        (0, 'female'),        (1, 'male')    )    id = serializers.IntegerField(label='ID', read_only=True)    hname = serializers.CharField(label='名字', max_length=20)    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)    # hbook = serializers.PrimaryKeyRelatedField(label='书籍', read_only=True)  # 默认是将关联模型的id序列化    # hbook = serializers.StringRelatedField(label='书籍', read_only=True)  # 默认是将关联模型的__str__方法返回值序列化出来    # hbook = BookInfoSerializer()  # 关联模型对象的序列化器中所有字段序列化出来    # hbook = serializers.PrimaryKeyRelatedField(label='书籍', queryset=BookInfo.objects.all())class BookInfoSerializer(serializers.Serializer):    """书籍的序列化器"""    id = serializers.IntegerField(label='ID', read_only=True)    btitle = serializers.CharField(max_length=20, label='名称', required=True)    bpub_date = serializers.DateField(label='发布日期')    bread = serializers.IntegerField(label='阅读量', required=False)    bcomment = serializers.IntegerField(label='评论量', required=False)    is_delete = serializers.BooleanField(label='逻辑删除', required=False)    # hello = serializers.CharField()    # heroinfo_set = serializers.PrimaryKeyRelatedField(many=True)    # heroinfo_set = HeroInfoSerializer(many=True)  # 如果一里面关联序列化多时, 需要多指定many=True    # def validate_btitle(self, value):    #     # validate_<field_name>    #     # 对序列化器中单个字段追加额外的校验逻辑    #     # 当前要进行校验的单个字段的值    #     if 'django' not in value.lower():    #         raise serializers.ValidationError("图书不是关于Django的")    #    #     return value    # def validate(self, attrs):    #     """对多个字段进行联合校验    #     attrs: 里面是前端 传入过来的所有数据 字典    #     """    #     # attrs['hello'] = 'world'    #     return attrs    def create(self, validated_data):        # validated_data 得来的是反序列化校验后的大字典数据        """当调用序列化器的save方法时, 如果当初创建序列化器对象是没有给instance传参数"""        # BookInfo.objects.create(**{'btitle': '三国django', 'bpub_date': '1991-11-11'})        book = BookInfo.objects.create(**validated_data)        return book        # BookInfo.objects.create(        #     btitle='三国django',        #     bpub_date='1991-11-11'        # )    def update(self, instance, validated_data):        """如果创建序列化器时给instance传了参数,再调用序列化器的save方法是实际会调用当前的update        instance: 要修改的模型对象 创建序列化器是 BookInfoSerializer(instance=book, data=data)        """        # request = self.context['request']        instance.btitle = validated_data.get('btitle')        instance.bpub_date = validated_data.get('bpub_date')        instance.save()        return instance"""book 模型中有7个属性book.aa = 10{8个key: value}BookInfoSerializer(instace, data)如果直给instace 形参传递参数表示做序列化serializer = BookInfoSerializer(instace = book)serializer.data  获取到序列化后的数据"""