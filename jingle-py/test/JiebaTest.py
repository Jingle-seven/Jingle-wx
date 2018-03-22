import jieba
import jieba.posseg as psg
import jieba.analyse

txt = open('../resource/jieba-test.txt',encoding='utf8').read()
print(type(txt))

#词
words = list(jieba .cut(txt))
print([x for x in words])

#词和词性
print([x for x in psg .cut(txt)])

#出现最多的几个词(还待去除停止词)
from collections import Counter
c = Counter(words).most_common(20)
print(c)

#关键词
tags = jieba.analyse.extract_tags(txt, topK=10)
print(tags)
