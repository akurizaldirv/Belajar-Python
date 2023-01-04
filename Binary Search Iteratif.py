def binarySearch(listData, data):
    iteration = 0
    first = 0
    last = len(listData)-1
    found = False
    temp = []
    while first<=last and not found:
        midpoint=(first+last)//2

        
        print('first:', listData[first], ', last:', listData[last], ', midpoint:', listData[midpoint])
        
        if listData[midpoint]==data:
            found=True
            temp.append(midpoint)
            midpoint1 = midpoint
            if midpoint == last:
                break
            elif midpoint == first:
                break
            else:
                
                while listData[midpoint1+1] == data:
                    if midpoint1+1 == last:
                        temp.append(midpoint1+1)
                        break
                    else:
                        temp.append(midpoint1+1)
                        midpoint1 += 1

                while listData[midpoint-1] == data:
                    if midpoint-1 == first:
                        temp.insert(0, midpoint-1)
                        break
                    else:
                        temp.insert(0,midpoint-1)
                        midpoint -= 1
                
        else:
            if data<listData[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1

    if found==True:
        print('Data ditemukan di index =', temp)
        return found
    else:
        print('Data tidak ditemukan')
        return False

a=[3,5,9,12,12,12,14,15,19]
binarySearch(a, 12)
