import os
import random

#dictionary of to do's

#from dictionary pick 3 to do's

todofile = open('todo.txt')

list1 = todofile.readlines()

todofile.close()

#create a text file with the date in title and 3 tasks

select_list = random.sample(list1, 3)
str_list = "\n".join(select_list)

written_file = open('Todo list.txt','w')
written_file.write(str_list)
written_file.close()

print(select_list)
print(str_list)

#remove from dictionary
a = set(list1)
b = set(select_list)

c = a-b

d = "\n".join(c)

#write new list
todofile = open('todo.txt','w')

todofile.write(d)

todofile.close()
