#Write a python program to make a 2-dimensional list that contains represents a table of records, for instance, student details like Roll no, Student Name, Marks; And complete the following 2 sub-tasks.
#i) Add some records in the list and print the list in tabular form,
#ii) From created list, extract and print second record/row that contains

#install and import the tabulate module
from tabulate import tabulate
mydata = [["1", "abc","100"], 
          ["2", "def","95"], 
          ["3", "ghi","90"], 
          ["4", "jkl","85"]]
head = ["Roll no.", "Name","marks"]
#subtask-1
mydata.append(["5", "mno","80"])
print(tabulate(mydata, headers=head, tablefmt="plain"))
#Subtask-2
print(mydata[1])





