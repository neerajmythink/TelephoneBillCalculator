def readCSVfile(rawfile):
    import pandas as pd
    df = pd.read_excel(rawfile,header=None)
    return df

def getCallCost():
    df = readCSVfile('generated_sample.xlsx')
    unitcost_type1 = 1.0    # applied between 08:00:00 to 16:00:00
    unitcost_type2 = 0.5    # applied outside 08:00:00 to 16:00:00
    unitcost_type3 = 0.2    # applied for extended minutes more than 5 min.
    unitcost_type4 = 0.0    # applied for most frequent number
    totalcost = 0

    for index, row in df.iterrows():
        number     = row[0]
        starttime  = row[1]
        endtime    = row[2]
        duration = (endtime - starttime).seconds/60

        if int(duration) < float(duration):
            duration = int(duration)+1
        else:
            duration = int(duration)

        if duration <= 5:
            if starttime.hour >= 8 and endtime.hour < 16:
                unitcost = unitcost_type1
                callcost = duration*unitcost
            else:
                unitcost = unitcost_type2
                callcost = duration*unitcost
        else:
            rem_time = duration - 5

            if starttime.hour >= 8 and endtime.hour < 16:
                unitcost = unitcost_type1
                callcost = 5*unitcost
            else:
                unitcost = unitcost_type2
                callcost = 5*unitcost
                
            callcost = callcost + rem_time*unitcost_type3


        print(index,'Call start', starttime.time() ,'duration in minutes', duration, 'and the cost' , round(callcost,2))
        totalcost = totalcost + callcost
    print ('total cost ',round(totalcost,2))
    return (totalcost)
    
getCallCost()

