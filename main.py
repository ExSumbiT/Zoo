from input import parse, print_info, check_area, add_new_one, place_corral


if __name__ == '__main__':
    # CN = parse(input('Enter list of animals:'))
    CN = parse(open('animals.txt', 'r').read())
    place_corral(CN)
    print(f'Corral needed: {len(set(CN))}')
    print_info()
    check_area(open('new_animals.txt', 'r').read())
    while 1:
        info = input("Enter 'e' for exit\nEnter animal kind and corral id(lion,1):")
        if info == 'e':
            break
        add_new_one(info.split(',')[0], int(info.split(',')[1]))
    print_info()
