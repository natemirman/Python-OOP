from tests import test_greetings, test_ages
from datetime import datetime as date


class Person:
    """
    Base class for the Person -> Student -> SoftwareStudent inheritance hierarchy

    attributes:
        name (str): The name of the person
        birth_year (int): The year the person was born
    """

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_greeting(self):
        return "Hello, my name is "+self.name+"."

    def get_age(self):
        return (date.now().year - self.birth_year)

def main():
    """
    Runs tests on the Person class.
    """
    names_list = ["Agatha", "Bert", "Cruella"]
    ages_list = [34, 33, 435]

    person_list = [
        Person(names_list[0], 1989),
        Person(names_list[1], 1990),
        Person(names_list[2], 1588),
    ]

    test_greetings(names_list, person_list)
    test_ages(ages_list, person_list)

    print("All tests passed!")


if __name__ == "__main__":
    main()
