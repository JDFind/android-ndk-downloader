#!/usr/bin/env python

# Modifications Copyright 2018 JDFind
# Author: Tzutalin <tzu.ta.lin@gmail.com>
# Copyright 2017 Tzutalin
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import collections
import json
import os

def init():

    # fixes Python 2.x/ 3.x compatibility issues with raw_input/ input
    try: input = raw_input
    except NameError: pass

    with open('table.json') as data_file:
        url_table = json.load(data_file)

    if url_table is None or len(url_table) <= 0:
        print('\033[91m' + ' There is no item in table.json ' + '\033[0m')
        os.sys.exit(0)

    index = 0
    for key in url_table:
        index = index + 1
        print('[' + str(index) + ']\t' + key)

    return url_table

def getTargetLink(desired_index, url_table):
    index = 0
    for key in url_table:
        index = index + 1
        if desired_index == index:
            return url_table[key]
    return None

def download(url):
    if url == None:
        return

    file_name = url.split('/')[-1]
    u = urlopen(url)
    f = open(file_name, 'wb')
    file_size = int(u.headers['Content-Length'])
    print("Downloading: %s Bytes: %s" % (file_name, file_size))

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print(status)

    f.close()

if __name__ == '__main__':
    url_table = init()
    var = input("Please enter the numer you want to download: ")
    link = getTargetLink(int(var), url_table)
    download(link)
