#! /usr/bin/env/ python

from smtplib import SMTP_SSL
from poplib import POP3_SSL
from time import sleep

SMTPSVR = 'smtp.yandex.com'
POP3SVR = 'pop.yandex.com'

who = 'lezgintsev13@yandex.ru'

body = """
From: %(who)s
To: %(who)s
Subject: test msg

Hello world!
""" % {'who': who}

sendSvr = SMTP_SSL(SMTPSVR, 465)
sendSvr.login(who, 'jabraileurope13foreveriwillbe')

errs = sendSvr.sendmail(who, [who], body)

sendSvr.quit()
assert len(errs) == 0, errs
sleep(2)

recvSvr = POP3_SSL(POP3SVR)

recvSvr.user('lezgintsev13@yandex.ru')
recvSvr.pass_('jabraileurope13foreveriwillbe')

numMessages = len(recvSvr.list()[1])
print(recvSvr.retr(483))




