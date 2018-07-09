import os,json,time

def execCodeFromJson(jsonPath):
    # print(os.getcwd() )
    # print(os.path.abspath('../'))
    hot_code = open(jsonPath).read()
    print(hot_code)
    hot = json.loads(hot_code)
    context = dict()
    for k,v in hot.items():
        # 从json文件中加载代码
        exec(v,context)
        # 从context中用json中的函数名调用函数
        print(context[k](2))

while True:
    execCodeFromJson("../resource/hot_code.json")
    time.sleep(10)