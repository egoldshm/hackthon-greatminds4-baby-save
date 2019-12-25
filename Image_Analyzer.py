import AgeGender
import time
import  safepool
def scan(l_d):
    pred_age=AgeGender()
    for i in pred_age:
        if i.lower <"9":
            i=i+1
    j=len(pred_age)-i
    d={"adults": j, "kids": i}
    safepool(d, l_d ,"001")
    time.sleep(1)
    scan(d)
scan({})