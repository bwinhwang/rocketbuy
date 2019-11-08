#!/bin/bash

function tap()
{
X=$1
Y=$2
adb -s 458fefb shell "sendevent /dev/input/event2 3 58 1000 ;sendevent /dev/input/event2 3 53 ${X};sendevent /dev/input/event2 3 54 ${Y};sendevent /dev/input/event2 1 330 1 ;sendevent /dev/input/event2 0 0 0;sendevent /dev/input/event2 1 330 0;sendevent /dev/input/event2 0 0 0"
}

function submit()
{
    tap 800 2100
}

function back()
{
    tap 100 200
}

function order()
{
    tap 800 2300
}

date +%H:%M:%S:%N


##############################HHMMSSNNNNNNNNN
while [[ `date +%H%M%S%N` -lt 194500000000000 ]]
do 
date +%M:%S
sec=$(random 60 600)
echo "sleep $sec"
sleep $sec
submit
sleep $(random 10 10)
back
done

date +%M:%S:%N
##############################HHMMSSNNNNNNNNN
while [[ `date +%H%M%S%N` -lt 195950500000000 ]]
do 
sleep 1
date +%M:%S
time tap 1 1
done
date +%M:%S:%N

############################MMSSNNNNNNNNN
while [[ `date +%M%S%N` -lt 5953000000000 ]]
do 
submit
sleep 2
back
done
date +%M:%S:%N

############################MMSSNNNNNNNNN
while [[ `date +%M%S%N` -lt 5959750000000 ]]
do 
sleep 0.05
done
date +%M:%S:%N

# submit from cart
submit
date +%M:%S:%N
# keep submiting order 9 times

sleep 0.3
i=0 

while [ $i -lt 5 ] 
do 
order
i=$[$i+1]
done

date +%M:%S:%N
