from input import Animal, Corral, Zoo, Obj_list


def min_area(animal: Animal):  # function to calculate corral area
    animal.corral.area = (animal.counter * animal.personal_area)  # calculate corral area for animal
    Zoo.free_space -= animal.corral.area  # calculate free space
    if Zoo.free_space <= 0:
        Zoo.free_space = 0
        return False
    return True


def max_area():
    for animal in Obj_list:
        animal_corral = Corral(animal)  # create Corral object for Animal object
        animal.corral = animal_corral
        animal.max_area = int(Zoo.max_square * validity(animal))


def validity(animal: Animal):
    amount = 0
    for _ in Obj_list:
        amount += _.personal_area
    return animal.personal_area / amount
