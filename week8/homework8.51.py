fname = raw_input("Enter file name: ")

fh = open(fname)
count = 0

for lines in fh:
  if lines.startswith('From'):
    lst=lines.split()
    if lst[0] == 'From':
      print lst[1]
      count=count+1

print "There were", count, "lines in the file with From as the first word"

