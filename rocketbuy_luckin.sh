#!/bin/bash


function tap()
{
X=$1
Y=$2
adb -s 458fefb shell "sendevent /dev/input/event2 3 58 1000 ;sendevent /dev/input/event2 3 53 ${X};sendevent /dev/input/event2 3 54 ${Y};sendevent /dev/input/event2 1 330 1 ;sendevent /dev/input/event2 0 0 0;sendevent /dev/input/event2 1 330 0;sendevent /dev/input/event2 0 0 0"
}

function submit()
{
    tap 540 2250
}

function back()
{
    tap 100 200
}

function order()
{
    submit
}

date +%M:%S:%N
##########################HHMMSSNNNNNNNNN
while [ `date +%M%S%N` -lt  5956500000000 ]
do 
sleep 1
date +%M:%S
tap 1 1
done
date +%M:%S:%N

############################HHMMSSNNNNNNNNN
while [ `date +%M%S%N` -lt    5959800000000 ]
do 
sleep 0.1
done
date +%M:%S:%N

# submit from cart
submit
date +%M:%S:%N

# keep order 8 times
i=0 
while [ $i -lt 8 ] 
do 
order
i=$[$i+1]
done

date +%M:%S:%N
