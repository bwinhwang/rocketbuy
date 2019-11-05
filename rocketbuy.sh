#!/bin/bash
date +%M:%S:%N
# submit from cart
adb shell input tap 800 2100 
date +%M:%S:%N
# keep submiting order 100 times

sleep 0.3
i=0 

while [ $i -lt 100 ] 
do 
adb shell input tap 800 2300 
sleep 0.03
i=$[$i+1]
done

date +%M:%S:%N
