my_file = open("people_exercise.txt","r")
file_data = my_file.read()
print (file_data)
counter=0
files=file_data.split("\n")
i=0
for i in files:
        counter=counter+1
print("Total lines =",counter)
