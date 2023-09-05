username = 'universitas'
password = 'pertamina'
kesempatan =1

while(kesempatan < 2):
    username_user = input('Masukan username: ')
    password_user = input('Masukan password :')

    if(username == username_user and password == password_user) :
        print('berhasil')
        break
    else:
        kesempatan-1
        print('kesempatan tersisa{} kali lagi' .format(kesempatan))