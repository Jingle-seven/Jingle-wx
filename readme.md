[<img src="https://img.shields.io/travis/Jingle-seven/jingle-wx.svg"/>](https://travis-ci.org/Jingle-seven/jingle-wx)

# How to start
python3 and django should be installed in your server  
cd . / and run commands to init database and  start application
- python3 manage.py migrate
- python3 manage.py runserver 0.0.0.0:8000  

# Note  
It is better run in pycharm, and make ./jingle as source root  
and then run small py files

# Some script
#### what whl file the pip support 
import pip  
print(pip.pep425tags.get_supported())  
#### is your py 32bit or 64bit
import platform  
print(platform.architecture())