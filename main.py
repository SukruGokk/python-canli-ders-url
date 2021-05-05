# -*- coding: utf-8 -*-
# @date: 6.5.2021
# @author: Şükrü Erdem Gök
# @version: Python 3.8
# @os: Ubuntu 20.04
# @github: https://github.com/SukruGokk

# EBA Canlı Ders Url-Scrapper

# Lib
from json import loads
from requests import Session
from bs4 import BeautifulSoup as BS
from sys import exit

# Gerekli inputlar alınıyor
tc = input('TC: ')
password = input('PASSWORD: ')

with Session() as ses:
# Eba'da oturum açma
    onlineLessonPage = ses.post('https://giris.eba.gov.tr/EBA_GIRIS/OgrenciGiris', data = {'tckn': tc,'password' : password},
                                headers = {'User-Agent' : 'Firefox'})

    # Eğer şifre veya parola yanlışsa, sayfa değişmeyeceğinden link aynı kalır bu yolla da yanlışlık olduğu tespit edilebilir
    if onlineLessonPage.url == 'https://giris.eba.gov.tr/EBA_GIRIS/student.jsp':
        input('HATA\nTc veya parola yanlış')# Hata veriyo
        exit()

    # Canlı dersin bilgilerinin bulunduğu bölümdeki json bilgilerini işliyo
    liveLessonInfo = BS(ses.get('https://ders.eba.gov.tr/ders/getlivelessoninfo', headers = {'User-Agent' : 'Firefox'}).content, 'html.parser')

    try:# Eğer canlı ders yoksa program hata verip durmasın diye try-except yapısı ile canlı dersin olup olmadığı anlaşılabilir
        
        liveLessonInfo = loads(str(liveLessonInfo)) # Json verilerini bir değişkene atama
        url = liveLessonInfo['liveLessonInfo']['studyTime']['meetingJoinUrl'] # Verilerden linki çekiyor

        print('CANLI DERS LİNKİ: {}'.format(url))# Bulunan linki ekrana yazılıyor

    except:# Eğer ders yoksa;
        print('CANLI DERSİNİZ BULUNMAMAKTADIR !')
