def read_from_database():
    file= open("D:\PythonCourse_FUM\Session6/Database.txt")
    #lines=file.read()
    for line in file:
        product=line.split(",")           # slip my line where ever you see comma" ,".
        #products.append(line)
        product= {"id":product[0], "name":product[1], "price":[2], "count":[3]}
        products.append(product)
        print("Product: ",product)
# each one is a funcion , the user must be able to use any of it        
def show_menu():
    print("1 - add")
    print("2 -edit")
    print("3 - delete")
    print("4 - buy")
    print("5 - show list")
    print("6 - search")
    print("7 - exit")
def add():
    id=input("Enter product id: ")
    name=input("Enter product name: ")
    price=input("Enter product price: ")
    count=input("Enter product count: ")
    product= {"id":id , "name":name , "price": price , "count":count}
    products.append(product)
    print(products)
def edit():
    done=0
    while done ==0:
        user_input_Edit=input("Enter the product id to edit: ")
        for product in range(len(products)):
            if user_input_Edit==product["id"]:
                print(product)
                cat_to_edit=input("Whet category do you want to edit? (1 - name , 2 - price , 3 - count )")
                if cat_to_edit=="1":
                    new_name=input("New name: ")
                    for product in products:
                        if new_name==product["name"]:
                            print("Try a new name")
                        else:
                            product["name"]=new_name
                        done=bool(input("Are you done? 0/1 "))
                        if done==1:
                            print("your changes has been commited. ")
                            print(product)
                            break
                elif cat_to_edit=="2":
                    new_price=float(input("Enter the new preice"))
                    product["price"]=new_price
                    done=bool(input("Are you done? 0/1 "))
                    if done==1:
                        print("your changes has been commited. ")
                        print(product)
                        break
                elif cat_to_edit=="3":
                    new_count=int(input("Enter new count: "))
                    product["count"]=new_count
                    done=bool(input("Are you done? 0/1 "))
                    if done==1:
                        print("your changes has been commited. ")
                        print(product)
                        break
def delete():
    user_key_word=input("Enter a keyword to search: ") 
    for product in products:
        if user_key_word==product["id"] or user_key_word==product["name"]:
            products.remove(product)
            print("The ", product["name"], "was removed")
            break
        else:
            print("Try anothe  id or name: ")
            
def buy():
    while True:
        show_products()
        product_buy=input("Enter the product id or name or cancle")
        if product_buy == "cancle":
            break
        for product in products:
            if product_buy==product["id"] or product_buy==product["name"]:
                count_buy=int(input("Enter the count: "))
                if count_buy<=product["count"] and count_buy>0:
                    product["count"]=product["count"] - count_buy
                    print(count_buy , " Added to the cart!")
                else:
                    print("not enogh item!!!")
                    break
            else: 
                print("Not found")        
def write_to_database():
    file= open("D:\PythonCourse_FUM\Session6/Database.txt") 
    for i in range(len(products)):
        product=[products[i]["id"],products[i]["name"],products[i]["price"],products[i]["count"]]
        for j in range(len(product)):
            if j == 3 :
                list=product[j]
            else:
                list=product[j]+","
            file.write(list)
        file.write("")
        
        
def show_products():
    print("id \t name \t price \t count") 
    for i in range (len(products)):
        print(products[i]["id"],"\t",products[i]["name"],"\t",products[i]["price"],"\t",products[i]["count"])
def search():
    user_key_word=input("Enter a keyword to search: ") 
    for product in products:
        if user_key_word==product["id"] or user_key_word==product["name"]:
            print(product)
            break
    else:
        print("Not found")
def write_to_database():
    pass

products=[] 
read_from_database()
print(products)
  
while True:
      #create a menu as a function inoder for the menu to be portable
    show_menu()
    user_choice = input("Select: ")
    if user_choice=="1":
        add()
    if user_choice=="2":
        edit()
    if user_choice=="3":
        delete()
    if user_choice=="4":
        buy()
    if user_choice=="5":
        show_products()
    if user_choice=="6":
        search()
    if user_choice=="7":
        write_to_database()
        exit()


