import timeit
class Sorting:

    def __init__(self,data_random):
        self.data=data_random

    def BubleSort(self,Asced_Desced):
        data=self
        AD=Asced_Desced
        if AD == "a":
            count=0
            for outIter in range(len(data)-1,-1,-1):
                count=count+1
                print ('Iterasi ke-', count,':')
                for i in range(outIter):
                    if data[i]>data[i+1]:
                        temp=data[i]
                        data[i]=data[i+1]
                        data[i+1]=temp
                        #listData[i],listData[i+1]=listData[i+1],listData[i]
                    print(listData)
            #print('Data urut-',listData)
        elif AD == "d":
            count=0
            for outIter in range(len(data)-1,-1,-1):
                count=count+1
                for i in range(outIter):
                    if data[i]<data[i+1]:
                        temp=data[i]
                        data[i]=data[i+1]
                        data[i+1]=temp
        else:
            print("Masukan tidak benar")
            
        return timeit.timeit()

    

    def SelectionSort(self,Asced_Desced):
        data=self.data
        AD=Asced_Desced
        if AD == "a":
            #print('Algoritma Selection Sort konvensional')
            #print('Data Awal=',listData)
            for outIter in range(len(data)-1):
                minIndex=outIter
                for i in range(outIter+1,len(data)):
                    if data[i]<data[minIndex]:
                        minIndex=i
                temp=data[outIter]
                data[outIter]=data[minIndex]
                data[minIndex]=temp
                #print('Iterasi ke-',outIter+1,':',listData)
            #print('Data Urut=',listData)
        elif AD == "d":
            count=0
            for outIter in range(len(data)-1,-1,-1):
                count=count+1
                for i in range(outIter):
                    if data[i]<data[i+1]:
                        temp=data[i]
                        data[i]=data[i+1]
                        data[i+1]=temp
        else:
            print("Masukan tidak benar")
            
        return timeit.timeit()



    def InsertionSort(self,Asced_Desced):
        data=self.data
        AD=Asced_Desced
        if AD == "a":
            for outIter in range(1,len(data)):
                #print(data)
                key=data[outIter]
                ind=outIter
                while (ind>0 and data[ind-1]>key):
                    data[ind]=data[ind-1]
                    ind=ind-1
                    #print('inner=',data)
                data[ind]=key
            #print('sortedData=',data)
        elif AD == "d":
            for outIter in range(1,len(data)):
                #print(data)
                key=data[outIter]
                ind=outIter
                while (ind>0 and data[ind-1]<key):
                    data[ind]=data[ind-1]
                    ind=ind-1
                    #print('inner=',data)
                data[ind]=key
            #print('sortedData=',data)
        else:
            print("Masukan tidak benar")
            
        return timeit.timeit()
data = [7,6,5,4,3,2]
print(Sorting.BubleSort(data,'a'))
