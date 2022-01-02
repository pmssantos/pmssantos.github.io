#!/usr/bin/env python3
import fileinput
import os 
import re

f = open('template.html','r')
template = f.read()
f.close()

filelist=os.listdir('src/')
print(filelist)
body_filelist = [file for file in filelist if 'body' in file]

for body in body_filelist:

    body_name=re.search('[^_]*$',body).group(0); # body.partition('_')[2];
    f = open('src/'+body,'r')
    body_content = f.read()
    f.close()
    
    print(body_content)
    body_file = template.replace('REPLACEME',body_content);

    #f = open('../bld/'+body_name,'w')
    f = open(body_name,'w')
    f.write(body_file)
    f.close()
    #print(body_file)
    
    #f = open('template.html','r')

    #with fileinput.FileInput(f, inplace=True, backup='.bak') as file:
    #    for line in file:
    #        print(line.replace(REPLACEME, ), end='')


    #f = write('template.html','r')

#print(filelist)





#F = open(',”w”) 
