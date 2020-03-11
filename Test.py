from OpenX_Intership import *
import unittest


posts = json.load(open("posts_test.txt"))
users = json.load(open("users_test.txt"))


class ProgramTest(unittest.TestCase):

    def test_check_url_exists(self):
            url = 'http://google.com/'
            self.assertTrue(check_url_exists(url))

    def test_check_url_not_exists(self):
            url = 'http://google.com/nieistniejacyurl'
            self.assertFalse(check_url_exists(url))   
            
    def test_url_is_not_empty(self):
            url = 'http://google.com/'
            self.assertTrue(url_not_empty(url))
                        
    def test_data(self):
        self.assertEqual(data(users,posts)[2],{'userId': 3, 'id': 3, 'title': 'tytul 3', 'name': 'Anna Graham', 'username': 'User 3', 'address': {'geo': {'lat': '-60', 'lng': '-50'}}})

    def test_number_of_posts(self):
        self.assertEqual(number_of_posts(users,posts)[2],"User 3 napisal(a) 2 postow")
        self.assertEqual(number_of_posts(users,posts)[0],"Bret napisal(a) 1 postow")

    def test_unique_posts(self):
        self.assertEqual(unique_posts(posts),[['tytul 2'], 2])

    def test_users_distance(self):
        self.assertEqual(users_distance(users)[0],"Najblizej Patrick Graham ----> Ervin Howell  (110.45361017187261)")
        self.assertEqual(users_distance(users)[1],"Najblizej Ervin Howell ----> Anna Graham  (28.284271247461902)")
        self.assertEqual(users_distance(users)[2],"Najblizej Anna Graham ----> Ervin Howell  (28.284271247461902)")


if __name__ == '__main__':
    unittest.main()
        
