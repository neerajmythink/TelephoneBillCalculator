def readCSVfile(rawfile):
    import pandas as pd
    df = pd.read_excel(rawfile,header=None)
    return df

def get_most_occuerd_value(data):
    import numpy as np
    res = [*set(data)]
    duplicate_data = np.zeros((len(res), 2), dtype=float)
    dd=0
    for index_i, ele_i in enumerate(res):
        dd = []
        for index_j, ele_j in enumerate(l):
            if ele_j == ele_i:
                dd.append(ele_i)
            else:
                pass
        duplicate_data[index_i][0] = ele_i
        duplicate_data[index_i][1] = len(dd)   
    
    sortedArr = duplicate_data[duplicate_data[:,1].argsort()]
    print ('The most occued number is',int(sortedArr[-1,0]), 'and occured', int(sortedArr[-1,1]),'times')
    return int(sortedArr[-1,0])

def getCallCost(df):
    
    unitcost_type1 = 1.0    # applied between 08:00:00 to 16:00:00
    unitcost_type2 = 0.5    # applied outside 08:00:00 to 16:00:00
    unitcost_type3 = 0.2    # applied for extended minutes more than 5 min
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


        # print(index,'Call start', starttime.time() ,'duration in minutes', duration, 'and the cost' , round(callcost,2))
        totalcost = totalcost + callcost
    print ('total cost ',round(totalcost,2))
    return (totalcost)

df = readCSVfile('generated_sample.xlsx')
l = list(df[0])
import pandas as pd
freq_number = get_most_occuerd_value(list(df[0]))
new_df = []
for index, ele in enumerate(df.iterrows()):
    if ele[1][0] == freq_number:
        pass
    else:
        new_df.append(list(ele[1]))

new_df = pd.DataFrame(new_df)
getCallCost(new_df)
    
        

