# coding: utf-8

import time
import requests
import demo.net.EmailSender as messenger


def getRawJson(date="2017-04-28", fromStt="GZQ", toStt="NCQ"):
    ticketUrl = "https://kyfw.12306.cn/otn/leftTicket/query" \
                "?leftTicketDTO.train_date=%s" \
                "&leftTicketDTO.from_station=%s" \
                "&leftTicketDTO.to_station=%s" \
                "&purpose_codes=ADULT" % (date,fromStt,toStt)

    r2 = requests.get(ticketUrl, verify=False)
    return r2.json()

def getTrainsInfo(rawJson):
    trainsInfo = []
    for i in rawJson["data"]:
        trainsInfo.append(i["queryLeftNewDTO"])
    return trainsInfo

def hasTickets(trainInfo):
    resTickets = trainInfo.get("yz_num","--")
    if resTickets == "无" or resTickets == "--":
        return False
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


def watcher():
    trainsIinfo = getTrainsInfo(getRawJson())
    for i in trainsIinfo:
        info = hasTickets(i)
        if info:
            subject = "%s: %s > %s日%s去%s" \
                      % (info["列车"], info["硬座"], info["出发日期"][4:], info["出发时间"], info["到达站"],)
            messenger.sendEmail(subject, str(info))
            print(subject)
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" 无票")

if __name__ == "__main__":
    while(True):
        try:
            watcher()
        except Exception as e:
            print(e)
        time.sleep(60 * 10)








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