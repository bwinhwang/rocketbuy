#!/bin/bash
# script for MI5 

#http://androidxref.com/4.4_r1/xref/prebuilts/ndk/6/platforms/android-9/arch-arm/usr/include/linux/input.h
# EV_SYN 0 EV_KEY 1 EV_ABS 3

# data of a typical click collected from getevent
#[   14275.464083] /dev/input/event2: 0003 0039 00000090
#[   14275.464083] /dev/input/event2: EV_ABS       ABS_MT_TRACKING_ID   00000090            
#[   14275.464083] /dev/input/event2: 0001 014a 00000001
#[   14275.464083] /dev/input/event2: EV_KEY       BTN_TOUCH            DOWN                
#[   14275.464083] /dev/input/event2: 0001 0145 00000001
#[   14275.464083] /dev/input/event2: EV_KEY       BTN_TOOL_FINGER      DOWN                
#[   14275.464083] /dev/input/event2: 0003 0035 0000034f
#[   14275.464083] /dev/input/event2: EV_ABS       ABS_MT_POSITION_X    0000034f            
#[   14275.464083] /dev/input/event2: 0003 0036 000006a9
#[   14275.464083] /dev/input/event2: EV_ABS       ABS_MT_POSITION_Y    000006a9            
#[   14275.464083] /dev/input/event2: 0003 0030 00000004
#[   14275.464083] /dev/input/event2: EV_ABS       ABS_MT_TOUCH_MAJOR   00000004            
#[   14275.464083] /dev/input/event2: 0003 0031 00000004
#[   14275.464083] /dev/input/event2: EV_ABS       ABS_MT_TOUCH_MINOR   00000004            
#[   14275.464083] /dev/input/event2: 0000 0000 00000000
#[   14275.464083] /dev/input/event2: EV_SYN       SYN_REPORT           00000000            
#[   14275.512061] /dev/input/event2: 0003 0039 ffffffff
#[   14275.512061] /dev/input/event2: EV_ABS       ABS_MT_TRACKING_ID   ffffffff            
#[   14275.512061] /dev/input/event2: 0001 014a 00000000
#[   14275.512061] /dev/input/event2: EV_KEY       BTN_TOUCH            UP                  
#[   14275.512061] /dev/input/event2: 0001 0145 00000000
#[   14275.512061] /dev/input/event2: EV_KEY       BTN_TOOL_FINGER      UP                  
#[   14275.512061] /dev/input/event2: 0000 0000 00000000
#[   14275.512061] /dev/input/event2: EV_SYN       SYN_REPORT           00000000 
#

function tap()
{
#/dev/input/event2: EV_ABS       ABS_MT_TRACKING_ID   ffffffff            
# adb shell sendevent /dev/input/event2 3 57 -1
#/dev/input/event2: EV_KEY       BTN_TOUCH            DOWN                
adb shell sendevent /dev/input/event2 1 330 1
#/dev/input/event2: EV_KEY       BTN_TOOL_FINGER      DOWN                
# adb shell sendevent /dev/input/event2 1 325 1  
#/dev/input/event2: EV_ABS       ABS_MT_POSITION_X    0000036f            
adb shell sendevent /dev/input/event2 3 53 950  
#/dev/input/event2: EV_ABS       ABS_MT_POSITION_Y    000006a3            
adb shell sendevent /dev/input/event2 3 54 1750
#/dev/input/event2: EV_ABS       ABS_MT_TOUCH_MAJOR   00000003            
# adb shell sendevent /dev/input/event2 3 48 5
#/dev/input/event2: EV_ABS       ABS_MT_TOUCH_MINOR   00000003            
# adb shell sendevent /dev/input/event2 3 49 5
#/dev/input/event2: EV_SYN       SYN_REPORT           00000000            
adb shell sendevent /dev/input/event2 0 0 0
#/dev/input/event2: EV_ABS       ABS_MT_TRACKING_ID   ffffffff            
# adb shell sendevent /dev/input/event2 3 57 -1
#/dev/input/event2: EV_KEY       BTN_TOUCH            UP 
adb shell sendevent /dev/input/event2 1 330 0
#/dev/input/event2: EV_KEY       BTN_TOOL_FINGER      UP                
# adb shell sendevent /dev/input/event2 1 325 0
adb shell sendevent /dev/input/event2 0 0 0
}

function tap2()
{
adb shell sendevent /dev/input/event2 1 330 1
adb shell sendevent /dev/input/event2 3 53 950  
adb shell sendevent /dev/input/event2 3 54 1750
adb shell sendevent /dev/input/event2 0 0 0
adb shell sendevent /dev/input/event2 1 330 0
adb shell sendevent /dev/input/event2 0 0 0
}

#   ____\ X
#  |    /
#  |
#  |
# \|/
#Y

function tap()
{
X=$1
Y=$2
adb shell "sendevent /dev/input/event2 1 330 1 ;sendevent /dev/input/event2 3 53 ${X};sendevent /dev/input/event2 3 54 ${Y};sendevent /dev/input/event2 0 0 0;sendevent /dev/input/event2 1 330 0;sendevent /dev/input/event2 0 0 0"
}

function submit()
{
    tap 950 1750
}

function back()
{
    tap 100 200
}

function order()
{
    tap 950 1850
}



date +%M:%S:%N
submit
date +%M:%S:%N
sleep 0.8
back
date +%M:%S:%N
