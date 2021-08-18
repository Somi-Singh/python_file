banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
f=open("bank_list.txt","w")
for i in banks_list:
    print(i)
    f.write(i)
    f.write("\n")
f.close()