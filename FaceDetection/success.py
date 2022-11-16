import math, TTS

#Success calculator calculate the success and failure rates and decides the detection status for each success rate.

dict = {"Success Rate":"0.0%", "Failure Rate":"0.0%", "Detection Status":"Unknown"}
def cond1(dict):
    dict["Success Rate"] = str(100.0)+"%"
    dict["Failure Rate"] = str(0.0)+"%"
    dict["Detection Status"] = "Perfection"
    return dict

def cond2(dict):
    dict["Success Rate"] = "Guaranteed Success"
    dict["Failure Rate"] = "No way"
    dict["Detection Status"] = "Exceptionally detected more faces than the actual number of faces. "
    return dict

def cond3(per, dict):
    dict["Success Rate"] = str(100-per)+"%"
    dict["Failure Rate"] = str(per)+"%"
    if per<=10.0:
        dict["Detection Status"] = "Outstandingness"
    elif per>10.0 and per<=20.0:
        dict["Detection Status"] = "Excellency"
    elif per>20.0 and per<=30.0:
        dict["Detection Status"] = "Very Good State"
    elif per>30.0 and per<=40.0:
        dict["Detection Status"] = "Good State"
    elif per>40.0 and  per<=50:
        dict["Detection Status"] = "Average State"
    else:
        dict["Detection Status"] = "Poor State"
    return dict
    
def status_calc(l):
    
    sum1 = math.fsum(list(list(zip(*l))[0]))
    
    sum2 = math.fsum(list(list(zip(*l))[1]))
    
    mean1 = sum1/len(l)
    mean2 = sum2/len(l)
    std_diff = mean1-mean2
    per = (std_diff/mean1)*100
    #std_diff stands for standard difference, which should be equal to zero for perfection in detection

    if std_diff==0:
        return cond1(dict)

    elif std_diff<0:
        return cond2(dict)

    else:
        return cond3(per, dict)
    

def succ_img(per):
    dict = {"Success Rate":"0.0%", "Failure Rate":"0.0%", "Detection Status":"Unknown"}
    if per==0.0:
        return cond1(dict)
    elif per<0.0:
        return cond2(dict)
    else:
        return cond3(per, dict)
    