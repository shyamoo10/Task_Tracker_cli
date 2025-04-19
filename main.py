import sys
import json
from datetime import datetime
fulltime=  datetime.now().time()
str_fulltime=  str(fulltime)
time_split=  str_fulltime.split(".")
time=  time_split[0]


def read_file(file_name):
  with open(file_name,"r")  as f:
     content =f.read()
     
     f.close()
     return content
     
def write_file(data,file_name):
    with open(file_name,"w") as f:
        
        str_data=  json.dumps(data)       
    
        f.write(str_data)
        f.close()
        
        
        
def add_task(data):
  content=  read_file("./tasks.json")
  parsed_content =  json.loads(content)
  parsed_content[data["id"]]=  data
  write_file(parsed_content,"./tasks.json")
  print("data added successfully")


def id_counter():
   count= read_file("./count.txt")
   int_count=  int(count)
   new_count=  int_count+1
   write_file(new_count,"./count.txt")
   new_id=  read_file("./count.txt")
   return new_id

def update(id,data):
  tasks=  read_file("./tasks.json")
  parsed_tasks=  json.loads(tasks)
  if str(id) in parsed_tasks:
    
   parsed_tasks[str(id)]["description"]= data
   parsed_tasks[str(id)]["updatedAt"] =time
   write_file(parsed_tasks,"./tasks.json")
   print("task updated succesfully")
  else:
    print("invalid task id")
     
  
print(len(sys.argv))
print(sys.argv)


if len(sys.argv) >  1 :
  if sys.argv[1]=="add":
    if len(sys.argv )==3 :
     id=   id_counter()
     data=  {"id":id,"description":sys.argv[2],"status":"todo","createdAt":time,"updatedAt":None}
     add_task(data)
    else:
        print("incorrect input format")
  elif sys.argv[1]=="update":
    if len(sys.argv) == 4   :
      update(sys.argv[2],sys.argv[3])
    else:
       print("incorrect input format")
  else:
    print(f"the provided  action {sys.argv[1]} cant be performed")     
       
      
    
else:
  print("please provide an action to perform")    
  
    

  
  



