def add_stack(inlist,ele):
    inlist.append(ele)
    return inlist
def remove_stack(inlist):
    inlist.pop()
    return inlist

stacklist = []

add_stack(stacklist,10)
add_stack(stacklist,20)
add_stack(stacklist,30)
add_stack(stacklist,40)
add_stack(stacklist,50)
print(stacklist)

remove_stack(stacklist)
remove_stack(stacklist)
print(stacklist)

add_stack(stacklist,60)
add_stack(stacklist,70)
add_stack(stacklist,80)
print(stacklist)
