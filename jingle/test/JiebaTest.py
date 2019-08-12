import jieba
import jieba.posseg as psg
import jieba.analyse
from collections import Counter

fileName = "多情剑客无情剑"
txt = open('../resource/jieba/%s.txt'%fileName,encoding='utf8').read()

#词
words = list(jieba .cut(txt))
# print([x for x in words])

#词和词性
# print([x for x in psg .cut(txt)])

#出现最多的几个词(还待去除停止词)
c = Counter(words).most_common(20)
print(c)

# 自定义停止词和语料库
jieba.analyse.set_stop_words("../resource/jieba/stop_words.txt")
# jieba.analyse.set_idf_path("../extra_dict/idf.txt.big")
#关键词
tags = jieba.analyse.extract_tags(txt, topK=50 , withWeight=True)
for x in tags:
    print(x)
