password = 'a123456'
i = 3 # No. of trial left
while True:
    pwd = input ('Please enter the password:')
    if pwd == password:
        print ('Login successfully')
        break #quit the loop
    else:
        i = i - 1
        print ('Wrong password!', 'No. of trials left:', i,)
    if i == 0:
        break
