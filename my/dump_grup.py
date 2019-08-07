from requests import get,post
from json import loads
from sys import stdout,exit
from time import sleep
from os import remove as apus
import os

import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 2.0)
mengetik('Selamat Datang Di Tools Grab ID Grup Facebook Gunakan Dengan Bijak')
mengetik('Kunjungi Tutorial Termux lainnya Di youtube.com/p/PangeranAlvins')
os.system('clear')

print ('╔═════════════════╗')
print ('   [DUMP ID GRUP FB]')
print ('   [Athor: Alvins]')
print ('╚═════════════════╝')
print
try:
        token=open(raw_input('- Tempat Token Lu? : ')).read().split('\n')[0]
        limit=raw_input('- Mau Ambil Berapa Id cuk : ')
        id=raw_input('- Masukan ID Grup : ')
        output=open('id.txt','w')
        print("- starting ...")
        ambil=get('https://graph.facebook.com/'+id+'?access_token='+token).json()
        print "+ mengambil "+str(limit)+" id dari grup:",ambil['name']
        for x in get('https://graph.facebook.com/'+id+'/members?fields=id&limit='+str(limit)+'&access_token='+token).json()['data']:
                print("\r+ "+x['id']+" ..."),;stdout.flush();output.write(x['id']+"\n")
                sleep(000.001)
        print("\n+ done. "+str(limit)+" id terambil ")
        print("+ output: id.txt")
except:
        print('- token Lu Salah Gan')
        apus('id.txt')
        exit()
