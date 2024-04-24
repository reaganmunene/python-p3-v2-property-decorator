APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    # def get_name(self):
    #     return self._name

    @property
    def name (self):
        """the name property"""
        return self._name

    # def set_name(self, name):
    #     if isinstance(name, str) and 1 <= len(name) <= 25:
    #         self._name = name.title()
    #     else:
    #         raise ValueError(
    #             "Name must be string between 1 and 25 characters.")
    @name.setter
    def name(self,name):
        """Name must be a string between 1 and 25 charachters in length"""
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            raise ValueError("Name must be string between 1 and 25 charachters.")


    # name = property(get_name, set_name)

    # def get_breed(self):
    #     return self._breed

    # def set_breed(self, breed):
    #     if breed in APPROVED_BREEDS:
    #         self._breed = breed
    #     else:
    #         raise ValueError("Breed must be in list of approved breeds.")

    # breed = property(get_breed, set_breed)

    @property
    def breed(self, name):
        return self._name

    @breed.setter
    def breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            raise ValueError("Breed must be in the list of approved breeds.")


# ipdb> Dog("Fido", "German shepherd")
