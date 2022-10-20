class Queue():
    def __init__(self):
        self.people = []

    def __len__(self):
        return len( self.people )

    def add_person(self, person_list):
        copy = self.people[:]
        copy.extend( person_list )
        self.people = copy

        for p in person_list:
            print(f"{p} added !")

    def remove_person(self, index):
        person = self.people[index]
        del self.people[index]
        print(f"{person} removed !")

    def size(self):
        print(f"There are { len(self.people) } people on this queue.")

    def insert(self, person, position):
        self.people.insert( ( position - 1 ), person )

    def position(self, person):
         print(self.people.index( person ) + 1)
         