#!/usr/bin/env python3

import multiprocessing
import traceback
import datetime
import time


''' https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064 '''


def nobody(st, et):
    print('1111111', st, et)
    #raise Exception()
    time.sleep(10)


def worker(*args, **kwargs):
    print('will_run', args, kwargs)
    try:
        nobody(*args, **kwargs)
    except:
        print(traceback.format_exc())


def main(st, et):
    p = multiprocessing.Pool(4)
    while st < et:
        ee = st + datetime.timedelta(days=1)
        p.apply_async(worker, args=(st, ee,))
        st = ee
    p.close()
    p.join()



if __name__ == '__main__':
    st = datetime.datetime(2018,1,2)
    et = datetime.datetime(2018,1,13)
    main(st, et)





