#!/bin/bash
if [ $(wc -l < $1) -lt 10000 ]; then 
    echo "Input Error, File must have at least 10000 lines!"
else
    wc -l < $1
    head -n 1 $1
    tail -n 10000 $1| grep -i "potus" | wc -l
    tail -n +100 $1 | head -n 101 | grep -w "fake" | wc -l 
fi


