import unittest
from hero import Hero
from squad import Squad


class MyTestCase(unittest.TestCase):
    def test_hero(self):
        h = Hero("Loki", "Alive", "Evil", 50)
        self.assertContains(h.name, "Loki")
        self.assertContains(h.status, "Alive")
        self.assertContains(h.nature, "Evil")
        self.assresisinstance(h.power, int)

    def test_squad(self):
        s = Squad("Axis", [Hero("Thanos", "Alive", "Evil", 100), Hero("Troll", "Alive", "Evil", 30)],
                  True)
        self.assertContains(s.name, "Axis")
        self.assresisinstance(s.resting, bool)


if __name__ == '__main__':
    unittest.main()
