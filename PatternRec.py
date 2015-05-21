import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time


## Raise Numpy floast errors
np.seterr(over='ignore')



totalStart = time.time()
date, bid, ask = np.loadtxt('data/GBPUSD1d.txt', unpack=True,
                            delimiter=',',
                            converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})


avgLine = ((bid+ask)/2)
patternAr = []
performanceAr = []
patforRec = []


## Very simple difference based on the input values 
def percentChange(startPoint, currentPoint):
    try:
      x = ((float(currentPoint)-startPoint)/startPoint)*100.00
      ## Error handling since Numpy bitches about NAN
      if x == 0.0:
            return 0.0000000001
      else:
            return x
    except:
            return 0.000001

def looptest(y,amt):
    patStartTime = time.time()
    x = len(avgLine)-60
    n = 1
    m = amt
    p = 1 
    pattern =[]
    while n <= m:
        print percentChange(avgLine[y - m],avgLine[y - (m - 1)])
        p = p + n
        ##print 'Item', n, p

        ##vars()[p] = percentChange(avgLine[30],avgLine[oset])
        vars()[p] = percentChange(avgLine[y - m],avgLine[y - (m - 1)])
            ##p1 = percentChange(avgLine[30],avgLine[29])
        print 'inside', p, vars()[p]
        n += 1
    print n
    
    ##y += 1
    ##patEndTime = time.time()
    ##print 'Pattern Storage Took:', patEndTime - patStartTime, 'seconds for', len(patternAr) ,'records'
    
    
    
    
    
def patternStorage():
    patStartTime = time.time()
    x = len(avgLine)-60
    y = 31
    print x, y
    while y < x:
        pattern =[]
        p1 = percentChange(avgLine[y-30],avgLine[y-29])
        p2 = percentChange(avgLine[y-30],avgLine[y-28])
        p3 = percentChange(avgLine[y-30],avgLine[y-27])
        p4 = percentChange(avgLine[y-30],avgLine[y-26])
        p5 = percentChange(avgLine[y-30],avgLine[y-25])
        p6 = percentChange(avgLine[y-30],avgLine[y-24])
        p7 = percentChange(avgLine[y-30],avgLine[y-23])
        p8 = percentChange(avgLine[y-30],avgLine[y-22])
        p9 = percentChange(avgLine[y-30],avgLine[y-21])
        p10 = percentChange(avgLine[y-30],avgLine[y]-20)
        
        p11 = percentChange(avgLine[y-30],avgLine[y-19])
        p12 = percentChange(avgLine[y-30],avgLine[y-18])
        p13 = percentChange(avgLine[y-30],avgLine[y-17])
        p14 = percentChange(avgLine[y-30],avgLine[y-16])
        p15 = percentChange(avgLine[y-30],avgLine[y-15])
        p16 = percentChange(avgLine[y-30],avgLine[y-14])
        p17 = percentChange(avgLine[y-30],avgLine[y-13])
        p18 = percentChange(avgLine[y-30],avgLine[y-12])
        p19 = percentChange(avgLine[y-30],avgLine[y-11])
        p20 = percentChange(avgLine[y-30],avgLine[y]-10)
        
        p21 = percentChange(avgLine[y-30],avgLine[y-9])
        p22 = percentChange(avgLine[y-30],avgLine[y-8])
        p23 = percentChange(avgLine[y-30],avgLine[y-7])
        p24 = percentChange(avgLine[y-30],avgLine[y-6])
        p25 = percentChange(avgLine[y-30],avgLine[y-5])
        p26 = percentChange(avgLine[y-30],avgLine[y-4])
        p27 = percentChange(avgLine[y-30],avgLine[y-3])
        p28 = percentChange(avgLine[y-30],avgLine[y-2])
        p29 = percentChange(avgLine[y-30],avgLine[y-1])
        p30 = percentChange(avgLine[y-30],avgLine[y])
        
        outcomeRange = avgLine[y+20:y+30]
        currentPoint= avgLine[y]
        try:
            avgOutcome = reduce(lambda x, y: x+y, outcomeRange) / len(outcomeRange)
        except Exception, e:
            print str(e)
            avgOutcome = 0
        
        futureOutcome =percentChange(currentPoint, avgOutcome)
        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)
        
        pattern.append(p11)
        pattern.append(p12)
        pattern.append(p13)
        pattern.append(p14)
        pattern.append(p15)
        pattern.append(p16)
        pattern.append(p17)
        pattern.append(p18)
        pattern.append(p19)
        pattern.append(p20)
        
        pattern.append(p21)
        pattern.append(p22)
        pattern.append(p23)
        pattern.append(p24)
        pattern.append(p25)
        pattern.append(p26)
        pattern.append(p27)
        pattern.append(p28)
        pattern.append(p29)
        pattern.append(p30)
        patternAr.append(pattern)
        performanceAr.append(pattern)

        y += 1
    patEndTime = time.time()
    print 'Pattern Storage Took:', patEndTime - patStartTime, 'seconds for', len(patternAr) ,'records'
    patternRecognition()


def currentPattern():
    cp1 = percentChange(avgLine[-31], avgLine[-30])
    cp2 = percentChange(avgLine[-31], avgLine[-29])
    cp3 = percentChange(avgLine[-31], avgLine[-28])
    cp4 = percentChange(avgLine[-31], avgLine[-27])
    cp5 = percentChange(avgLine[-31], avgLine[-26])
    cp6 = percentChange(avgLine[-31], avgLine[-25])
    cp7 = percentChange(avgLine[-31], avgLine[-24])
    cp8 = percentChange(avgLine[-31], avgLine[-23])
    cp9 = percentChange(avgLine[-31], avgLine[-22])
    cp10 = percentChange(avgLine[-31], avgLine[-21])
    
    cp11 = percentChange(avgLine[-31], avgLine[-20])
    cp12 = percentChange(avgLine[-31], avgLine[-19])
    cp13 = percentChange(avgLine[-31], avgLine[-18])
    cp14 = percentChange(avgLine[-31], avgLine[-17])
    cp15 = percentChange(avgLine[-31], avgLine[-16])
    cp16 = percentChange(avgLine[-31], avgLine[-15])
    cp17 = percentChange(avgLine[-31], avgLine[-14])
    cp18 = percentChange(avgLine[-31], avgLine[-13])
    cp19 = percentChange(avgLine[-31], avgLine[-12])
    cp20 = percentChange(avgLine[-31], avgLine[-11])
    
    cp21 = percentChange(avgLine[-31], avgLine[-10])
    cp22 = percentChange(avgLine[-31], avgLine[-9])
    cp23 = percentChange(avgLine[-31], avgLine[-8])
    cp24 = percentChange(avgLine[-31], avgLine[-7])
    cp25 = percentChange(avgLine[-31], avgLine[-6])
    cp26 = percentChange(avgLine[-31], avgLine[-5])
    cp27 = percentChange(avgLine[-31], avgLine[-4])
    cp28 = percentChange(avgLine[-31], avgLine[-3])
    cp29 = percentChange(avgLine[-31], avgLine[-2])
    cp30 = percentChange(avgLine[-31], avgLine[-1])
    
    patforRec.append(cp1)
    patforRec.append(cp2)
    patforRec.append(cp3)
    patforRec.append(cp4)
    patforRec.append(cp5)
    patforRec.append(cp6)
    patforRec.append(cp7)
    patforRec.append(cp8)
    patforRec.append(cp9)
    patforRec.append(cp10)
    
    patforRec.append(cp11)
    patforRec.append(cp12)
    patforRec.append(cp13)
    patforRec.append(cp14)
    patforRec.append(cp15)
    patforRec.append(cp16)
    patforRec.append(cp17)
    patforRec.append(cp18)
    patforRec.append(cp19)
    patforRec.append(cp20)
    
    patforRec.append(cp21)
    patforRec.append(cp22)
    patforRec.append(cp23)
    patforRec.append(cp24)
    patforRec.append(cp25)
    patforRec.append(cp26)
    patforRec.append(cp27)
    patforRec.append(cp28)
    patforRec.append(cp29)
    patforRec.append(cp30)
    
    print 'Pat:::', patforRec

def patternRecognition():
    ##patforRec = []
    print 'Pattern Length ', len(patforRec)
    if len(patforRec) != 0:
        for eachPattern in patternAr:
            sim1 = 100.00 - abs(percentChange(eachPattern[0],patforRec[0]))
            sim2 = 100.00 - abs(percentChange(eachPattern[1],patforRec[1]))
            sim3 = 100.00 - abs(percentChange(eachPattern[2],patforRec[2]))
            sim4 = 100.00 - abs(percentChange(eachPattern[3],patforRec[3]))
            sim5 = 100.00 - abs(percentChange(eachPattern[4],patforRec[4]))
            sim6 = 100.00 - abs(percentChange(eachPattern[5],patforRec[5]))
            sim7 = 100.00 - abs(percentChange(eachPattern[6],patforRec[6]))
            sim8 = 100.00 - abs(percentChange(eachPattern[7],patforRec[7]))
            sim9 = 100.00 - abs(percentChange(eachPattern[8],patforRec[8]))
            sim10 = 100.00 - abs(percentChange(eachPattern[9],patforRec[9]))
            
            sim11 = 100.00 - abs(percentChange(eachPattern[10],patforRec[10]))
            sim12 = 100.00 - abs(percentChange(eachPattern[11],patforRec[11]))
            sim13 = 100.00 - abs(percentChange(eachPattern[12],patforRec[12]))
            sim14 = 100.00 - abs(percentChange(eachPattern[13],patforRec[13]))
            sim15 = 100.00 - abs(percentChange(eachPattern[14],patforRec[14]))
            sim16 = 100.00 - abs(percentChange(eachPattern[15],patforRec[15]))
            sim17 = 100.00 - abs(percentChange(eachPattern[16],patforRec[16]))
            sim18 = 100.00 - abs(percentChange(eachPattern[17],patforRec[17]))
            sim19 = 100.00 - abs(percentChange(eachPattern[18],patforRec[18]))
            sim20 = 100.00 - abs(percentChange(eachPattern[19],patforRec[19]))
            
            sim21 = 100.00 - abs(percentChange(eachPattern[20],patforRec[20]))
            sim22 = 100.00 - abs(percentChange(eachPattern[21],patforRec[21]))
            sim23 = 100.00 - abs(percentChange(eachPattern[22],patforRec[22]))
            sim24 = 100.00 - abs(percentChange(eachPattern[23],patforRec[23]))
            sim25 = 100.00 - abs(percentChange(eachPattern[24],patforRec[24]))
            sim26 = 100.00 - abs(percentChange(eachPattern[25],patforRec[25]))
            sim27 = 100.00 - abs(percentChange(eachPattern[26],patforRec[26]))
            sim28 = 100.00 - abs(percentChange(eachPattern[27],patforRec[27]))
            sim29 = 100.00 - abs(percentChange(eachPattern[28],patforRec[28]))
            sim30 = 100.00 - abs(percentChange(eachPattern[29],patforRec[29]))
            
            howsim = (sim1+sim2+sim3+sim4+sim5+sim6+sim7+sim8+sim9+sim10+
                      sim11+sim12+sim13+sim14+sim15+sim16+sim17+sim18+sim19+sim20+
                      sim21+sim22+sim23+sim24+sim25+sim26+sim27+sim28+sim29+sim30)/30.00
        
            if howsim >40:
                patdex = patternAr.index(eachPattern)
                print ' ---------------------------'
                print 'predictedoutcome' , performanceAr[patdex]
                xp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
                fig = plt.figure()
                plt.plot(xp, patforRec)
                plt.plot(xp, eachPattern)
                plt.show()
                matplotlib.use('Agg')
                fig.savefig('charts/chart')


def graphRawFX():

    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
            
    ax1.plot(date,bid)
    ax1.plot(date,ask)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
        
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
        
    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g', alpha=.3)
    
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    plt.subplots_adjust(bottom=.23)
        
    plt.grid(True)
    plt.show()
    ##Use b/c Cloud9 is a pain in the ass
    matplotlib.use('Agg')
    fig.savefig('chart')

def Main():
    ##looptest(31, 2)
    patternStorage()
    currentPattern()
    patternRecognition()
    

##graphRawFX()
##patternStorage()
##currentPattern()
##patternRecognition()
Main()
totalTime = time.time() - totalStart
print 'Entire Processing time took:', totalTime, 'seconds'