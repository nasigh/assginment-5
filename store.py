PRODUCTS = []
def load_data_from_file():
    f = open('database.csv','r')
    for row in f:
        info = row[:-1].split(',')
        new_dict = {'code' : info[0],'name' : info[1],'price' : info[2],'count' : info[3]}
        PRODUCTS.append(new_dict)
def add():
    print('Enter Code:')
    int_code = int(input())
    print('Enter Name:')
    int_name = input()
    print('Enter Price')
    int_price = int(input())
    print('Enter Count:')
    int_count = int(input())
    add_array = [int_code ,int_name ,int_price ,int_count]
    PRODUCTS.append({'code' : add_array[0],'name' : add_array[1],'price' : add_array[2],'count' : add_array[3]})
def edit():
    print('Enter Name:')
    int_name=input()
    for product in PRODUCTS:
        if int_name == product['name']:
            print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'])
            print('Enter Edit:')
            print('Code:')
            int_code = int(input())
            print('Name:')
            int_name = input()
            print('Price')
            int_price = int(input())
            print('Count:')
            int_count = int(input())
            edit_array=[int_code, int_name, int_price, int_count]
            product['code'] = int_code
            product['name'] = int_name
            product['price'] = int_price
            product['count'] = int_count
            break
def delete ():
    print('Enter Name:')
    int_name=input()
    for product in PRODUCTS:
        if int_name == product['name']:
            print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'])
            print('Delete Or NO?(y,n)')
            answer = input()
            while answer !='y' and answer != 'n':
                print('try again')
                answer = input()
            if answer =='y':
                PRODUCTS.remove(product)
                print('Deleted')
            elif answer =='n':
                break
def show_list():
    print("id\tname\tprice\tcount")
    for product in PRODUCTS:
        print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'],'\t')
def search():
    print('Enter Name:')
    int_name = input()
    for product in PRODUCTS:
        if int_name == product['name']:
            print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'])
            break
def buy():
    print('Enter Item Name:')
    int_name=input()
    for product in PRODUCTS:
        if int_name == product['name']:
            print(product['code'],'\t',product['name'],'\t',product['price'],'\t',product['count'])
            print('Buy Or No?(y,n)')
            answer = input()
            if answer=='y':
                print('Enter Count:')
                int_count = int(input())
                while int_count > int(product['count']):
                    print('Wrong...Try Again')
                    int_count = int(input())
                if int_count <= int(product['count']):
                    count_list = int(product['count'])
                    count_list = count_list - int_count
                    product['count'] = srt(count_list)
                    print('Successed')
            elif answer=='n':
                print('Exited')
                break
            break
def save():
    f=open('database.csv','w')
    for element in PRODUCTS:
        f.write(element + "\n")
    f.close()
def show_menu():
    print("Welcome To Sadjad Store")
    print("1_Add")
    print("2_Edit")
    print("3_Delete")
    print("4_show list")
    print("5_search")
    print("6_buy")
    print("7_save")
load_data_from_file()
while True:
    show_menu()
    choice = int(input("Enter Your Choice :"))
    if choice==1:
        add();
    elif choice == 2:
        edit()
    elif choice == 3:
        delete()
    elif choice ==4:
        show_list()
    elif choice ==5:
        search()
    elif choice == 6:
        buy()
    elif choice == 7:
        save()