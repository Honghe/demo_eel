# -*- coding:utf8 -*-

import eel
from multiprocessing import Pool, freeze_support
import time

print('import')


@eel.expose  # Expose this function to Javascript
def Open():
    url_list = [1]
    pool.map_async(parsing, url_list)
    # for text in ret:
    #     print(text)


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


if __name__ == '__main__':
    # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.freeze_support
    freeze_support()
    import bottle_websocket
    # Set web files folder and optionally specify which file types to check for eel.expose()
    pool = Pool(processes=2)
    eel.init('web', allowed_extensions=['.js', '.html'])
    eel.start('index.html', close_callback=close_callback,  size=(800, 600))
