import hashlib

# sha1和md5被破解过.sha256是sha2其中之一,存在理论上的可破解性.
# 不过这三者日常使用还是可以的,md5性能最好安全性在其中也最差
md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()
sha3_512 = hashlib.sha3_256()
encs = [md5,sha1,sha256,sha3_512]
for enc in encs:
    #  m.update(a); m.update(b) is equivalent to m.update(a+b).
    # enc.update('ok') # Update the hash object with the bytes-like object
    enc.update('fine'.encode('utf-8'))
    print(enc.hexdigest(),enc.digest())