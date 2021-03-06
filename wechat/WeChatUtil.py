# author: HuYong
# coding=utf-8
import json
from math import *
import requests


def calcDistance(Lat_A, Lng_A, Lat_B, Lng_B):
    ra = 6378.140  # 赤道半径 (km)
    rb = 6356.755  # 极半径 (km)
    flatten = (ra - rb) / ra  # 地球扁率
    rad_lat_A = radians(Lat_A)
    rad_lng_A = radians(Lng_A)
    rad_lat_B = radians(Lat_B)
    rad_lng_B = radians(Lng_B)
    pA = atan(rb / ra * tan(rad_lat_A))
    pB = atan(rb / ra * tan(rad_lat_B))
    xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B))
    c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2
    c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (xx + dr)
    return float('%.4f' % distance) * 1000


def GetAddress(longitude, latitude):
    BaseUrl = "http://restapi.amap.com/v3/geocode/regeo?output=json&location=LON,LAT&key=KEY&radius=100&extensions=all&roadlevel=0&poitype=楼"
    URL = BaseUrl.replace("LON", str(longitude)).replace("LAT", str(latitude)).replace("KEY","9c9aaf8f45b7d23a26274866b578a2a9")
    response = requests.get(URL)
    s = json.loads(response.text)
    return s["regeocode"]["formatted_address"]

#print GetAddress(118.721893,32.141903)
