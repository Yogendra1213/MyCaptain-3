inp_list=[]
out_list=[]
no=int(input("Enter number of elements in the list:"))
for i in range(0,no):
    a=int(input())
    inp_list.append(a)
print("Input List:",inp_list)
for j in inp_list:
    if j>0:
        out_list.append(j)
print("Output List:",out_list)
