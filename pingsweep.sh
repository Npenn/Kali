#!/bin/bash

mask=$1;
for i in {0..255};
do ping -c 1 -W 1 $mask.$i | grep 'from';
done
