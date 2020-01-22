class village:
    def __init__(self, id,name,count = 0,obj = None,remark=''):
        self.id = id
        self.name = name
        self.count = count
        self.obj = obj
        self.remark = remark
    def __repr__(self):
        return '{%s,%s,%s}'%(self.id,self.name,self.count)
villages = [
    village('4402820401','赤岭',0),
    village('4402820402','弱过',0),
    village('4402820403','大部',0),
    village('4402820404','云西',0),
    village('4402820405','大坪',0),
    village('4402820406','沙头',0),
    village('4402820407','下湖',0),
    village('4402820408','河村',0),
    village('4402820409','下楼',0),
    village('4402820410','石庄',0),
    village('4402820411','群星',0),
    village('4402820412','泷头',0),
    village('4402820413','水口',0),
    village('4402820414','社区',0)
]
nameToVillage = {}
for v in villages:
    nameToVillage[v.name] = v

class ColProp:
    def __init__(self, head,len = 5,obj = None,remark='',**argDict):
        self.head = head
        self.len = len
        self.obj = obj
        self.remark = remark
        for k,v in argDict.items():
            setattr(self,k,v)