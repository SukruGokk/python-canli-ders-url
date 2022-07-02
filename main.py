# -*- coding: utf-8 -*-
# @author: Şükrü Erdem Gök
# @version: Python 3.8

from json import loads
from requests import Session
from bs4 import BeautifulSoup as BS
from sys import exit

tc = input('TC: ')
password = input('PASSWORD: ')

with Session() as ses:
    onlineLessonPage = ses.post('https://giris.eba.gov.tr/EBA_GIRIS/OgrenciGiris', data = {'tckn': tc,'password' : password},
                                headers = {'User-Agent' : 'Firefox'})

    if onlineLessonPage.url == 'https://giris.eba.gov.tr/EBA_GIRIS/student.jsp':
        input('HATA\nTc veya parola yanlış')
        exit()

    liveLessonInfo = BS(ses.get('https://ders.eba.gov.tr/ders/getlivelessoninfo', headers = {'User-Agent' : 'Firefox'}).content, 'html.parser')

    try:
        
        liveLessonInfo = loads(str(liveLessonInfo))
        url = liveLessonInfo['liveLessonInfo']['studyTime']['meetingJoinUrl']

        print('CANLI DERS LİNKİ: {}'.format(url))

    except:
        print('CANLI DERSİNİZ BULUNMAMAKTADIR !')
