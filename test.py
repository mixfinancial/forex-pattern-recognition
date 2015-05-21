
def percentChange(startPoint, currentPoint):
    return ((float(currentPoint)-startPoint)/startPoint)*100.00
    
    
def patternFinder():
    avgLine = ((bid+ask)/2
    x = len(avgLine)-30
    
        y = 11
        while y < x:
        p1 = percentChange(avgLine[y-10],avgLine[y-9])
        p2 = percentChange(avgLine[y-10],avgLine[y-8])
        p3 = percentChange(avgLine[y-10],avgLine[y-7])
        p4 = percentChange(avgLine[y-10],avgLine[y-6])
        p5 = percentChange(avgLine[y-10],avgLine[y-5])
        p6 = percentChange(avgLine[y-10],avgLine[y-4])
        p7 = percentChange(avgLine[y-10],avgLine[y-3])
        p8 = percentChange(avgLine[y-10],avgLine[y-2])
        p9 = percentChange(avgLine[y-10],avgLine[y-1])
        p10 = percentChange(avgLine[y-10],avgLine[y])
        
        outcomeRange = avgLine[y+20:y+30]
        currentPoint= avgLine[y]
        
        print reduce(lambda x, y: x+y, outcomeRange) / len(outcomeRange)
        print currentPoint
        print '________'
        
        print p1,p2,p3,p4,p5,p6,p7,p8,p9,p10
        y += 1
        time.sleep(5555)