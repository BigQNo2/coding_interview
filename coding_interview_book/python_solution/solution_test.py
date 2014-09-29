"""Unit test for module solution.
"""


import unittest
import solution

class SolutionTest(unittest.TestCase):

    def setUp(self):

        pass

    def test_is_unique_chars(self):
        self.assertEqual(solution.is_unique_chars('aaaaa'), True)
        self.assertEqual(solution.is_unique_chars('aaaba'), False)

    def test_reverse(self):
        self.assertEqual(solution.reverse('abcde'), 'edcba')

    def test_is_permutation_sort(self):
        self.assertEqual(solution.is_permutation('water','ertaw'), True)
        self.assertEqual(solution.is_permutation('water','ertab'), False)

    def test_is_permutation_count(self):
        self.assertEqual(solution.is_permutation('water','ertaw',
                                                 method='count'), True)
        self.assertEqual(solution.is_permutation('water','ertab',
                                                 method='count'), False)

    def test_replace_spaces(self):
        self.assertEqual(solution.replace_spaces('a b c d '),
                         'a%20b%20c%20d%20')

    def test_replace_spaces(self):
        self.assertEqual(solution.compress_string('abbcccdddd'),
                     'a1b2c3d4')

    def test_rotate_matrix(self):
        pass

    def test_set_zeros(self):
        self.assertEqual(solution.set_zeros([[1,2,0,4],
                                             [2,3,4,0],
                                             [1,2,3,4],
                                             [4,5,6,7]]),
        [[0,0,0,0],
         [0,0,0,0],
         [1,2,0,0],
         [4,5,0,0]
         ])

    def test_is_rotation(self):
        self.assertEqual(solution.is_rotation('waterbottle','erbottlewat'),
                                              True)
        self.assertEqual(solution.is_rotation('waterbottle','erobttlewat'),
                                              False)

if __name__ == '__main__':
    unittest.main()