#!/usr/bin/python
from subprocess import call

i = 0
mask = 
while i < 256:
address = mask+"."+i;
res = call(["ping", "-c", "1", "-W", "1", address]); 
if res == 0:
print "ping to", address, "worked"
