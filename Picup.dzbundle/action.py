# Dropzone Action Info
# Name: Picup
# Description: upload images to the image hosting site - sm.ms
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
# OptionsNIB: Login


import os
import json
import shutil
import time


class UploadRecord():
    def __init__(self):
        self.upload_time = None
        self.original_path = None
        self.backup_path = None
        self.size = None
        self.url = None
        self.delete = None

    def __str__(self):
        return '  {\n' + 4 * ' ' + '"upload_time": ' ' "' + self.upload_time + '",\n' + \
            4 * ' ' + '"original_path": ' ' "' + self.original_path + '",\n' + \
            4 * ' ' + '"backup_path": ' ' "' + self.backup_path + '",\n' + \
            4 * ' ' + '"size": ' + str(self.size) + ',\n' + \
            4 * ' ' + '"url": ' ' "' + self.url + '",\n' + \
            4 * ' ' + '"delete": ' ' "' + self.delete + '"\n  }\n'


def dragged():
    dz.begin('Start uploading..')
    dz.determinate(True)
    dz.percent(10)
    item = items[-1]

    upload_record = UploadRecord()
    # back up image
    backup_img(item, upload_record)
    # upload to sm
    img_url = upload_to_smms(item, upload_record)
    # log record
    log_to_file(upload_record)
    dz.percent(100)
    # write clipboard
    dz.text(img_url)


def log_to_file(up_rec):
    backup_dir = os.environ['username']
    abs_dir = os.path.expanduser(backup_dir)
    log_filename = os.path.join(abs_dir, 'smms_upload_log.txt')

    with open(log_filename, 'a+') as f:
        # json.dump(up_rec.__dict__, f)
        f.write(up_rec.__str__())
    print('logged into: ', log_filename)


def backup_img(img_path, up_rec):
    # backup_dir = '~/Dropbox/upload_images'
    backup_dir = os.environ['username']
    abs_dir = os.path.expanduser(backup_dir)

    if not os.path.exists(abs_dir):
        os.makedirs(abs_dir)
        print('created image backup dir: ', abs_dir)
    else:
        print('using image backup dir: ', abs_dir)

    try:
        backup_path = shutil.copy(img_path, abs_dir)
    except FileNotFoundError as e:
        print('backup failed! ', e.args[1], ': ', e.filename)
    else:
        up_rec.original_path = img_path
        up_rec.backup_path = backup_path
        print('backup ', img_path, ' to ', abs_dir)


def upload_to_smms(img_path, up_rec):
    UPLOAD_URL = "https://sm.ms/api/upload"
    p = os.popen('/usr/bin/curl -s ' + UPLOAD_URL +
                 ' -F "smfile=@' + img_path + '"')
    upload_resp = p.read()
    p.close()
    upload_result = json.loads(upload_resp)
    if upload_result['code'] != 'success':
        dz.finish('Upload file failed!')
    else:
        img_url = upload_result['data']['url']
        # setting up the record
        up_rec.url = img_url
        up_rec.size = upload_result['data']['size']
        up_rec.delete = upload_result['data']['delete']
        up_rec.upload_time = time.asctime()
        dz.finish('Upload file success')
        return img_url
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
