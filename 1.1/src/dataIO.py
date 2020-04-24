# =============================================================================
#      FileName: dataIO.py
#          Desc: 实现数据保存与交互
# =============================================================================
import os
import json
import css

#----------数据文件-------------
'''
@note: create statistics file
'''
def update_statistics(data, first_date):
    with open(css.statisticsPath, 'w', encoding='utf-8') as sta:
        data[first_date] = data.pop('date')
        json.dump(data, sta)

'''
@note: read statistics file
'''
def readStatistics(data, first_date):
    if not os.path.exists(css.statisticsPath):
        update_statistics(data, first_date)
    with open(css.statisticsPath, 'r', encoding='utf-8') as sta:
        info = json.load(sta)
    return info

'''
@note: read finishing rate at appointed date
'''
def readFinishRate(date):
    with open(css.statisticsPath, 'r', encoding='utf-8') as sta:
        info = json.load(sta)
    finish = len(info[date]['finished'])
    unfinish = len(info[date]['unfinished'])
    rate = finish / (unfinish + finish)
    rateList = []
    rateList.append(finish)
    rateList.append(unfinish)
    rateList.append(rate)
    return rateList

'''
@note: write statistics file
'''
def writeStatistics(data):
    with open(css.statisticsPath, 'w', encoding='utf-8') as sta:
        json.dump(data, sta)

#----------配置文件-------------
'''
@note: create config file
'''
def update_config(data):
    with open(css.configPath, 'w', encoding='utf-8') as cfg:
        json.dump(data, cfg)

'''
@note: read config file
'''
def read(data):
    if not os.path.exists(css.configPath):
        update_config(data)
    with open(css.configPath, 'r', encoding='utf-8') as cfg:
        info = json.load(cfg)
    return info

'''
@note: read memo settings
'''
def readMemoSettings(data):
    if not os.path.exists(css.configPath):
        update_config(data)
    with open(css.configPath, 'r', encoding='utf-8') as cfg:
        info = json.load(cfg)
        set_data = info['set_data']
    return set_data

'''
@note: read memo Ui_settings
'''
def readMemoUi(data):
    if not os.path.exists(css.configPath):
        update_config(data)
    with open(css.configPath, 'r', encoding='utf-8') as cfg:
        info = json.load(cfg)
        ui_data = info['ui_data']
    return ui_data

'''
@note: read memo content
'''
def readMemoContent(data):
    memo_content = []
    if not os.path.exists(css.configPath):
        update_config(data)
    with open(css.configPath, 'r', encoding='utf-8') as cfg:
        info = json.load(cfg)
        memo_data = info['memo_data']
    for each in memo_data:
        memo_content.append(each['content'])

    return memo_content

'''
@note: read memo performance
'''
def readMemoPerformance(data):
    memo_done = []
    if not os.path.exists(css.configPath):
        update_config(data)
    with open(css.configPath, 'r', encoding='utf-8') as cfg:
        info = json.load(cfg)
        memo_data = info['memo_data']
    for each in memo_data:
        memo_done.append(each['if_done'])

    return memo_done

'''
@note: write config file
'''
def write(data):
    with open(css.configPath, 'w', encoding='utf-8') as cfg:
        json.dump(data, cfg)

'''
@note: update config file
'''
def addNewMemoInfo(data):
    data['memo_num'] += 1
    singleMemo = {
        'id': data['memo_num'],
        'content': 'It is empty!',
        'set_date': '',
        'delete_date': '',
        'if_done': {
        }
    }
    data['memo_data'].append(singleMemo)

    return data
