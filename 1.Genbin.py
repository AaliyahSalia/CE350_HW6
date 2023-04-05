# Write a function or method with positive int type argument, 
# such as genBin(7), and outputs will be binary number sequence 
# from 1_10 to 7_10, like 1_2,10_2,11_2,100_2 〖,101〗_2 〖,110〗_2,111_2 
# by using queue structure.


from queue import Queue 

def genBin(num):
    q = Queue()
    q.put('1')

    for i in range(num):
        binary_num = q.get()
        print("The binary number is: ", binary_num)

        c1 = binary_num + '0'
        c2 = binary_num + '1'

        if int(c1, 2) <= num:
            q.put(c1)
        if int(c2, 2) <= num:
            q.put(c2)

num = int(input("Please enter a positive integer: "))
print(genBin(num))