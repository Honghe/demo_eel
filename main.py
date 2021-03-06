# -*- coding:utf8 -*-
import os
from tkinter import Tk, filedialog

import eel
from multiprocessing import Pool, freeze_support
import time

print('import')


@eel.expose  # Expose this function to Javascript
def Open():
    url_list = [1]
    pool.map_async(parsing, url_list)


@eel.expose
def btn_get_folder():
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    folder = filedialog.askdirectory()
    return folder


@eel.expose
def btn_get_file():
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("video files", "*.mp4"), ("all files", "*.*")))
    return root.filename


@eel.expose
def process_file(filepath, prologue, epilogue):
    print('process_file')
    time.sleep(5)
    print('process end')
    return 'OK'


def parsing(url):
    print(f'parsing {url}')
    print(f'sleep')
    while True:
        print(f'subprocess {url}')
        time.sleep(1)
    print(f'out sleep')
    return url


def close_callback(closed_page_path, websockets):
    print(__name__)
    print(f'closed_page_path {closed_page_path}')
    print(f'websockets {websockets}', flush=True)
    pool.close()
    pool.terminate()
    pool.join()

    # exit. copy from eel._websocket_close
    from eel import gvt
    if eel._shutdown:
        eel._shutdown.kill()
    eel._shutdown = gvt.spawn_later(1.0, eel._detect_shutdown)


if __name__ == '__main__':
    # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.freeze_support
    freeze_support()
    import bottle_websocket

    # Set web files folder and optionally specify which file types to check for eel.expose()
    pool = Pool(processes=2)
    eel.init('web', allowed_extensions=['.js', '.html'])
    eel.start('index.html', close_callback=close_callback, size=(800, 600))
