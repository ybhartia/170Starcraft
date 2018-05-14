filepath = 'replayCollection.txt'  
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       # print("Line {}: {}".format(cnt, line.strip()))
       line = line.strip()
       vals = line.split(" ")
       for i in range(0,len(vals)-1):
       	vals[i] = int(vals[i])


       print(vals)
       # READ THE NEXT LINE
       line = fp.readline()
       cnt += 1
      