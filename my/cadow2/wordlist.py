#!/usr/bin/python
# coding=utf-8
#//Coded By Pangeran Alvins
'''Mau Ngapain Cok !!
'''

import time,os
import struct
import sys
import itertools
import banner
prred = ("\033[91m")
white = ("\033[1;37m")
green = ("\033[92m")
blue = ("033[34m")
pryellow = ("\033[93m")
prLightPurple=("\033[94m")
prCyan=("\033[96m")
prgray = ("\033[97m")
prBlack=("\033[98m")
p  = '\033[35m' # purple
c  = '\033[36m' # cyan



class you:
    def __init__(self):
        print
        self.ohh= time
       
        self.boss = (prred+'[#]localhost@: ')
        print
        print (white+' [#]Temukan File /sdcard/wordlists.txt')
        print
        print
        self.cu = str(raw_input(green+'[#]Masukan Kata (Custom): '))
        self.ohh.sleep(1)
        
        print
        self.min = int(raw_input(prred+'[#]Jumblah Minimal Karakter: '))
        self.ohh.sleep(1)
        print
        self.max = int(raw_input(prgray+'[#]Jumblah Maksimal Karakter: '))
        self.ohh.sleep(1)
        return self.proses()
    def mom(self):
        
        print
        
        self.get = raw_input(self.boss)
        print
        if (self.get=='1' or self.get=='satu'):
            return self.lowercase()
        elif(self.get=='2' or self.get=='dua'):
            return self.uppercase()
        elif(self.get=='3' or self.get=='tiga'):
            return self.num()
        elif(self.get=='4' or self.get=='empat'):
            return self.sp()
        else:
            return self.mom()
    def proses(self):
        print
        print (prred+prgray+'       [#]Pilih Karakter Yang Diminta ')
        print
        print white+' [[1]]'+green+'Huruf Kecil[a-z]'
        print white+' [[2]]'+green+'Huruf besar[A-Z]'
        print white+' [[3]]'+green+'Nomer[0-9]'
        print white+' [[4]]'+green+'Karakter spesial[@#?$%(And More )]'
        return self.mom()
    def num(self):
        print
        self.ohh.sleep(1)
        lat = ('0123456789')
        war= itertools.permutations(lat,self.max)
        fil = open('/sdcard/wordlists.txt','w')
        for x in war:
            self.creat= '\n'+self.cu+('').join(x)
            for g in self.creat:
                fil.write(g)
    def lowercase(self):
        print
        alp = ('abcdefghijklmnopqrstuvwxyz')
        war= itertools.permutations(alp,self.max)
        fil = open('/sdcard/wordlists.txt','w')
        for x in war:
            self.creat= '\n'+self.cu+('').join(x)
            
            for g in self.creat:
                fil.write(g)           
    def k(self):
        self.ohh.sleep(1)
        print
        print (blue+'[✏]Membuat Teks Wordlist')
        print (blue+'[✔]Wordlist Berhasil dibuat') 
    def uppercase(self):
        al = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        warr= itertools.permutations(al,self.max)
        fil = open('/sdcard/wordlists.txt','w')
        for x in warr:
            self.creat= '\n'+self.cu+('').join(x)
            for g in self.creat:
                fil.write(g)    
    def sp(self):
        all = ('''@#$%&-+()*"':;!?,_/.~`|•√π÷×¶∆£¢€¥^°={}\©®™℅[],<>.''')
        wa= itertools.permutations(all,self.max)
        fil = open('/sdcard/wordlists.txt','w')
        for x in wa:
            self.creat= '\n'+self.cu+('').join(x)
            for g in self.creat:
                fil.write(g)