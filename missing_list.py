list1 = [2,4,8,10,12,18,22,26,28,32,40]
print('Original list: '+ str(list1))
missing_elements = []
stop = list1[-1] + 1
for num in range(list1[0], stop,2):
    if num not in list1:
        missing_elements.append(num)
print("Missing Numbers List: " + str(missing_elements))
