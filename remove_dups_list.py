#!/usr/bin/python

mylist = ['john','kate', 'john', 'kate', 'meg', 'harry', 'will', 'will']
# mylist = [1,2,3,2,1,3,5,6,3,2,5,3,1,4]

print mylist

def remove_dups(slist):
    rlist = []
    for i in slist:
        if (len(rlist) == 0):
            rlist.append(i)
        else:
            if (i not in rlist):
               rlist.append(i)
    return rlist

outlist = remove_dups(mylist)
print outlist
