from tree import create_people

class Person:
    person = []

    def __init__(self, name, born=None, died=None, mom=None, dad=None):
        self.name = name
        self.born = born
        self.died = died
        self.mom = mom
        self.dad = dad
        Person.person.append(self)

    def is_sibling_of(self, other):
        same_mom = self.mom is not None and other.mom is not None and self.mom is other.mom
        same_dad = self.dad is not None and other.dad is not None and self.dad is other.dad
        # Half or full, we don't care
        return same_mom or same_dad

    def print_family_tree(self, prefix="", level=0):
        """Print the family tree starting from this person."""
        indent = "    " * level
        print(f"{prefix}{self.name} {self.born or '?'}-{self.died or '?'}")
        if self.mom:
            self.mom.print_family_tree(f"  {indent}mom: ", level + 1)
        if self.dad:
            self.dad.print_family_tree(f"  {indent}dad: ", level + 1)

    def is_parent_of(self, other):
        """Return if this person is a parent of the other person."""
        return other is not None and (other.mom is self or other.dad is self)

    def is_child_of(self, other):
        """Return if this person is a child of the other person."""
        return other.is_parent_of(self)

    def is_grandparent_of(self, other):
        """Return if this person is a grandparent of another person."""
        return other is not None and (
            (other.mom is not None and self.is_parent_of(other.mom)) or
            (other.dad is not None and self.is_parent_of(other.dad)))

    def known_grandparents(self):
        known_grandparents = []
        if self.mom is not None and self.mom.mom is not None:
            known_grandparents.append(self.mom.mom)
        if self.mom is not None and self.mom.dad is not None:
            known_grandparents.append(self.mom.dad)
        if self.dad is not None and self.dad.mom is not None:
            known_grandparents.append(self.dad.mom)
        if self.dad is not None and self.dad.dad is not None:
            known_grandparents.append(self.dad.dad)
        print("Known Grandparents:")
        for Person in known_grandparents:
            print(Person.name)

    def known_siblings(self):
        known_siblings = []
        print("Known Siblings:")
        for person in Person.person:
            if person.is_sibling_of(self) and person is not self:
                known_siblings.append(person)
        for person in known_siblings:
            print(person.name)

    def first_cousin(self):
        first_cousin = []
        print("First Cousins:")
        for person in Person.person:
            if person.is_sibling_of(self.mom) or person.is_sibling_of(self.dad) and person:
                first_cousin.append(person)
        for person in first_cousin:
            print(person.name)


    def __str__(self):
        span = f"({self.born or '?'}-{self.died or '?'})"
        mom = f"{self.mom.name if self.mom is not None else '?'}"
        dad = f"{self.dad.name if self.dad is not None else '?'}"
        return f"{self.name} {span} mom: {mom}, dad: {dad}"


people = create_people(Person)

print(people["adele"].is_sibling_of(people["joseph"]))  # should be true
print(people["joseph"].is_sibling_of(people["adele"]))  # should be true
print(people["salvatore"].is_sibling_of(people["louise"]))  # should be false

people["adele"].known_siblings()

people["adele"].first_cousin()

"""
ok this isnt working
"""