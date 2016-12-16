import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()

import blog.models
from blog.models import Article

# create数据库增加操作
# res1 = Article.objects.create(title = 'Hello World', category = 'Python', content = '我们来做一个简单的数据库增加操作')
# res2 = blog.models.Person.objects.create(name="ok",age=13)

# update
article = Article.objects.get(id=1)
article.title = "kill me inside"
# article.save()

# filter ignore case
a2 = Article.objects.filter(title__icontains="world")
print(a2)
# a2[0].delete()

res3 = Article.objects.all()
print(res3)
