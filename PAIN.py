# Laba_which_make_me_cry

__author__ = 'student'
#!/usr/bin/python3

import os
import sys
import math
from heapq import*

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            for line in f.readlines:
                if len(line.split())==2:
                    self._n=int(line[0])
                    self._nlinks=int(line[1])


            #(n, _nlinks) = (0, 0) # TODO: прочитать из файла

            self._titles = []
            self._sizes = array.array('L', [0]*self._n)
            self._links = array.array('L', [0]*self._nlinks)
            self._redirect = array.array('B', [0]*self.n)
            self._offset = array.array('L', [0]*(self.n+1))
            self._offset[0] = 0
            k = 0

            for i in range(self._n):
                title = f.readline()
                size, flag, link = map(int, f.readline().split())
                title = list(title)
                t = title[0:-1]
                t = ''.join(t)
                self._titles.append(t)
                self._sizes[i] = size
                self._redirect[i] = flag
                self._offset[i+1] = self._offset[i] + link
                for j in range(link):
                    self._links[k] = int(f.readline())
                    k += 1

            # TODO: прочитать граф из файла

        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._offset[_id + 1] - self._offset[_id]

    def get_links_from(self, _id):
        return self._links[self._offset[_id]: self._offset[_id + 1]]

    def get_id(self, title):
        return self._titles.index(title)

    def get_number_of_pages(self):
        return self._n

    def is_redirect(self, _id):
        flag = self._redirect[_id]
        if flag == 0:
            return False
        else:
            return True

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]

    def dijkstra(self, vertex):
        start = self.get_id(vertex)
        d = {v: float('+inf') for v in range(self._n)}
        d[start] = 0
        Q = [(0, start)]
        used = set()
        paths = {vertex: [self.get_title(vertex)]}
        while Q:
            d_c, current = heappop(Q)
            if d_c != d[current]:
                continue
            for neighbor in self.get_links_from(current):
                l = d[current] + 1
                if l < d[neighbor]:
                    d[neighbor] = l
                    heappush(Q, (l, neighbor))
                    paths[neighbor] = [i for i in paths[current]]
                    paths[neighbor].append(self.get_title(neighbor))
            used.add(current)
        return paths
def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

# TODO: статистика и гистограммы

    way = wg.dijkstra('Python')
    r_1 = way[wg.get_id('Список_файловых_систем')]
    r_2 = 0
    r_5 = -1
    r_6 = 0
    off_links = []

    for i in range(wg._n):
        if wg._redirect[i] == 1:
            r_2 += 1
        off = wg.get_number_of_links_from(i)
        off_links.append(off)
        if off > r_5:
            r_5 = off
            r_6 = 0
            r_7_id = i
        if off == r_5:
            r_6 += 1

    r_3 = min(off_links)
    r_4 = off_links.count(r_3)
    r_7 = wg.get_title(r_7_id)
    r_8 = (statistics.mean(off_links) // 0.01) / 100
    r_8_mistake = (statistics.stdev(off_links) // 0.01) / 100

    r_11 = -1
    r_17 = -1
    frequency = [0] * wg._n
    redirects = [0] * wg._n
    for i in range(wg._n):
        if not wg.is_redirect(i):
            link = wg.get_links_from(i)
            for j in range(len(link)):
                n = int(link[j])
                frequency[n] += 1
        else:
            r = int(wg.get_links_from(i)[0])
            redirects[r] += 1
    for i in frequency:
        if i > r_11:
            r_11 = i
            r_12_id = frequency.index(i)
            r_13 = 0
        if i == r_11:
            r_13 += 1
    for i in redirects:
        if i > r_17:
            r_17 = i
            r_19_id = frequency.index(i)
            r_18 = 0
        if i == r_11:
            r_13 += 1

    r_9 = min(frequency)
    r_10 = frequency.count(r_9)
    r_12 = wg.get_title(r_12_id)
    r_14 = (statistics.mean(frequency) // 0.01) / 100
    r_14_mistake = (statistics.stdev(frequency) // 0.01) / 100
    r_15 = min(redirects)
    r_16 = redirects.count(r_15)
    r_19 = wg.get_title(r_19_id)
    r_20 = (statistics.mean(redirects) // 0.01) / 100
    r_20_mistake = (statistics.stdev(redirects) // 0.01) / 100

    print('Кратчайший путь от статьи Python до статьи Список_файловых_систем')
    for i in r_1:
        print(i)
    print('Количество статей с перенаправлением:', r_2)
    print('Минимальное количество ссылок из статьи:', r_3)
    print('Количество статей с минимальным количеством ссылок:', r_4)
    print('Максимальное количество ссылок из статьи:', r_5)
    print('Количество статей с максимальным количеством ссылок:', r_6)
    print('Статья с наибольшим количеством ссылок:', r_7)
    print('Среднее количество ссылок в статье:', r_8, '( среднее отклонение', r_8_mistake, ')')
    print('Минимальное количество ссылок на статью:', r_9)
    print('Количество статей с минимальным количеством внешних ссылок:', r_10)
    print('Максимальное количество ссылок на статью:', r_11)
    print('Количество статей с максимальным количеством внешних ссылок:', r_13)
    print('Статья с наибольшим количеством внешних ссылок:', r_12)
    print('Среднее количество внешних ссылок на статью:', r_14, '( среднее отклонение', r_14_mistake, ')')
    print('Минимальное количество перенаправлений на статью:', r_15)
    print('Количество статей с минимальным количеством внешних перенаправлений:', r_16)
    print('Максимальное количество перенаправлений на статью:', r_17)
    print('Количество статей с максимальным количеством внешних перенаправлений:', r_18)
    print('Статья с наибольшим количеством внешних перенаправлений:', r_19)
    print('Среднее количество внешних перенаправлений на статью:', r_20, '( среднее отклонение', r_20_mistake, ')')
