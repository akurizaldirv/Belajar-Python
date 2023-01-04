def unorder(listData, data):
    ind = 0
    hasil = []
    found = False
    while ind < len(listData) and not found:
        if listData[ind] == data:
            hasil.append(ind)
            found = True
            ind += 1
        else:
            ind = ind+1
        print(ind)
    if hasil == []:
        return ('Data tidak ada')
    else:
        return ('Data ditemukan di index =', hasil)
        

def order(listData, data):
    ind = 0
    found = False
    stop = False
    position=[]
    while ind < len(listData) and not found and not stop:
        if listData[ind] == data:
            found = True
            position.append(ind)
            ind += 1
            while listData[ind] == data:
                found = True
                position.append(ind)
                ind += 1
        else:
            if listData[ind] > data:
                stop = True
                ind += 1
            else:
                ind = ind+1
        print(ind)
    if found:
        return ('Data ditemukan di index =',position)
    else:
        return ('Data tidak ada')


print("Unordered Sequential Seatch")
data = [9,12,5,3,15,19,14]
print('Data =',data)
print(unorder(data, 12))
print("\n")


print("Ordered Sequential Search")
data1 = [3,5,9,12,14,15,19]
print("Data =", data1)
print(order(data1, 12))
