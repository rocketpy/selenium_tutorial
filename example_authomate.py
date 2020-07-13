import csv
from os.path import isfile
from time import sleep, ctime
from collections import namedtuple
from threading import Thread
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


BANDCAMP_FRONTPAGE = 'https://bandcamp.com/'
 
class BandLeader():
    def __init__(self):
        # initialize a browser
        opts = Options()
        opts.set_headless()     
        self.browser = Firefox(options=opts)
        self.browser.get(BANDCAMP_FRONTPAGE)
 
        # tracklist
        self._current_track_number = 1
        self.track_list = []
        self.tracks()
 
    def tracks(self):
        sleep(1)
 
        # Получаем хранилище для списка видимых треков.
        discover_section = self.browser.find_element_by_class_name('discover-results')
        left_x = discover_section.location['x']
        right_x = left_x + discover_section.size['width']
 
        # Фильтруем объекты в списке, чтобы получить только те, которые мы можем включать.
        discover_items = self.browser.find_elements_by_class_name('discover-item')
        self.track_list = [t for t in discover_items
                           if t.location['x'] >= left_x and t.location['x'] < right_x]
 
        # Вывод доступных треков на экран.
        for (i,track) in enumerate(self.track_list):
            print('[{}]'.format(i+1))
            lines = track.text.split('\n')
            print('Album  : {}'.format(lines[0]))
            print('Artist : {}'.format(lines[1]))
            if len(lines) > 2:
                print('Genre  : {}'.format(lines[2]))
