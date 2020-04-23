
#This program works for only non duplicate values
list1=[27,2,1,32,56,0]

for i in range(len(list1)):
    min_value = min(list1[i:])
    min_index=list1.index(min_value)
    #swapping
    list1[i],list1[min_index]=list1[min_index],list1[i]

print(list1)

"""
    another method for swapping
    temp=list1[0]
    list1[0]=list1[min_index]
    list1[min_index]=temp
    """

#This program works for   duplicate values
list2=[27,2,2,1,32,0,56,0]
for i in range(len(list2)):
    min_value = min(list2[i:])
    min_index=list2.index(min_value,i)
    #swapping
    list2[i],list2[min_index]=list2[min_index],list2[i]
print("duplicate values")
print(list2)