import datetime
import nntplib
import threading

from nntplib import NNTP


def main_func(year):
    nntp = NNTP('news.alaska-software.com')
    print(year)
    for month in range(1, 12):
        for day in range(1, 28):
            date = datetime.date(year, month, day)
            groups = nntp.newgroups(date)[1]
            for group in groups:
                try:
                    news = nntp.newnews(group, date)
                except nntplib.NNTPPermanentError:
                    continue
                else:
                    print(news)


threads = []

for year in range(2005, 2018):
    threads.append(threading.Thread(target=main_func, args=(year,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
