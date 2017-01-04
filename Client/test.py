#!/usr/bin/python2.7
from subprocess import call
import shlex
import os
import timeit 
from dude import * 
def call1():
      newpath = r'./output-throughput-latency'
      if not os.path.exists(newpath): os.makedirs(newpath)
      os.chdir('./output-throughput-latency')
      rate1=[1,1000, 2000, 5000, 10000, 20000, 30000, 50000, 100000, 150000]
      start_time=0
      stop_time=0
      for i in range(1,10):    
             a=rate1[i]
             a1=str(a)
             
             start_time=timeit.timeit()
             os.system('mcperf --server=172.17.0.2 -p22 -n'+ a1 +' 2>output_new'+str(i)+'.txt')
             stop_time=timeit.timeit() 
             total_time=  (stop_time - start_time)/1000000
             print 'Memcached Experinment: ' + str(i)
             print 'Request Rate: '+a1
             print  'Time of Execution: '+str(total_time)
             print '-----------------------------------------------------------'          
              
import re
import sys
import csv
def greb_output():
     
     f = open("./stats.csv", "wb")
     f.write('rate'',''response'',''latency\n')
     for i in range(1,10):
	
        
     
        with open('output_new'+str(i)+'.txt') as origin:
    	   	for line in origin:
   	     	   if  "Total: connections" in line:
                     reqR=line.split(' ')[2]
                    
                     f.write(reqR)
                     f.write(',')
                    
        with open('output_new'+str(i)+'.txt') as origin1:
   	       for line in origin1:
        	  if  "Response rate" in line:
                     ResR=line.split(': ')[1]
                     ResRate=ResR.split(' ')[0]
                     f.write(ResRate)
                     f.write(',')
                     
        with open('output_new'+str(i)+'.txt') as origin2:
          for line in origin2:
              if  "Connection time [ms]: " in line:
                     ConT=line.split('avg ')[1]
                     ConTime=ConT.split(' ')[0]
                     f.write(ConTime)
                     f.write('\n')
                     
                     
                     
     os.chdir('/home/shermin/memcached exercise')         
     f.close()        

  
call1()
greb_output()
 
