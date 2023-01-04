import Sorting as srt
import random

    

#random_data=random.sample(range(0,1000),500)
#dataSort=srt.Sorting(random_data)
#t1=dataSort.InsertionSort("d")
#print(dataSort.data)
#print("Waktu komputasi = ",t1, "detik")

random_data_input=int(input("Masukan berapa banyak bilangan random : "))
random_data_range_input=int(input("Masukan range bilangan random (Contoh : 1000): "))
print("")
print("1. BubleSort")
print("2. SelectionSort")
print("3. InsertionSort")
print("")
PilihSorting=int(input("Masukan Pilihan Sorting : "))


if PilihSorting == 1:
    as_or_des=str(input("Jika Ascending (input 'a'), Jika Descending (input 'd') ?"))
    if as_or_des == "a":
        random_data=random.sample(range(0,random_data_range_input),random_data_input)
        dataSort=srt.Sorting(random_data)
        t1=dataSort.BubleSort("a")
        print(dataSort.data)
        print("Waktu komputasi = ",t1, "detik")
    elif as_or_des == "d":
        random_data=random.sample(range(0,random_data_range_input),random_data_input)
        dataSort=srt.Sorting(random_data)
        t1=dataSort.BubleSort("d")
        print(dataSort.data)
        print("Waktu komputasi = ",t1, "detik")

        
elif PilihSorting == 2:
    as_or_des=str(input("Jika Ascending (input 'a'), Jika Descending (input 'd') ?"))
    if as_or_des == "a":
        random_data=random.sample(range(0,random_data_range_input),random_data_input)
        dataSort=srt.Sorting(random_data)
        t1=dataSort.SelectionSort("a")
        print(dataSort.data)
        print("Waktu komputasi = ",t1, "detik")
    elif as_or_des == "d":
        random_data=random.sample(range(0,random_data_range_input),random_data_input)
        dataSort=srt.Sorting(random_data)
        t1=dataSort.SelectionSort("d")
        print(dataSort.data)
        print("Waktu komputasi = ",t1, "detik")

elif PilihSorting == 3:
    as_or_des=str(input("Jika Ascending (input 'a'), Jika Descending (input 'd') ?"))
    if as_or_des == "a":
        random_data=random.sample(range(0,random_data_range_input),random_data_input)
        dataSort=srt.Sorting(random_data)
        t1=dataSort.InsertionSort("a")
        print(dataSort.data)
        print("Waktu komputasi = ",t1, "detik")
    elif as_or_des == "d":
        random_data=random.sample(range(0,random_data_range_input),random_data_input)
        dataSort=srt.Sorting(random_data)
        t1=dataSort.InsertionSort("d")
        print(dataSort.data)
        print("Waktu komputasi = ",t1, "detik")

else :
    print("Masukan tidak benar")


                
                
        
