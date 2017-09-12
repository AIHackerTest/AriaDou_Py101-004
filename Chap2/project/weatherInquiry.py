# -*- coding: utf-8 -*-
import requests

history_weather = []

def printHelp():
    print(
    '''
    输入城市名，返回该城市的天气数据；
    输入h或help，打印帮助文档；
    输入history，打印查询历史；
    输入quit，退出程序。
    '''
    )

def printResult(result):
    print(result['city'] + "的天气为" + result['cond_txt'] + "，风向为" + result['wind_dir'] + "，温度为" + result['tmp'] + "摄氏度。")
    print("更新时间：" + result['update'])

def inquiryWeather(city):
    key = "bbd1ac758b5d464e8d1d63a58ef015f9"
    url = 'https://free-api.heweather.com/v5/now?city=' + city + '&key=' + key
    weather = requests.get(url)
    weather_info = eval(weather.text)['HeWeather5'][0]
    result = {}
    if weather_info['status'] != 'ok':
        print("没有该城市信息")
    else:
        result['city'] = city
        result['cond_txt'] = weather_info['now']['cond']['txt']
        result['wind_dir'] = weather_info['now']['wind']['dir']
        result['tmp'] = weather_info['now']['tmp']
        result['update'] = weather_info['basic']['update']['utc']
        printResult(result)
        history_weather.append(result)

def printHistory():
    for i in history_weather:
        printResult(i)

def checkCommand():
    command = input("请输入指令或城市名：")
    if command == "help" or command == "h":
        printHelp()
    elif command == "history":
        printHistory()
    elif command == "quit":
        printHistory()
        return 0
    else:
        inquiryWeather(command)
    return checkCommand()

checkCommand()
