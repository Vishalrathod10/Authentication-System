def register():
    db = open("database.txt", 'r')
    username = input('create username : ')
    password = input('create password : ')
    password1 = input('confirm password : ')
    uname = []
    pword = []

    for i in db:
        a,b = i.split(', ')
        b = b.strip()
        uname.append(a)
        pword.append(b)
    data = dict(zip(uname, pword))

    if password1 != password:
        print('password dont match , try again')
        register()
    else:
        if len(password) <= 8 or len(password) >= 16:
            print('password format dont match , try again')
            register()
        elif username in uname:
            print('username already exist, try again')
            register()
        elif password in pword:
            print('password already exist, try again')
            register()
        else:
            db = open("database.txt", 'a')
            db.write(username+', '+password+"\n")
            print("account created successfully")



def access():
    db = open("database.txt", 'r')
    username = input('please enter your username : ')
    password = input('please enter your password : ')

    if not len(username or password) < 1:
        uname = []                              # to check if user is trying to authenticate
        pword = []
        
        for i in db:
            a,b = i.split(', ')
            b = b.strip()
            uname.append(a)
            pword.append(b)
        data = dict(zip(uname, pword))

        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("login successful")
                        print('Hi, ', username)
                        print('how are you, ', username)

                    else:
                        print("username or password incorrect")
                except:
                    print('incorrect password or username')
            else:
                print("username doesn't exist, please register")
        except:
            print('username does not exist, please register')
    else:
        print("please enter the value")


def home(option=None):
    option = input("login | signup :")
    if option == 'login':
        access()
    elif option == 'signup':
        register()
    else:
        print("please enter an option")

home()





                





        
