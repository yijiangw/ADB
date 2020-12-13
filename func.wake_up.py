import sys
#import subprocess
import time
import os

device_dict={
'C9':'84B7N16307001706',
'C8':'84B7N16506004336',
'C7':'84B7N16506004393',
'C4':'FA68B0301761',
'C5':'FA68S0304949',
'C3':'FA68V0300393',
'C6':'FA68W0312642',
'C2':'FA71J0301472',
'C1':'FA7530302218',
'C10':'FA75K0301214',}
device_list=['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10']
#processes=set()

if __name__=='__main__':
    device_name=sys.argv[1]
    assert device_name in device_list
    device_id=device_dict[device_name]
    text='adb -s %s shell input keyevent 224'%(device_id)
    os.system(text)
    #seg=text.split(' ')
    #processes.add(subprocess.Popen(seg))
    time.sleep(2)
    text='adb -s %s shell input swipe 300 1000 300 500'%(device_id)
    os.system(text)
    #seg=text.split(' ')
    #processes.add(subprocess.Popen(seg))
    time.sleep(2)
    text='adb -s %s shell input keyevent 3'%(device_id)
    os.system(text)
