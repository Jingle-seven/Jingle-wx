# coding: utf-8

import time
import requests
import EmailSender as messenger

NAN_XIONG = "NCQ"
GUANG_ZHOU = "GZQ"
GUANG_ZHOU_DONG = "GGQ"


def getRawJson(date, fromStt=GUANG_ZHOU, toStt=NAN_XIONG):
    ticketUrl = "https://kyfw.12306.cn/otn/leftTicket/query" \
                "?leftTicketDTO.train_date=%s" \
                "&leftTicketDTO.from_station=%s" \
                "&leftTicketDTO.to_station=%s" \
                "&purpose_codes=ADULT" % (date, fromStt, toStt)

    r2 = requests.get(ticketUrl, verify=False)
    return r2.json()


def getTrainsInfo(rawJson):
    trainsInfo = []
    # 接口返回值变更了,原本是json,现在是字符串,此处会报错
    for i in rawJson["data"]:
        trainsInfo.append(i["queryLeftNewDTO"])
    return trainsInfo


def formatInfo(trainInfo):
    # resTickets = trainInfo.get("yz_num", "--")
    # if resTickets == "无" or resTickets == "--":
    #     return False
    info = {}
    info["出发站"] = trainInfo["from_station_name"]
    info["始发站"] = trainInfo["start_station_name"]
    info["到达站"] = trainInfo["to_station_name"]
    info["无座"] = trainInfo["wz_num"]
    info["硬座"] = trainInfo["yz_num"]
    info["列车"] = trainInfo["station_train_code"]
    info["出发时间"] = trainInfo["start_time"]
    info["到达时间"] = trainInfo["arrive_time"]
    info["历时"] = trainInfo["lishi"]
    info["出发日期"] = trainInfo["start_train_date"]

    return info


def watcher(trainNum=[]):
    trainsInfo = getTrainsInfo(getRawJson(date="2017-05-27"))
    for i in trainsInfo:
        info = formatInfo(i)
        hardSeat = info.get("硬座", "--")
        isTheTrain = len(trainNum)==0 or (len(trainNum)> 0 and ["列车"] in trainNum)
        if isTheTrain and hardSeat != "无" and hardSeat != "--" :
            subject = "%s: %s > %s日%s去%s" \
                      % (info["列车"], info["硬座"], info["出发日期"][4:], info["出发时间"], info["到达站"],)
            messenger.sendEmail(subject, str(info))
            print(subject)
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) + info.get("列车")+" 无硬座票")

if __name__ == "__main__":
    # while (True):
    #     try:
    #         watcher()
    #     except Exception as e:
    #         print("Xz Error: "+str(e))
    watcher()
    time.sleep(60* 10)

    """{  
        "train_no": "240000G14104",          // 列车编号  
        "station_train_code": "G141",        // 车次  
        "start_station_telecode": "VNP",     // 始发站编码  
        "start_station_name": "北京南",      // 始发站名  
        "end_station_telecode": "AOH",       // 终到站编码  
        "end_station_name": "上海虹桥",      // 终到站名  
        "from_station_telecode": "VNP",      // 查询输入经过站编码  
        "from_station_name": "北京南",       // 查询输入经过站名  
        "to_station_telecode": "AOH",        // 查询输入到站编码  
        "to_station_name": "上海虹桥",       // 查询输入到站名  
        "start_time": "14:16",               // 出发时间  
        "arrive_time": "19:47",              // 到站时间  
        "day_difference": "0",               // 花费天数  
        "train_class_name": "",  
        "lishi": "05:31",                    // 历时  
        "canWebBuy": "Y",                    // 是否可以预定  
        "lishiValue": "331",  
        "yp_info": "O055300094M0933000999174800017",  
        "control_train_day": "20301231",  
        "start_train_date": "20140123",  
        "seat_feature": "O3M393",  
        "yp_ex": "O0M090",  
        "train_seat_feature": "3",  
        "seat_types": "OM9",  
        "location_code": "P3",  
        "from_station_no": "01",  
        "to_station_no": "09",  
        "control_day": 19,  
        "sale_time": "1400",                // 出票时间点hhmm  
        "is_support_card": "1",  
        "gg_num": "--",  
        "gr_num": "--",          // 高级软卧座剩余数  
        "qt_num": "--",          // 其他座剩余数  
        "rw_num": "--",          // 软卧座剩余数  
        "rz_num": "--",          // 软座座剩余数  
        "tz_num": "--",          // 特等座剩余数  
        "wz_num": "--",          // 无座座剩余数  
        "yb_num": "--",  
        "yw_num": "--",          // 硬卧座剩余数  
        "yz_num": "--",          // 硬座座剩余数  
        "ze_num": "有",          // 二等座剩余数  
        "zy_num": "有",          // 一等座剩余数  
        "swz_num": "17"          // 商务座剩余数  
    }"""
    
    # 接口返回值变更了,原本是json,现在是字符串
"|预订|630000T1700M|T170|GZQ|SNH|GZQ|NCQ|14:55|18:31|03:36|N|qfbbFTUxvI2%2FyFOG0vJK4RzPanp2kXWj%2BPKpkHd9EXGvuLTcHF3zA2x%2BfeQ%3D|20170527|3|Q7|01|04|0|0||||无|||无||无|无||||10401030|1413"
"%2BzBa2OZh5ZBQm4Y%2B5WTxYJLPZEYRDBY5GlM5d1xNTkCO7GifjjR%2F5A%2FqA8LYzbPC0UlFv1wNr88x%0AaLz1hX%2FM0ejtjmBFu4Bn7csPCUcUeJWEm8fChFS5aoGdr6V4%2B0nAYZWT%2FFMdKJ1plVT8E%2FkFmviB%0AmOQxJ71MJObLhnGdiZ4wHG8kw4zOFLiiTgCXAewnVr2PSWJSURaKwTPEnYJbykWrBp1gRHKXstZc%0AaLdkJOk8qN%2B2RNlazA%3D%3D" \
"|预订|65000K166601|K1666|GGQ|GZG|GGQ|NCQ|15:22|19:49|04:27|Y|tY2NhFwlaRZ417DkAX71sBKsJs4nfuEnMvqlG5BNgBRquWlKsF5Ze%2F9jVRs%3D|20170527|3|Q9|01|07|0|0||||无|||有||有|有||||10401030|1413"