class Zoo:

    def __init__(self):
        self.max_square = 340
        self.free_space = self.max_square
        self.corral_count = 0


class Animal:  # class for describing animals

    def __init__(self, kind: str, predator: bool, pa: int):
        self.counter = 0
        self.validity = 0
        self.kind = kind
        self.predator = predator
        self.personal_area = pa
        self.max_area = 0
        self.corral = None

    def __repr__(self):
        return (f'''Corral {self.corral.id}
            Animal: {self.kind}
            Quantity: {self.counter}
            Minimal area: {self.corral.area}m²
            Recommended area: {self.max_area}m²''')


class Corral(Zoo):  # class to describe the corral

    def __init__(self, animal: Animal):
        super().__init__()
        Zoo.corral_count += 1
        self.id = Zoo.corral_count
        self.animal = animal
        self.area = 0


Zoo = Zoo()
Lion = Animal('lion', True, 12)
Monkey = Animal('monkey', False, 2)
Panther = Animal('panther', True, 12)
Lynx = Animal('lynx', True, 10)
Deer = Animal('deer', False, 9)
Roe = Animal('roe', False, 5)
Hare = Animal('hare', False, 1)
Raccoon = Animal('raccoon', False, 1)
Bear = Animal('bear', True, 7)
Crocodile = Animal('crocodile', True, 8)
Horse = Animal('horse', False, 12)
Cheetah = Animal('cheetah', True, 12)
Obj_list = [Lion, Monkey, Panther, Lynx, Deer, Roe, Hare, Raccoon, Bear, Crocodile, Horse, Cheetah]
# list for all animal objects

from calculate import min_area, max_area


def parse(animals: str):  # getting list from string
    return animals.replace(' ', '').lower().split(',')


def place_corral(animal_list: list):  # calculate recommended area, minimal area and corral objects
    max_area()
    for _ in Obj_list:  # iterate list of animal objects to record the number of animals
        _.counter += animal_list.count(f'{_.kind}')
    for animal in Obj_list:  # iterate list of animal objects to calculate corral needed area or all animals
        if animal.counter > 0:
            if not (min_area(animal)):
                print(f"No area to place corral!\nFree area: {Zoo.free_space}")
                break


def print_info():  # print to console info about animal and corral
    for animal in Obj_list:
        if animal.counter > 0:
            print(animal)


def check_area(new_animals: str):  # checks whether it is possible to accommodate all newly arrived animals
    for animal in parse(new_animals):  # iterate list of new animals
        for _ in Obj_list:  # iterate list of animal objects to find needed animal kind and corral id
            if _.kind == animal:
                if add_new_one(animal, _.corral.id):
                    break


def add_new_one(animal: str, corral_id: int):  # puts the animal in the right corral
    for _ in Obj_list:
        if _.kind == animal and _.corral.id == corral_id:  # find animal object and needed corral
            _.counter += 1  # animal count +1
            _.corral.area += _.personal_area  # plus one new animal
            Zoo.free_space -= _.personal_area  # minus zoo free space
            if Zoo.free_space < 0:  # if there is no free space, cancel everything
                Zoo.free_space = -1
                _.counter -= 1
                _.corral.area -= _.personal_area
                Zoo.free_space += _.personal_area
                print(f"No area to place {animal}!")  # and print to console about it
                return False
        if _.kind == animal and _.corral.id != corral_id:  # if you try to settle an animal in another corral
            print(f"You can't settle {animal} here!")
            return False
        else:
            continue
