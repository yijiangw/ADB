import sys
import subprocess
import time
import os

device_dict={'C6':'FA68W0312642'}
device_list=['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10']
processes=set()

def op(device_name, command):
    if device_name=='all':
        pass
    else:
        device_id=device_dict[device_name]
        text=command%(device_id)
        seg=text.split(' ')
        processes.add(subprocess.Popen(seg))

def op_sc(device_name, command):
    if device_name=='all':
        for device_name in device_list:
            device_id=device_dict[device_name]
            text=command%(device_id, device_name)
            seg=text.split(' ')
            processes.add(subprocess.call(text, shell=True))
    else:
        device_id=device_dict[device_name]
        text=command%(device_id, device_name)
        #print(text)
        seg=text.split(' ')
        processes.add(subprocess.call(text, shell=True))

def op_check(device_name):
    device_id=device_dict[device_name]
    text='adb -s %s shell ls -l mnt/sdcard/DCIM/Camera'%(device_id)
    seg=text.split(' ')
    out1=subprocess.check_output(seg).decode('utf-8')
    #out1_list=[l for l in out1.split('\n') if l[-4:]=='.mp4']
    print(out1)

def op_copy(device_name):
    if device_name=='all':
        pass
    else:
        device_id=device_dict[device_name]
        text='adb -s %s shell ls -l mnt/sdcard/DCIM/Camera'%(device_id)
        seg=text.split(' ')
        out1=subprocess.check_output(seg).decode('utf-8')
        out1_list=[l for l in out1.split('\n') if l[-4:]=='.mp4']
        #print(out1_list)
        time.sleep(2)
        out2=subprocess.check_output(seg).decode('utf-8')
        out2_list=[l for l in out2.split('\n') if l[-4:]=='.mp4']
        #print(out2_list)
        for s in out1_list:
            if s in out2_list:
                video_name=s.split(' ')[-1].strip()
                print('copy %s'%(video_name))
                os.system('adb -s %s pull mnt/sdcard/DCIM/Camera/%s ./'%(device_id, video_name))
                outmp=subprocess.check_output(seg).decode('utf-8')
                outmp_list=[l for l in outmp.split('\n') if l[-4:]=='.mp4']
                print('s:', s)
                print('outmp:', outmp_list)
                if s in outmp_list:
                    print('delete %s'%(video_name))
                    os.system('adb -s %s shell rm mnt/sdcard/DCIM/Camera/%s'%(device_id, video_name))
                

if __name__=='__main__':
    request=sys.argv[1]
    device_name=sys.argv[2]
    if not device_name=='all':
        assert device_name in device_list
    
    if request=='wake_up':
        op(device_name, 'adb -s %s shell input keyevent 224')
        time.sleep(2)
        op(device_name, 'adb -s %s shell input swipe 300 1000 300 500')
    elif request=='open_camera':
        op(device_name, 'adb -s %s shell am start -a android.media.action.VIDEO_CAPTURE')
    elif request=='start_video':
        op(device_name, 'adb -s %s shell input keyevent 24')
    elif request=='end_video':
        op(device_name, 'adb -s %s shell input keyevent 24')
        time.sleep(2)
        op(device_name, 'adb -s %s shell input keyevent 24')
    elif request=='screen_cap':
        op_sc(device_name, 'adb -s %s exec-out screencap -p > %s.png')
    elif request=='check_video':
        op_check(device_name)
    elif request=='copy_video':
        op_copy(device_name)
    if request=='exception':
        op(device_name, 'adb -s %s shell input keyevent 187')
        time.sleep(2)
        op(device_name, 'adb -s %s shell input swipe 300 1000 300 500')
    time.sleep(1)
