
def register_username():
    username = input('Select username: ')
    available = check_username_availability(username + '\n')
    if available == True:
        register_username()
        return
    file1 = open('credentials.txt','a')
    file1.write(username + '\n')
    file1.close()
    register_password()
def register_password():
    password = input('Select password: ')
    if password != input('Reenter password for verification: '):
        password = ''
        register_password()
        return
    file1 = open('credentials.txt','a')
    file1.write(password + '\n')
    file1.close()
def check_username_availability(username):
    file1 = open('credentials.txt','r')
    current_usernames = file1.readlines()
    file1.close()
    i = 0
    for usernames in current_usernames:
        i += 1
        if i % 2 == 0:
            continue
        if username == usernames:
            print('Username is already taken. Please select a different username.')
            return True
    return False
def login(username, password):
    file1 = open('credentials.txt', 'r')
    credentials = file1.readlines()
    file1.close()
    current_username = False
    i = 0
    for credential in credentials:
        i += 1
        if i % 2 != 0:  #if an odd number line then we know it is a username
            if username == credential:
                current_username = True
            else:
                continue    #not user loging in so skip to next username
        else:
            if current_username == False:
                continue
            else:   #current credential matches password for username given
                if password == credential:
                    return True
                else:
                    return False
    return False

register_or_login = input('Would you like to register a new account or login to an existing account?\n').lower()
if register_or_login == 'register':
    register_username()
elif register_or_login == 'login':
    username = input('Username: ')
    password = input('Password: ')
    valid_login = login(username + '\n', password + '\n')
    if valid_login != True:
        print('INVALD USERNAME OR PASSWORD')
    elif valid_login == True:
        print('LOGIN SUCCESSFUL.\nWelcome!')
