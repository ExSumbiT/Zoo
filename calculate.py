from input import Animal, Corral, Zoo, Obj_list


def min_area(animal: Animal):  # function to calculate corral area
    animal.corral.area = (animal.counter * animal.personal_area)  # calculate minimal area on corral for N animal
    Zoo.free_space -= animal.corral.area  # calculate free space
    if Zoo.free_space <= 0:  # if no free space
        Zoo.free_space = 0
        return False
    return True


def max_area():
    for animal in Obj_list:
        animal_corral = Corral(animal)  # create Corral object for Animal object
        animal.corral = animal_corral  # tie the detachment object to the animal object
        animal.max_area = int(Zoo.max_square * validity(animal))  # calculate recommended area for all animal kind


def validity(animal: Animal):  # returns the coefficient for calculating the recommended area
    amount = 0
    for _ in Obj_list:
        amount += _.personal_area
    return animal.personal_area / amount
