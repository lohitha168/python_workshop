contact={}
def add_cont(name,phno):
    if(name in contact.keys()):
        print(name,'contact already exists')
    else:
        contact[name]=phno
        print("contact added successfully")
def disp_cont():
    i=1
    if(i<len(contact)):
        for name,phno in contact.items():
              print(i,".name=",name,",phno=",phno)
              i+=1
def del_cont(name):
    if(name in contact.keys()):
        contact.pop(name)
        print("deleted successfully")
       # for name in contact.items():
    else:
        print(name,"does not exist")
def update_cont(name,phno):
    if(name in contact.keys()):
        contact[name]=phno
        print("contact is updated")
    else:
        print("not found")

