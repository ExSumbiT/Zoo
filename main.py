from input import parse, print_info, check_area, add_new_one, place_corral


if __name__ == '__main__':  # main function
    # CN = parse(input('Enter list of animals:'))  # enter animal list from keyboard
    CN = parse(open('animals.txt', 'r').read())  # read animal list from file "animals.txt"

    place_corral(CN)  # set corrals from animal list
    print(f'Corral needed: {len(set(CN))}')  # how many corrals are needed
    print_info()  # print to console info about animal and corral

    # checks whether it is possible to accommodate all newly arrived animals
    check_area(open('new_animals.txt', 'r').read())  # read animal list from file "new_animals.txt"

    while 1:  # the user alternately accommodates each newly arrived animal
        info = input("Enter 'e' for exit\nEnter animal kind and corral id(lion,1):")
        if info == 'e':
            break
        add_new_one(info.split(',')[0], int(info.split(',')[1]))
    print_info()  # print to console info about animal and corral
