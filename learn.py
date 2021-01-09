import csv
import sys


def main():
    print("""
    
    =-=-=-=-=-= TECHHAMPERS =-=-=-=-=-=
    |........1 - Register             |
    |........2 - Login                |
    |........3 - Management Login     |
    |........4 - Quit                 |
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    """)
    choice = int(input("Enter the number corresponding to your choice:  "))
    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 3:
        manalogin()
    elif choice == 4:
        print("GOODBYE :(")
        sys.exit() 
    else:
        print("Invalid Input. Try Again!")
        main() 
    

def register():
    valid_username = False
    valid_password = False
    print("Welcome to the REGISTRATION PAGE. Here, you can register an account!")

    while valid_username == False:
        newacc = input("Enter your new username! (It must be at least 8 characters long with no spaces, it also needs at least 1 upper case and lowercase character as well as at least 1 number:  ")
        if len(newacc) >= 8 and newacc.isalnum() == True and newacc.isnumeric() == False and newacc.isalpha() == False and newacc.isupper()  != True and newacc.islower() != True:
            
            if " " in newacc:
                print("Uh oh! NO spaces!")
                sys.exit()
            with open("logininfo.txt","r",newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    for field in row:
                        if newacc in field:
                            valid_username = False
                            print("This username has already been taken! Try using another one!")
                            main()
                        else:
                            break
                            
            valid_username = True
            print("You have succesfully registered a new username,",newacc)
                            


        else:
            nope = input("Do you want to exit to the main menu? ('y' to exit and 'n' to stay)")
            if nope == "y":
                main() 
            else:
                donothing = ""         
                print(donothing) 

    while valid_password == False:
        newpass = input("Enter your new password. It needs to be 8 characters or more in length with no spaces and needs to have both uppercase and lowercase. Don't forget at least one number!")
        if len(newpass) >= 8 and newpass.isalnum() == True and newpass.isnumeric() == False and newpass.isalpha() == False and newpass.isupper()  != True and newpass.islower() != True:
            #with open("logininfo.txt","r",newline="") as f:
                #reader = csv.reader(f)
                #for row in reader:
                    #for field in row:
                        #if newpass in field:
                            #valid_password= False
                            #print("This Password is already in use!")
            
            print("You have succesfully registered a new password,",newpass)
            valid_password = True

        else:
            print("Uh oh. Something went wrong, make sure you met all the criteria.")
            nope = input("Do you want to exit to the main menu? ('y' to exit and 'n' to stay)")
            if nope == "y":
                main()
            else:
                pass

    with open("logininfo.txt","a",newline="") as fa:
        writer = csv.writer(fa)
        writer.writerow([newacc,newpass])
    

def login():
    verifylist = []
    print("""    
    =-=-=-=-=-= TECHHAMPERS =-=-=-=-=-=
    |    Welcome to the Login Page    |
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    """)
    print("")
    favtech = input("What is your favourite tech?   ")
    loginacc = input("Please enter your username here:  ")
    with open("logininfo.txt","r",newline="") as fa:
        reader = csv.reader(fa)
        for row in reader:
            for field in row:
                if loginacc in field:
                    print("Welcome Back!")
                    loginpass = input("Please enter your password here:  ")
                    with open("logininfo.txt","r",newline = "") as fb:
                        reader = csv.reader(fb)
                        for row in reader:
                            if row[0] == loginacc and row[1] == loginpass:
                                print("You are succesfully logged in!")
                                order(loginacc)
`

def order(loginacc):
    deli = input("Would you like to order a hamper? (y/n):   ").upper()
    if deli == "Y":
        numero = int(input("How many Hampers would you like to order?   "))
        address = input("Enter the address you would like to deliver the hamper to!")

    elif deli == "N":
        main() 
    with open("deliveryinfo.txt","a",newline = "") as fa:
        writer = csv.writer(fa)
        writer.writerow([loginacc,numero,address])
        print("order placed succesfully!")
    main()
        
        

def manalogin():
    username = "management"
    password = "manage123"
    manalgin = input("Enter the Management Username:    ")
    if manalgin == username:
        manapass = input("Enter the Management Password:    ")
        if manapass == password:
            print("Logged In")
            devtools()
        else:
            print("Try Again!")
            main() 
    else:
        print("Incorrect Username!")
        main() 


def devtools():
    print("Welcome to the GOD COMMAND!")
    print("""
    =-=-=-=-=-= TECHHAMPERS =-=-=-=-=-=
    |    Welcome to the Admin Page    |
    |    You Have Four Options:       |
    |  ...1 - View all customer info  |
    |  ...2 - Delete customer record  |
    |  ...3 - Delete delivery info    |
    |  ...4 - Edit delivery info      |
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    """)
    godhand = int(input("Enter the number corresponding to your choice of action:   "))
    if godhand == 1:
        with open("deliveryinfo.txt","r",newline = "") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                with open("logininfo.txt","r",newline = "") as fa:
                    reader = csv.reader(fa)
                    for row in reader:
                        print(row)

    if godhand == 2:
        updatedlist=[]
        with open("logininfo.txt",newline="") as f:
            reader=csv.reader(f)
            username=input("Enter the username of the user you wish to remove from file:")
            for row in reader: 
                if row[0]!=username: #as long as the username is not in the row .......
                    updatedlist.append(row) #add each row, line by line, into a list called 'udpatedlist'
        print(updatedlist)
        updatefile(updatedlist)
    
    if godhand == 3:
        updateddeli=[]
        with open("deliveryinfo.txt",newline="") as f:
            reader=csv.reader(f)
            username=input("Enter the username of the user you wish to remove from file:")
            for row in reader: 
                if row[0]!=username: #as long as the username is not in the row .......
                    updateddeli.append(row) #add each row, line by line, into a list called 'udpatedlist'
        print(updateddeli)
        updatfile(updateddeli)    

    if godhand == 4:

        editedlist=[]
        tempolist=[]

        with open("deliveryinfo.txt",newline="") as f:
          reader=list(csv.reader(f))
          print("CHANGE ADDRESS?:  ")
          username=input("Enter the username for the required user:")
          tempolist=reader 

          for row in reader: 
              for field in row:
                    if field==username: 
                        editedlist.append(row) 
                        newaddress=input("Enter new address:   ")
                        editedlist[0][2] = newaddress 

    def updatepassword(editedlist,tempolist):
        for index, row in enumerate(tempolist):
            for field in row:
                if field==editedlist[0]:
                    tempolist[index]=editedlist 
        
    updatepassword(editedlist,tempolist)




    with open("deliveryinfo.txt","w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(tempolist)
        print("File has been updated")

    
        
def updatefile(updatedlist):
    with open("logininfo.txt","w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(updatedlist)
        print("File has been updated")

def updatfile(updateddeli):
    with open("logininfo.txt","w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(updateddeli)
        print("File has been updated")

main()
