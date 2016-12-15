import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()

import unittest
import blog.models
from blog.models import Article


# It said that django.test.TestCase should be used here ,but I run tests normally with unittest.TestCase
class MyTestCase(unittest.TestCase):
    def testGetAll(self):
        res3 = Article.objects.all()
        print(res3)

    def testAdd(self):
        # create数据库增加操作
        # res1 = Article.objects.create(title = 'Hello World', category = 'Python', content = '我们来做一个简单的数据库增加操作')
        # res2 = blog.models.Person.objects.create(name="ok",age=13)
        pass

    def testUpdate(self):
        article = Article.objects.get(id=1)
        article.title = "kill me inside"
        # article.save()

    def testDelete(self):
        # filter ignore case
        a2 = Article.objects.filter(title__icontains="world")
        print("before delete: " + str(a2))
        a2[0].delete()
        a2 = Article.objects.filter(title__icontains="world")
        print("after delete: " + str(a2))
