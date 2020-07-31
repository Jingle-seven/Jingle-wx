# 在内存中保存的str类型是unicode编码, 可以在指定编码后转换成特定编码的bytes字节流
# 实际上字符串的编码解码就是从unicode编码和其他编码相互转换的过程,无论是读写文件还是转bytes
# bytes中保存的是特定编码的字元(即某个字符在特定编码中的序号),包含多个byte,类似java中的byte[]封装一下
# byte即字节,与java中的byte长度一样为8比特(bits),至于为什么是8bits就要从计算机的初生时代说起
# 不过py中并没有byte类型,py包含三种不可变类型Number,String,Tuple,三种可变类型List,Dictionary,Set
# 其中Number类型包括 int,float,bool,complex（复数）

print('a'.encode('utf-8'))# utf-8保存英文字符和数字等ASCII字符只需一个字节
print('可'.encode('utf-8'))# utf-8保存日常非ASCII字符需三字节
print('a'.encode('gbk'))# gbk保存英文字符和数字等ASCII字符只需一个字节
print('可'.encode('gbk'))# utf-8保存汉字需两字节
# utf-16(在65535字元以下可以等同于unicode,UCS-2)保存英文字符和数字等ASCII字符需两个字节.
# 这里出现了三个字节,第一个字节应该是用来标识大小端
print('a'.encode('utf-16'))
print('可'.encode('utf-16'))# utf-16保存日常非ASCII字符需两字节或四字节
a = 'a\n'
print(repr(a),str(a))