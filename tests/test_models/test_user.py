import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_attributes(self):
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))

if __name__ == "__main__":
    unittest.main()
