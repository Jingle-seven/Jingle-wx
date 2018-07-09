# 将book表的数据简单处理存到book_copy表
# 只允许绝对导入,同级目录下文件相对导入报错: ValueError: attempted relative import beyond top-level package
from jingle.util.MysqlConnector import *

finder = Finder(section='work_1')
inserter = Inserter(section="work_1")
books = finder.find("select * from book order by date asc")
# books = finder.findAll('book')
nameToBook = dict()
bookList = []
for book in books:
    # print(book)
    key = book['user_name']+book['name']
    theBook = nameToBook.get(key,None)
    if theBook is None:
        nameToBook[key] = book
    else:
        theBook['return_date'] = book['date']
for book in nameToBook.values():
    bookList.append((book['id'],book['name'],book['date'],book.get('return_date',None),
                     book['user_id'],book['user_name']))
print(bookList)
inserter.insert('book_copy',bookList)
