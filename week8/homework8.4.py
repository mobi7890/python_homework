fname=raw_input("Enter file name:")
fh=open(fname)
lst=list()
for line in fh:
    newline=line.rstrip()
    newlist=newline.split()
    for words in newlist:
        if words not in lst:
            lst.append(words)
lst.sort()
print lst
