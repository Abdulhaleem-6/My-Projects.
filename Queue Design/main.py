from Queue import Queue, Person

if __name__ == "__main__":
    print("Hey!")
    q = Queue()
    p1 = Person("Abdul")
    p2 = Person("Haleem")
    p3 = Person("Habib")
    p4 = Person("Abdulwahab")

    q.add_person([p1])
    q.size()
    q.add_person([p2, p3])
    q.size()
    q.remove_person(0)
    q.size()
    q.position(p2)
    print(q.people)

# from main import q, p1, p2, p3, p4

