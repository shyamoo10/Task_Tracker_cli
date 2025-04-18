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


if len(sys.argv) > 1 :
  if sys.argv[1]=="add":
    id=   id_counter()
    data=  {"id":id,"description":sys.argv[2],"status":"todo","createdAt":time,"updatedAt":None}
    add_task(data)
  else:
    print("please correct the syntax")  
else:
  print("please proide an action to perform")    
  
    

  
  



