import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time


## Raise Numpy floast errors
np.seterr(over='ignore')



totalStart = time.time()



## Loads dbGetForexRatesCSV.csv file int date, rate, bid, and ask objects
date, bid, ask = np.loadtxt('data/GBPUSD1d.txt', unpack=True,
                            delimiter=',',
                            converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})


## Commented out in preparation for the new forex_rates API code
##date, rate, bid, ask = np.loadtxt('data/dbGetForexRatesCSV.csv', unpack=True,
##                            delimiter=',',
##                            converters={0:mdates.strpdate2num('%Y-%m-%dT%H:%M:%S.000Z')})




##Creates an avgLine Array that for each bid and ask, gets the average.
avgLine = ((bid+ask)/2)

## Every pattern is stored in the pattern array
patternAr = []

## As we make the pattern, we store the outcome of pattern recognition here
performanceAr = []

patForRec = []


## Very simple difference based on the input values 
def percentChange(startPoint, currentPoint):
    try:
      x = ((float(currentPoint)-startPoint)/abs(startPoint))*100.00
      ## Error handling since Numpy bitches about NAN
      if x == 0.0:
            return 0.0000000001
      else:
            return x
    except:
            return 0.000001


##This function processes the data from the CSV file to calculate the percent change and and future outcome measures    
def patternStorage():
    ## Getting Current Unix Time
    patStartTime = time.time()

    ##Get length of array - 30
    x = len(avgLine)-30

    ##We are skipping the first 30 because our pattern is 30 ticks long
    y = 31
    print x, y
    while y < x:
        pattern =[]
        ## Grabbing the percent change for each tick for the last 30 minutes for each Y
        pattern.append(percentChange(avgLine[y-30],avgLine[y-29]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-28]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-27]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-26]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-25]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-24]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-23]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-22]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-21]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-20]))
        
        pattern.append(percentChange(avgLine[y-30],avgLine[y-19]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-18]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-17]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-16]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-15]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-14]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-13]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-12]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-11]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-10]))

        pattern.append(percentChange(avgLine[y-30],avgLine[y-9]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-8]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-7]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-6]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-5]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-4]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-3]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-2]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y-1]))
        pattern.append(percentChange(avgLine[y-30],avgLine[y]))
        
        ## Splicing the avgLine array to get indexes between (y+20) and (y+30)
        outcomeRange = avgLine[y+20:y+30]

        ##grab current avgLine
        currentPoint= avgLine[y]

        ##In order to avoid a negative infinity percent change, we gotta do this....
        try:
            ##Get the sum of outcomeRanges which is (y+20) to (y+30) and divides that by the number of elements in the array
            avgOutcome = reduce(lambda x, y: x+y, outcomeRange) / len(outcomeRange)

        except Exception, e:
            print str(e)
            avgOutcome = 0
        
        ##Percent difference between the current point and the average outcome of the +20 - +30 points.
        futureOutcome = percentChange(currentPoint, avgOutcome)

        #Appending Results to our arrays for plotting
        patternAr.append(pattern)
        performanceAr.append(futureOutcome)

        y += 1
    patEndTime = time.time()
    print 'Pattern Storage Took:', patEndTime - patStartTime, 'seconds for', len(patternAr) ,'records'
    patternRecognition()

## currentPattern grabs the percent change between the 31st record against the prior 30.
def currentPattern():
    # First we populate an array that has the percent change between the first 30 objects of the avgLine array
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
    

    patForRec.append(cp1)
    patForRec.append(cp2)
    patForRec.append(cp3)
    patForRec.append(cp4)
    patForRec.append(cp5)
    patForRec.append(cp6)
    patForRec.append(cp7)
    patForRec.append(cp8)
    patForRec.append(cp9)
    patForRec.append(cp10)
    
    patForRec.append(cp11)
    patForRec.append(cp12)
    patForRec.append(cp13)
    patForRec.append(cp14)
    patForRec.append(cp15)
    patForRec.append(cp16)
    patForRec.append(cp17)
    patForRec.append(cp18)
    patForRec.append(cp19)
    patForRec.append(cp20)
    
    patForRec.append(cp21)
    patForRec.append(cp22)
    patForRec.append(cp23)
    patForRec.append(cp24)
    patForRec.append(cp25)
    patForRec.append(cp26)
    patForRec.append(cp27)
    patForRec.append(cp28)
    patForRec.append(cp29)
    patForRec.append(cp30)
    
    print 'Pat:::', patForRec



def patternRecognition():
    ##patforRec = []
    print 'Pattern Length ', len(patForRec)
    if len(patForRec) != 0:
        for eachPattern in patternAr:
            sim1 = 100.00 - abs(percentChange(eachPattern[0],patForRec[0]))
            sim2 = 100.00 - abs(percentChange(eachPattern[1],patForRec[1]))
            sim3 = 100.00 - abs(percentChange(eachPattern[2],patForRec[2]))
            sim4 = 100.00 - abs(percentChange(eachPattern[3],patForRec[3]))
            sim5 = 100.00 - abs(percentChange(eachPattern[4],patForRec[4]))
            sim6 = 100.00 - abs(percentChange(eachPattern[5],patForRec[5]))
            sim7 = 100.00 - abs(percentChange(eachPattern[6],patForRec[6]))
            sim8 = 100.00 - abs(percentChange(eachPattern[7],patForRec[7]))
            sim9 = 100.00 - abs(percentChange(eachPattern[8],patForRec[8]))
            sim10 = 100.00 - abs(percentChange(eachPattern[9],patForRec[9]))
            
            sim11 = 100.00 - abs(percentChange(eachPattern[10],patForRec[10]))
            sim12 = 100.00 - abs(percentChange(eachPattern[11],patForRec[11]))
            sim13 = 100.00 - abs(percentChange(eachPattern[12],patForRec[12]))
            sim14 = 100.00 - abs(percentChange(eachPattern[13],patForRec[13]))
            sim15 = 100.00 - abs(percentChange(eachPattern[14],patForRec[14]))
            sim16 = 100.00 - abs(percentChange(eachPattern[15],patForRec[15]))
            sim17 = 100.00 - abs(percentChange(eachPattern[16],patForRec[16]))
            sim18 = 100.00 - abs(percentChange(eachPattern[17],patForRec[17]))
            sim19 = 100.00 - abs(percentChange(eachPattern[18],patForRec[18]))
            sim20 = 100.00 - abs(percentChange(eachPattern[19],patForRec[19]))
            
            sim21 = 100.00 - abs(percentChange(eachPattern[20],patForRec[20]))
            sim22 = 100.00 - abs(percentChange(eachPattern[21],patForRec[21]))
            sim23 = 100.00 - abs(percentChange(eachPattern[22],patForRec[22]))
            sim24 = 100.00 - abs(percentChange(eachPattern[23],patForRec[23]))
            sim25 = 100.00 - abs(percentChange(eachPattern[24],patForRec[24]))
            sim26 = 100.00 - abs(percentChange(eachPattern[25],patForRec[25]))
            sim27 = 100.00 - abs(percentChange(eachPattern[26],patForRec[26]))
            sim28 = 100.00 - abs(percentChange(eachPattern[27],patForRec[27]))
            sim29 = 100.00 - abs(percentChange(eachPattern[28],patForRec[28]))
            sim30 = 100.00 - abs(percentChange(eachPattern[29],patForRec[29]))
            
            howsim = (sim1+sim2+sim3+sim4+sim5+sim6+sim7+sim8+sim9+sim10+
                      sim11+sim12+sim13+sim14+sim15+sim16+sim17+sim18+sim19+sim20+
                      sim21+sim22+sim23+sim24+sim25+sim26+sim27+sim28+sim29+sim30)/30.00
            
            ## This determines how accurate a pattern must be to be determined a good pattern. 70 = 70%
            if howsim > 40:
                patdex = patternAr.index(eachPattern)


                print '####################'
                print '####################'
                print patForRec
                print '===================='
                print '===================='
                print eachPattern
                print '--------------------'
                print 'predicted outcome', performanceAr[patdex]
                xp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
                fig = plt.figure()
                plt.plot(xp, patForRec)
                plt.plot(xp, eachPattern)
                plt.show()
                print '####################'
                print '####################'


def Main():
    ##looptest(31, 2)
    patternStorage()
    currentPattern()
    patternRecognition()

Main()
totalTime = time.time() - totalStart
print 'Entire Processing time took:', totalTime, 'seconds'