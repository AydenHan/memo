# =============================================================================
#      FileName: dataIO.py
#          Desc: 实现数据保存与交互
# =============================================================================
import os
import json
import css

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
# '''
# @note: read last memo id
# '''
# def readLastMemoId(data):
#     if not os.path.exists(css.configPath):
#         update_config(data)
#     with open(css.configPath, 'r', encoding='utf-8') as cfg:
#         info = json.load(cfg)
#         num = info['memo_num']
#         lastId = info['memo_data'][num-1]['id']
#
#     return lastId
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
