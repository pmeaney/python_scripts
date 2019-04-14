
'''
Goal: 
csv list of:
IP, timestamp, http info, http code
Then, run a lookup on IP codes with: https://www.ipinfodb.com/
For each line in csv file, add location info & usage type.

1. Extract log file names into an array.
2. Loop through file names
3. If file name ends with 'gz' process it as a gzip file, otherwise, read it (as a normal, uncompressed file).
4. During processing, split string various ways to reduce info
5. Lookup IP address using an API, and add the response data to each line.
6. Sort the final data by timestamp.
'''

import gzip
import glob

nginx_logs = glob.glob('./exampleLogs/access*')
# nginx_logs = glob.glob('/var/log/nginx/access*')
print(nginx_logs)

for log in nginx_logs:
  # print(log)
  #get extension.  if extension is .gz, run gzip.open, otherwise open normally.
  lastTwoChars = log[-2:]
  if lastTwoChars == 'gz':
    print('gz file')
    with gzip.open(log,'r') as fin:
      for line in fin:
        # print(line)
        # print(line.split('"-"')[0])
        print(line.split(b'"-"')[0]) # on server, remove the "b"
        '''
        Next step: extract just the ip address, date, and http code.
        So, on the rightside: 
          remote: remove the last integer
          local: remove the last integer, and trim space.
        Then split at:
          1. - -  (leftside: IP. Rightside: everything else)
          2. +0000] (leftside: timestamp, rightside: http request info)
            - Also, trim off the [

        '''
  else:
    print('not a gz file')



# import gzip
# import glob

# nginx_logs = glob.glob('/var/log/nginx/access*')
# #print(nginx_logs)

# for log in nginx_logs:
#   #print(log)
#   # If last two characters are 'gz', run gzip.open, otherwise open normally.
#   lastTwoChars = log[-2:]
#   if lastTwoChars == 'gz':
#     print('gz file')
#     print(log[1])
#     #with gzip.open(log,'r') as fin:
#       #for line in fin:
#       #  print('got line', line)
#   else:
#     print('not a gz file')







#nginx_logs = glob.glob('/var/log/nginx/access*')
#print(nginx_logs)
#for log in nginx_logs:
  #print(log)
#with gzip.open('/var/log/nginx/access.log.10.gz','r') as fin:
#  for line in fin:
#    print('got line', line)

''' 
prints:
('got line', '180.76.15.20 - - [04/Apr/2019:08:56:41 +0000] "GET /robots.txt HTTP/1.1" 404 1540 "-" "Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2"\n')
'''

