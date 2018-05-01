from poplib import POP3_SSL

p = POP3_SSL('pop.yandex.com')
p.user('lezgintsev13@yandex.com')
p.pass_('jabraileurope13foreveriwillbe')

p.stat()
p.noop()
p.top(1, 2)
p.quit()
