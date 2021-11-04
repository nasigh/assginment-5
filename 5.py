from os import linesep
def show_menu():
    print(" 1.add ")
    print(" 2.delete ")
    print(" 3.edit ")
kala=[]
def load_data_from_datastore():
    f = open('datastore.csv', 'r')
    for line in f:
        info = line[:-1].split(',')
        new_dict = {'id': info[0], 'Name': info[1], 'Price': info[2], 'Stock': info[3]}
        kala.append(new_dict) 
def add(): 
    while(True):
        c=True
        if c==True:
            new_kala={'id':int(input("id")),'Name':input("name"),'Price':int(input("price")),'Stock':int(input("tedad"))}
            if new_kala not in kala :
                kala.append(new_kala)
            else:
                print("kala mojod ast.")
        c=False
        tekrar=(input("kalaye digari mikhahid vared kkonid (y/n) :"))
        if tekrar=="n":
            break
        elif tekrar=="y":
            c=True
        else :
            print("wrong")
            break
def show_List():
    print('id  ,  Name  ,  Price  ,  Stock')
    for product in kala:
        print(product['id'], '  ', product['Name'], '  ', product['Price'], '  ', product['Stock'])
def delete():
    show_List()
    x=int(input("id"))
    for kal in kala:
        if kal['id']==x:
            kala.remove(kal)
def edit():
    show_List()
    x=int(input())
    for kal in kala:
        if kal['id']==x:

            kal['Name']=input('enter your Name :')
            kal['Price']=input('enter your Price :')
            kal['Stock']=input('enter your Stock :')
while True:
    show_menu()
    choice = int (input("please choose from menu : \n"))
    load_data_from_datastore()
    if choice == 1:
        add()
    elif choice == 2:
        delete()
    elif choice == 3:
        edit()