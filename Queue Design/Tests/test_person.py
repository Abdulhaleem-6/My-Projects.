import unittest

from Queue import Queue, Person


class TestPersonClass(unittest.TestCase):
    def test_that_person_object_accepts_a_person(self):
        p = Person(name = "Abdul")
        self.assertEqual(
            p.name,
            "Abdul"
        )

    def test_technical_representation_of_person_object(self):
        p = Person("Abdul")
        self.assertEqual(
            repr(p),
            "Abdul"
        )

