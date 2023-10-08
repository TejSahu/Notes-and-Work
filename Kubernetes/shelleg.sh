#!/bin/bash
num=$1
a=0
b=1

echo $a
echo $b

for (( i=0; i<$num; i++ ))
do
    c=$(($a+$b))
    echo $c
    a=$b
    b=$c
done
