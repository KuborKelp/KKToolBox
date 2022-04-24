import os

old_path = './data/schdeule/old/'
new_path = './data/schdeule/new/'


def path_check():
    if not os.path.exists(old_path):
        os.makedirs(old_path)
    if not os.path.exists(new_path):
        os.makedirs(new_path)


def data_get():
    path_check()
    old = os.listdir(old_path)
    new = os.listdir(new_path)
    if not old:
        old = False
    else:
        old = [open(old_path + i, encoding='utf-8').read() for i in old]
    if not new:
        new = False
    else:
        new = [open(new_path + i, encoding='utf-8').read() for i in new]

    return {'old': old, 'new': new}
