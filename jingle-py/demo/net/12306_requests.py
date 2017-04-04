# coding: utf-8
# author: huym

import json
import requests


def getTickets(date="2017-04-28"):
    ticketUrl = "https://kyfw.12306.cn/otn/leftTicket/queryX" \
                "?leftTicketDTO.train_date=%s" \
                "&leftTicketDTO.from_station=GZQ" \
                "&leftTicketDTO.to_station=NCQ" \
                "&purpose_codes=ADULT" % date
    # print(r2.content.decode("utf-8"))

    r = requests.get(ticketUrl, verify=False)
    print(r.json())
if __name__ == "__main__":
    getTickets()