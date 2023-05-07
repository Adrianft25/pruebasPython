class MyEmptyPerson:
    pass



class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" # propiedad publica
        self.__name = name # propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} Está caminando")
        


my_person = Person("Adrián", "Freire")

#print(f"{my_person.name} {my_person.surname}")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_person2 = Person("Pepe", "Fernández", "Pepito")
print(my_person2.full_name)
my_person2.walk()
my_person2.full_name = "John Doe John Smith"
print(my_person2.full_name)
my_person2.full_name = 666
print(my_person2.full_name)