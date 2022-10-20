import unittest

from Queue import Queue, Person


class QueueTest(unittest.TestCase):
    
    def test_queue_class_starts_out_with_no_person_object(self):
        q = Queue()
        self.assertEqual(
            q.people,
            []
        )

    def test_that_queue_adds_person_object(self):
        q = Queue()
        p = Person("Abdul")
        q.add_person([p])
        
        self.assertEqual(
            q.people,
            [p]
        )

    def test_that_queue_removes_person_object(self):
        q = Queue()
        p = Person("Abdul")
        q.add_person([p])
        q.remove_person(p)

        self.assertEqual(
            q.people,
            []
        )

    def test_queue_gives_its_length(self):
        q = Queue()
        p1 = Person("Abdul")
        p2 = Person("Haleem")
        p3 = Person("Habib")
        q.add_person([p1, p2, p3])

        self.assertEqual(
            len(q),
            3
        )

    def test_queue_gives_has_size_attribute(self):
        q = Queue()
        p1 = Person("Abdul")
        p2 = Person("Haleem")
        p3 = Person("Habib")
        q.add_person([p1, p2, p3])

        self.assertEqual(
            q.size(),
            "There are 3 people on this queue."
        )

    def test_that_queue_inserts_a_person_in_a_particular_position(self):
        q = Queue()
        p1 = Person("Abdul")
        p2 = Person("Haleem")
        p3 = Person("Habib")

        q.add_person([p2, p3])
        q.insert(p1, 2)

        self.assertEqual(
            q.people[1],
            p1
        )

    def test_person_has_position_on_queue(self):
        q = Queue()
        p1 = Person("Abdul")
        p2 = Person("Haleem")
        p3 = Person("Habib")
        q.add_person([p1, p2, p3])

        self.assertEqual(
            q.position(p1),
            1
        )



        