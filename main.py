import time

from RequestProvider import RequestProvider
from RequestProvidersScheduler import RequestProvidersScheduler
from threading import Thread


news_api = RequestProvider("https://newsapi.org/v2/top-headlines?country=us&apiKey=", "0a3682d43c4b47eab54374b1b5f2fc19", 20)
news_api1 = RequestProvider("https://newsapi.org/v2/top-headlines?country=us&apiKey=", "0a3682d43c4b47eab54374b1b5f2fc19", 10)

if __name__ == "__main__":
    scheduler = RequestProvidersScheduler([news_api,news_api1], True)
    scheduler_thread = Thread(target=scheduler.run)
    scheduler_thread.start()
    # time.sleep(10) # wait for 10 seconds for example
    # scheduler.stop()
    # schedule.clear()
