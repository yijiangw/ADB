# ADB
唤起：

    adb shell input keyevent 224
[![reG0PI.png](https://s3.ax1x.com/2020/12/13/reG0PI.png)](https://imgchr.com/i/reG0PI)

adb 唤起后滑动解锁：

    adb shell input swipe 300 1000 300 500
[![reGBGt.png](https://s3.ax1x.com/2020/12/13/reGBGt.png)](https://imgchr.com/i/reGBGt)

adb 开始打开录像机

    adb -s FA68W0312642 shell am start -a android.media.action.VIDEO_CAPTURE
[![reGrxf.png](https://s3.ax1x.com/2020/12/13/reGrxf.png)](https://imgchr.com/i/reGrxf)

adb 音量加开始录像

adb -s FA68W0312642 shell input keyevent 24

[![reGDRP.png](https://s3.ax1x.com/2020/12/13/reGDRP.png)](https://imgchr.com/i/reGDRP)

adb 查看录像文件

    adb -s FA68W0312642 shell ls -l mnt/sdcard/DCIM/Camera

    total 183168
    -rw-rw---- 1 root sdcard_rw 187552069 2018-01-03 12:22 VID_20180103_122003.mp4

adb 删除录像文件

    adb -s FA68W0312642 shell rm mnt/sdcard/DCIM/Camera/VID_20180103_122003.mp4

adb 传回录像文件

    adb -s FA68W0312642 pull mnt/sdcard/DCIM/Camera/VID_20180103_122003.mp4 /C0/Yijiang/a1+TIMESTAMP.mp4

ADB 截屏保存

    adb -s FA68B0301761  exec-out screencap -p > x.png
