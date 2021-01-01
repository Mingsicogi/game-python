import schedule
import time

count = 0

def say_hello():
    count += 1
    print("{} hello~~".format(str(count)))
    

tick_interval = 3

schedule.every(tick_interval).seconds.do(say_hello)



while True:

    if count % 5 == 0:
        tick_interval -= 1

    schedule.run_pending()
    time.sleep(1)