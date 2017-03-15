
def not_use():
    try:
        a = input('number : ')
        a = int(a)
        a += 2
        print(a)
    except TypeError:
        print('TypeError')
    except ValueError:
        print('ValueError')


    def getNumber():
        while True:
            try:
                n = input('number : ')
                n = float(n)
                break
            # except TypeError:
            #     print('TypeError')
            except ValueError:
                print('ValueError')
        return n

    a = getNumber()
    print(a)




a = 3.14
print(int(a))










# a = [1,3,5]
# v = len(a)
#
# try:
#     print(a[v])
# except IndexError:
#     print('IndexError')
