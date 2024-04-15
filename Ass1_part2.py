def student():

    while True:
        x = input('         Student system (l/r/x): ')
        if x == 'l':
            return
        elif x == 'r':
            return
        elif x == 'x':
            return
        else:
            print('Invalid choice, please try again')


def admin():

    while True:
        x = input('         Admin system (c/g/p/r/s/x): ')
        if x == 'c':
            return
        elif x == 'g':
            return
        elif x == 'p':
            return
        elif x == 'r':
            return
        elif x == 's':
            return
        elif x == 'x':
            return
        else:
            print('Invalid choice, please try again')



def main():

    while True:
        x = input('University system: (A)dmin, (S)tudent, or X : ')
        if x == 'X':
            return print('Thank you')
        elif x == 'A':
            return admin()
        elif x == 'S':
            return student()
        else:
            print('Invalid choice, please try again')



if __name__ == '__main__':
    main()


