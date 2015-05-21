#Test script that grabs data from Yahoo Financials API for certain stocks.
#DO NOT DELETE!!!

import time
import datetime
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates


eachStock = 'TSLA','AAPL'

def graphData(stock):
    try:

        stockfile = stock +'.txt'
        print stockfile
        date, closep, highp, lowp, openp, volume = np.loadtxt(stockfile,delimiter=',',unpack=True,
                                                              converters={ 0: mdates.strpdate2num('%Y%m%d')})
        fig = plt.figure()
        ax1 = plt.subplot(1,1,1)
        ax1.plot(date, openp)
        ax1.plot(date, highp)
        ax1.plot(date, lowp)
        ax1.plot(date, closep)
        ax1.grid(True)
        
        
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
            
        plt.subplots_adjust(left=.10,bottom=.19, right= .93, top=.95,wspace=.20, hspace=.07)    
            
        plt.xlabel('Date')
        plt.ylabel('Stock Price')
        plt.suptitle(stock+' Stock Price')
            
        
        plt.show()
        matplotlib.use('Agg')
        fig.savefig(stock)
    #print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        
        
    except Exception, e:
        print 'failed main loop ', str(e)
        
        
        
        
for stock in eachStock:
    graphData(stock)
    
    