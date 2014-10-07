"""Unit test for module solution.
"""

import math
import random
import unittest

from linkedlist import LinkedListNode
import solution


class SolutionTest(unittest.TestCase):

    def setUp(self):
        head = LinkedListNode('a')
        head = head.append_to_tail('b')
        head = head.append_to_tail('b')
        head = head.append_to_tail('c')

        other_head = LinkedListNode(4)
        other_head = other_head.append_to_tail(2)
        other_head = other_head.append_to_tail(8)
        other_head = other_head.append_to_tail(1)
        other_head = other_head.append_to_tail(9)

        another_head = LinkedListNode(4)
        another_head = another_head.append_to_tail(2)
        another_head = another_head.append_to_tail(8)
        another_head = another_head.append_to_tail(1)

        loop0 = LinkedListNode('a')
        loop1 = LinkedListNode(data='b', next=loop0)
        loop2 = LinkedListNode(data='c', next=loop1)
        loop3 = LinkedListNode(data='d', next=loop2)
        loop4 = LinkedListNode(data='e', next=loop3)
        loop5 = LinkedListNode(data='f', next=loop4)
        loop0.next = loop3

        palindrome_odd = LinkedListNode('a')
        palindrome_odd = palindrome_odd.append_to_tail('b')
        palindrome_odd = palindrome_odd.append_to_tail('c')
        palindrome_odd = palindrome_odd.append_to_tail('b')
        palindrome_odd = palindrome_odd.append_to_tail('a')

        palindrome_even = LinkedListNode('a')
        palindrome_even = palindrome_even.append_to_tail('b')
        palindrome_even = palindrome_even.append_to_tail('b')
        palindrome_even = palindrome_even.append_to_tail('a')

        palindrome = LinkedListNode('a')
        palindrome = palindrome.append_to_tail('b')
        palindrome = palindrome.append_to_tail('c')
        palindrome = palindrome.append_to_tail('d')
        palindrome = palindrome.append_to_tail('e')

        self.board = [['x','x','o'],
                      ['o','o','x'],
                      ['x','o','x']]

        self.board_diag = [['x','x','o'],
                           ['o','x','x'],
                           ['x','o','x']]

        self.sequences = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        self.palindrome = palindrome #it's a->b->c->d->e
        self.palindrome_odd = palindrome_odd #it's a->b->c->b->a
        self.palindrome_even = palindrome_even #it's a->b->b->a
        self.loop_head = loop5 #it's f->e->d->c->b->a->d
        self.head = head #it's a->b->b->c
        self.other_head = other_head #it's 4->2->8->1->9
        self.another_head = another_head #it's 4->2->8->1
        self.node = self.head.next.next #it's b. b->c
        self.node_none = self.head.next.next.next #it's c. c->None
        self.words = {'Do': 1, 'Here': 1, 'I': 1, 'a': 2, 'book': 2,
                      'check': 1, 'find': 1, 'for': 1, 'frequencies': 1,
                      'important': 2, 'in': 2, 'is': 1, 'need': 1,
                      'testing': 1, 'the': 2, 'this': 1, 'to': 1,
                      'topics': 1, 'very': 6, 'words': 1}


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

    def test_remove_duplicates(self):
        self.assertEqual(solution.remove_duplicates(self.head).to_str(),'abc')
        self.assertEqual(solution.remove_duplicates(self.head,
                                                    followup=True).to_str(),
                                                    'abc')

    def test_find_the_kth_elem(self):
        self.assertEqual(solution.find_the_kth_elem(self.head, 2),'b')
        self.assertEqual(solution.find_the_kth_elem(self.head, 3),'a')

    def test_delete_a_node(self):
        self.assertEqual(solution.delete_a_node(self.node), True)
        self.assertEqual(solution.delete_a_node(self.node_none), False)
        self.assertEqual(self.head.to_str(),'abc')

    def test_partition(self):
        self.assertEqual(solution.partition_by_x(self.other_head,
                                                 3).to_str(),'12489')

    def test_add_two_linkedlist(self):
        self.assertEqual(solution.add_two_linkedlist(self.other_head,
                                                     self.other_head).to_str(),
                                                     '846381')
        self.assertEqual(solution.add_two_linkedlist(self.other_head,
                                                     self.another_head).to_str(),
                                                     '84639')

    def test_find_the_loop_beginning(self):
        self.assertEqual(solution.find_the_loop_beginning(self.loop_head).data,
                         'd')

    def test_is_palindrome(self):
        self.assertEqual(solution.is_palindrome(self.palindrome_odd), True)
        self.assertEqual(solution.is_palindrome(self.palindrome_even), True)
        self.assertEqual(solution.is_palindrome(self.palindrome), False)

    def test_swap_numbers(self):
        self.assertEqual(solution.swap_numbers(23,46),(46,23))

    def test_has_won_tic_tac_toe(self):
        self.assertEqual(solution.has_won_tic_tac_toe(self.board), False)
        self.assertEqual(solution.has_won_tic_tac_toe(self.board_diag), True)

    def test_trailing_zeros(self):
        self.assertEqual(solution.trailing_zeros(59), 13)

    def test_find_maximum(self):
        self.assertEqual(solution.find_maximum(123, 100), 123)
        self.assertEqual(solution.find_maximum(1234, 10000), 10000)

    def test_game_master(self):
        self.assertEqual(solution.game_master(('R','B','B','B'),
                                              ('B','R','Y','B')),
                                              {'hit': 1, 'pseudo_hit': 3})
        self.assertEqual(solution.game_master(('R','B','G','Y'),
                                              ('R','B','G','Y')),
                                              {'hit': 4, 'pseudo_hit': 0})
        self.assertEqual(solution.game_master(('R','B','G','Y'),
                                              ('Y','G','B','R')),
                                              {'hit': 0, 'pseudo_hit': 4})
        self.assertEqual(solution.game_master(('Y','G','G','Y'),
                                              ('G','G','Y','Y')),
                                              {'hit': 2, 'pseudo_hit': 2})

    def test_find_unsorted_sequences(self):
        self.assertEqual(solution.find_unsorted_sequences(self.sequences),
                        [10,11,7,12,6,7])

    def test_translate_the_number(self):
        self.assertEqual(solution.translate_the_number(1063434),
                         ('One Million,Sixty Three Thousands,'
                           'Four Hundreds Thirty Four.'))
        self.assertEqual(solution.translate_the_number(2111063434),
                 ('Two Billions,One Hundred and Eleven Millions,'
                  'Sixty Three Thousands,Four Hundreds Thirty Four.'))

    def test_the_maximum_sum_sublist(self):
        self.assertEqual(solution.the_maximum_sum_sublist([3, -9, 6, -2, 3]),
                         7)
        self.assertEqual(solution.the_maximum_sum_sublist([-3, -9, -6, -2, -3]),
                         -2)

    def test_find_words_frequencies(self):
        self.assertEqual(solution.find_words_frequencies('book.txt'),
                         self.words)

    def test_rand7(self):
        r7 = solution.rand7()
        N = 10000
        x = list(next(r7) for i in range(N))
        distr = [x.count(i) for i in range(7)]
        expmean = N / 7.0
        expstddev = math.sqrt(N * (1.0/7.0) * (6.0/7.0))
        print '%d TRIALS' % N
        print 'Expected mean: %.1f' % expmean
        print 'Expected standard deviation: %.1f' % expstddev
        print 'DISTRIBUTION:'
        for i in range(7):
            print ('%d: %d   (%+.3f stddevs)'
                   % (i, distr[i], (distr[i] - expmean) / expstddev))

    def test_two_sum(self):
        self.assertEqual(solution.two_sum([1,2,3,4,5,3,0,6], 6),
                                          {(4,0),(3,1),(5,2),(7,6)})

if __name__ == '__main__':
    unittest.main()
