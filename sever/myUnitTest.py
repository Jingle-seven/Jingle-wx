import os
import random

import django
from django.db.models import Count, Avg

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sever.settings")
django.setup()

import unittest
import sever.models
from sever.models import Article,Person


# It said that django.test.TestCase should be used here ,but I run tests normally with unittest.TestCase
class MyTestCase(unittest.TestCase):
    def testGetAll(self):
        res1 = Article.objects.all()
        # 倒序排列
        res2 = Article.objects.all().order_by('-title')
        # 链式过滤
        res3 = Article.objects.filter(title__icontains="i").exclude(tag="Tom")
        # offset limit (show sql)
        res4 = Article.objects.all()[2:3].query
        # as tuple
        res5 = Article.objects.all().values_list('tag', 'title')
        # as map
        res6 = Article.objects.all().values('tag', 'title')
        # count
        res7 = Article.objects.all().values('tag').annotate(count=Count('tag')).values('tag', 'count')
        # avg
        res8 = Person.objects.all().values('name').annotate(fuckTheAvg=Avg("age")).values('name', 'fuckTheAvg')
        # 需要哪个字段取哪个字段
        res9 = Article.objects.all().values("tag")
        print(res9)

    @unittest.skip("must skipping\n")
    def testAdd(self):
        # create数据库增加操作
        author = ["Tom", "Nancy", "Jack","Nike","Lucy","Iric"]
        title = ["I have a dream","you have a Dream","We have a Dream"]
        for i in range(1,10):
            r1 = random.randint(0, 5)
            r2 = random.randint(0, 2)
            # res1 = Article.objects.create(title = title[r1], tag = author[r2], content = '这是一个简单的文章')
            Person(id=i,name=author[r1],age=random.randint(13, 80)).save()
        pass

    @unittest.skip("must skipping\n")
    def testUpdate(self):
        article = Article.objects.get(id=1)
        article.title = "kill me inside"
        # article.save()

    @unittest.skip("must skipping\n")
    def testDelete(self):
        # filter ignore case
        a2 = Article.objects.filter(title__icontains="world")
        print("before delete: " + str(a2))
        # a2[0].delete()
        a2 = Article.objects.filter(title__icontains="world")
        print("after delete: " + str(a2))
