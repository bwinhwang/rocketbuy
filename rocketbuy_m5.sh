#!/bin/bash
# script for MI5 

date +%M:%S:%N
############################MMSSNNNNNNNNN
while [[ `date +%M%S%N` -lt 5950500000000 ]]
do 
sleep 1
date +%M:%S
time adb -s 64d72a00 shell input tap 1 1
done
date +%M:%S:%N

############################MMSSNNNNNNNNN
while [[ `date +%M%S%N` -lt 5953000000000 ]]
do 
adb -s 64d72a00 shell input tap 800 1750
sleep 2
adb -s 64d72a00 shell input tap 80 180
done
date +%M:%S:%N

############################MMSSNNNNNNNNN
while [[ `date +%M%S%N` -lt 5959400000000 ]]
do 
sleep 0.1
done
date +%M:%S:%N

# submit from cart
adb -s 64d72a00 shell input tap 800 1750 
date +%M:%S:%N
# keep submiting order 2 times

sleep 0.9
i=0 

while [ $i -lt 2 ] 
do 
adb -s 64d72a00 shell input tap 800 1850 
i=$[$i+1]
done

date +%M:%S:%N
