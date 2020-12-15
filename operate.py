import sys
import subprocess
import time
import os

device_dict={
'C1':'FA7530302218',
'C2':'FA71J0301472',
'C3':'FA68V0300393',
'C4':'FA68B0301761',
'C5':'FA68S0304949',
'C6':'FA68W0312642',
'C7':'84B7N16506004393',
'C8':'84B7N16506004336',
'C9':'84B7N16307001706',
'C10':'FA75K0301214',}
device_list=['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10']
processes=set()

if __name__=='__main__':
    request=sys.argv[1]
    device_name=sys.argv[2].upper()
    if device_name=='ALL':
        name_list=[s for s in device_list]
    else:
        name_list=['C'+s for s in device_name.split('C') if s.isdigit()]
    #print(name_list)
    if request=='wake_up':
        for device_name in name_list:
            processes.add(subprocess.Popen(['python', 'func.wake_up.py', device_name]))
    elif request=='open_camera':
        for device_name in name_list:
            processes.add(subprocess.Popen(['python', 'func.open_camera.py', device_name]))
    elif request=='start_video':
        for device_name in name_list:
            processes.add(subprocess.Popen(['python', 'func.start_video.py', device_name]))
    elif request=='end_video':
        for device_name in name_list:
            processes.add(subprocess.Popen(['python', 'func.end_video.py', device_name]))
    elif request=='screen_cap':
        for device_name in name_list:
            processes.add(subprocess.Popen(['python', 'func.screen_cap.py', device_name]))
    elif request=='list_video':
        for device_name in name_list:
            processes.add(subprocess.Popen(['python', 'func.list_video.py', device_name]))
    elif request=='trans_video':
        folder=str(int(time.time()))
        os.system('mkdir %s'%(folder))
        for device_name in name_list:
            processes.add(subprocess.Popen(['python', 'func.trans_video.py', device_name, folder]))
    elif request=='key':
        for device_name in name_list:
            processes.add(subprocess.Popen(['python', 'func.key.py', device_name, sys.argv[3]]))
    elif request=='carmera':
        for device_name in name_list:
            processes.add(subprocess.Popen(['python', 'func.carmera.py', device_name]))
    elif request=='exception':
        for device_name in name_list:
            processes.add(subprocess.Popen(['python', 'func.exception.py', device_name]))
    else:
        print('Wrong command!')
