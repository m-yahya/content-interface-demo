import os

import toml

snap_userdata = os.environ['SNAP_USER_DATA']


def get_vars():
    if os.path.isfile(snap_userdata + '/config.toml'):

        f = toml.load(snap_userdata + '/config.toml')
        items = f.items()
        print(items)
        
    else:
        print('file not found')