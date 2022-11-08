def readCSVfile(rawfile):
    import pandas as pd
    df = pd.read_excel(rawfile,header=None)
    return df

def get_most_occuerd_value(l):
    import numpy as np
    print("Original List: ", l)
    res = [*set(l)]
    print("List after removing duplicate elements: ", res)
    
    duplicate_data = np.array([[0]*2]*len(res))
    dd=0
    for index_i, ele_i in enumerate(res):
        dd = []
        for index_j, ele_j in enumerate(l):
            if ele_j == ele_i:
                dd.append(ele_i)
            else:
                pass
        print (ele_i,'occured', len(dd), 'times')
        duplicate_data[index_i][0] = ele_i
        duplicate_data[index_i][1] = len(dd)   
    
    sortedArr = duplicate_data[duplicate_data[:,1].argsort()]
    print ('The most occued value is',sortedArr[-1,0], 'and occured', sortedArr[-1,1],'times')
    return sortedArr[-1,0], sortedArr[-1,1]

l = [1, 2, 4, 2, 1, 4, 5, 2]
a,b=get_most_occuerd_value(l)

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

