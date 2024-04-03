def add(evenlist, oddlist,ele):
    if ele % 2 == 0:
        evenlist.append(ele)
    else:
        oddlist.append(ele)
    return evenlist,oddlist

def remove(evenlist,oddlist,count):
    count = count + 1
    if count % 2 == 0:
        evenlist = evenlist[1:]
    else:
        oddlist = oddlist[1:]
    return evenlist, oddlist,count

count = 0
olist = []
elist = []
elist, olist = add(elist,olist, 10)
elist, olist = add(elist,olist, 12)
elist, olist = add(elist,olist, 13)
elist, olist = add(elist,olist, 14)
elist, olist = add(elist,olist, 15)
elist, olist = add(elist,olist, 16)
elist, olist = add(elist,olist, 17)
elist, olist = add(elist,olist, 18)
elist, olist = add(elist,olist, 19)
elist, olist = add(elist,olist, 11)
print(elist)
print(olist)
elist, olist, count = remove(elist,olist, count)
print(elist)
print(olist)


