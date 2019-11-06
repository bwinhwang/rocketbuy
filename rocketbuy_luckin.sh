#!/bin/bash
date +%M:%S:%N
############################MMSSNNNNNNNNN
while [[ `date +%M%S%N` -lt 5956500000000 ]]
do 
sleep 1
date +%M:%S
time adb shell input tap 540 2250
done
date +%M:%S:%N

############################MMSSNNNNNNNNN
while [[ `date +%M%S%N` -lt 5959400000000 ]]
do 
sleep 0.1
done
date +%M:%S:%N

# submit from cart
adb shell input tap 540 2250 
date +%M:%S:%N
# keep submiting order 1 times
i=0 
sleep 1
while [ $i -lt 1 ] 
do 
adb shell input tap 540 2250 
date +%M:%S:%N
sleep 0.5
i=$[$i+1]
done

date +%M:%S:%N
