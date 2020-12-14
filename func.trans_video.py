import sys
import subprocess
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
    os.system('mkdir %s'%(device_name))
    text='adb -s %s shell ls -l mnt/sdcard/DCIM/Camera'%(device_id)
    seg=text.split(' ')
    out1=subprocess.check_output(seg).decode('utf-8')
    out1_list=[l for l in out1.split('\r\n') if l[-4:]=='.mp4']
    time.sleep(2)
    out2=subprocess.check_output(seg).decode('utf-8')
    out2_list=[l for l in out2.split('\r\n') if l[-4:]=='.mp4']
    for s in out1_list:
        if s in out2_list:
            video_name=s.split(' ')[-1].strip()
            print('\n\ncopy %s:%s'%(device_name, video_name))
            os.system('adb -s %s pull mnt/sdcard/DCIM/Camera/%s %s > %s.log'%(device_id, video_name, device_name, device_name))
            outmp=subprocess.check_output(seg).decode('utf-8')
            outmp_list=[l for l in outmp.split('\r\n') if l[-4:]=='.mp4']
            #print('s:', s)
            #print('outmp:', outmp_list)
            if s in outmp_list:
                print('\n\ndelete %s:%s'%(device_name, video_name))
                os.system('adb -s %s shell rm mnt/sdcard/DCIM/Camera/%s'%(device_id, video_name))
    text='adb -s %s shell ls -l mnt/sdcard/DCIM/Camera'%(device_id)
    seg=text.split(' ')
    out_value='\n\n====== %s Finished ====='%(device_name)+':\n'+subprocess.check_output(seg).decode('utf-8')
    print(out_value)
