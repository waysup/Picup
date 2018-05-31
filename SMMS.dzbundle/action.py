# Dropzone Action Info
# Name: SMMS
# Description: upload markdown images to sm.ms image hosting
# Handles: Files
# Creator: waysup
# URL: https://qnmlgb.app
# Events: Clicked, Dragged
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: Yes
# Version: 1.0
# MinDropzoneVersion: 3.5
# PythonPath: /usr/local/bin/python3


import os
import json


def dragged():
    dz.begin('Start uploading..')
    dz.determinate(True)
    dz.percent(10)
    item = items[-1]
    upload_to_smms(item)


def upload_to_smms(img_path):
    UPLOAD_URL = "https://sm.ms/api/upload"
    p = os.popen('/usr/bin/curl -s ' + UPLOAD_URL +
                 ' -F "smfile=@' + img_path + '"')
    upload_resp = p.read()
    p.close()
    upload_result = json.loads(upload_resp)
    dz.percent(100)
    if upload_result['code'] != 'success':
        dz.finish('Upload file failed!')
    else:
        img_url = upload_result['data']['url']
        dz.finish('Upload file success')
        dz.text(img_url)
        # dz.text('!' + '[' + os.path.basename(img_path) + '](' + img_url + ')')


def clicked():
    clear_upload_history()
    dz.url(False)


def clear_upload_history():
    CLEAR_URL = 'https://sm.ms/api/clear'
    p = os.popen('/usr/bin/curl -s ' + CLEAR_URL)
    clear_resp = p.read()
    p.close()
    clear_result = json.loads(clear_resp)
    # print(clear_result)
    if clear_result['code'] == 'success':
        dz.finish(clear_result['msg'])
    else:
        dz.finish('Clear file failed!')
