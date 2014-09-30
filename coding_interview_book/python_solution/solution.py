"""A module contains the methods (interfaces) to solve the coding puzzles in 
the book of coding interview"""

from linkedlist import LinkedListNode

###chapter 1 Arrays and Strings###

#1.1
def is_unique_chars(string):
    target = string[0]
    for index in range(1, len(string)):
        if string[index] != target:
            return False
    return True

#1.2
#Gotca: string in python is also immutable.
def reverse(string):
    host_list = list()
    for index in range(0, len(string)):
    #Gotca: range() in python is like [0,10).
        host_list.append(string[len(string)-1-index])

    return ''.join(host_list)

#1.3
def is_permutation(string1, string2, method = 'sort'):
    if len(string1) != len(string2):
        return False

    if method == 'sort':
        str1_list = list(string1)
        str2_list = list(string2)
        str1_list.sort()
        #Gotca list has sort method or using sorted() in which,can specify keys.
        str2_list.sort()
        #list.sort() return a None. The list is already the sorted one.
        #sorted(string or iterable ones) return a sorted list.
        if str1_list == str2_list:
            return True
        return False

    if method == 'count':
        check_table = dict()
        count = 1
        for s in string1:
            if check_table.has_key(s):
                check_table[s] += 1
            else:
                check_table.update({s:count})
        for s in string2:
            if check_table.has_key(s):
                check_table[s] -= 1
            else:
                return False
        for item in check_table.values():
            if item != 0:
                return False

        return True

#1.4
def replace_spaces(string):
    #pretty easy in python.
    return string.replace(' ', '%20')

#1.5
#Gotca string concatenation operates in O(n2).
#No stringBuffer in Python.
def compress_string(string):
    result_list = list()
    last = string[0]
    pointer = 1
    count = 1

    for i in range(pointer, len(string)):
        if string[i] == last:
            count += 1
        else:
            result_list.append(last)
            result_list.append(str(count))
            last = string[i]
            count = 1

    result_list.append(last)
    result_list.append(str(count))

    return ''.join(result_list)

#dictionary is not ordered, so this algorithm may give wrong results.
    # result_dict = dict()
    # result_list = list()
    # count = 1
    # for s in string:
    #     print s
    #     if result_dict.has_key(s):
    #         result_dict[s] += 1
    #     else:
    #         result_dict.update({s:count})
    #     print result_dict

    # for k,v in result_dict.iteritems():
    #     result_list.append(k)
    #     result_list.append(str(v))

    # return ''.join(result_list)

#1.6
def function():
    pass

#1.7
#Gotca: need to iterate, one for storing the zero index and the other to updates
#, otherwise, matrix will be set to all 0.
def set_zeros(matrix):
    row_length = len(matrix)
    column_length = len(matrix[0])
    zeros_row_list = list()
    zeros_column_list = list()

    for i in range(0, row_length):
        for j in range(0, column_length):
            if matrix[i][j] == 0:
                zeros_row_list.append(i)
                zeros_column_list.append(j)

    for i in range(0, row_length):
        for j in range(0, column_length):
            if i in zeros_row_list or j in zeros_column_list:
                matrix[i][j] = 0

    return matrix

#1.8
#Requirements: can only use is_substring() for one time.
def is_rotation(string1, string2):
    ext_string = string1 + string1

    def is_substring(str1, str2):
        if str2 in str1:
            return True
        else:
            return False

    if is_substring(ext_string, string2):
        return True
    else:
        return False

###chapter 2 LinkedList###

#2.1
def remove_duplicates(head, followup=False):
    #Using a dict that holds the data
    if not followup:
        temp = head
        previous = None
        check_map = dict()
        while head != None:
            if check_map.has_key(head.data):
                previous.next = head.next
            else:
                check_map.update({head.data:True})

            previous = head# Need a previous node.
            head = head.next

        return temp
    # Without a buffer
    current = head
    temp = head
    while current != None:
        target = current.data
        runner = current 
        # runner can not be a None, so we can just delete runner.next.
        while runner.next != None:
            if runner.next.data == target:
                runner.next = runner.next.next
            runner = runner.next
        current = current.next

    return temp

#2.2
#Hint: Using two runners with k differences. 
def find_the_kth_elem(head, k):
    slow_runner = head
    fast_runner = head

    for i in range(0, k):
        fast_runner = fast_runner.next

    while fast_runner != None:
        temp = slow_runner
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next

    return temp.data

#2.3
#copy the next node data to current data and then delete the next node
def delete_a_node(node):
    if node == None or node.next == None:
        return False

    node.data = node.next.data
    node.next = node.next.next

    return True

#2.4
#Hint: Maitain two linkedlists and then concatenate these two.
#Gotca: pay attentions to "if" and "if else".
def partition_by_x(head, x):
    node_more_head = None
    node_less_tail = None

    while head != None:
        #Update the more linkedlist, append to tail. more_head->...more
        if head.data > x:
            if not node_more_head:
                node_more_head = LinkedListNode(head.data)
                more_head = node_more_head
            else:
                node_more_tail = LinkedListNode(head.data)
                while node_more_head.next != None:
                    node_more_head = node_more_head.next
                node_more_head.next = node_more_tail
                print 'more: %s' % more_head.to_str()
        else:
        #Update the less linkedlist, update the head. less...->less_tail
            if not node_less_tail:
                node_less_tail = LinkedListNode(head.data)
                less_tail = node_less_tail

            else:
                node_less_head = LinkedListNode(head.data)
                node_less_head.next = node_less_tail
                node_less_tail = node_less_head
                print 'less: %s' % node_less_tail.to_str()

        head = head.next
    #concatenat. less...->less_tail->more_head->...more
    less_tail.next = more_head

    return node_less_tail

#2.5
#TODO: finish the followup part later.
def add_two_linkedlist(node1, node2, followup=False):
    #4->2->8->1->9: 91824    4->2->8->1->9: 91824
    #4->2->8->1->9: 91824    4->2->8->1:     1824
    #sum:          183648                   93648

    carry = 0
    result_node = None

    if not followup:
        while node1 != None or node2 != None:
            if node2 == None:
                digit = node1.data + carry
            if node1 == None:
                digit = node2.data + carry
            if node1 != None and node2 != None:
                digit = node1.data + node2.data + carry

            carry = 0 # reset carry

            if digit >= 10:
                digit = digit % 10
                carry = 1

            if result_node == None:
                result_node = LinkedListNode(digit)
            else:
                result_node.append_to_tail(digit)

            if node1 != None:
                node1 = node1.next
            if node2 != None:
                node2 = node2.next

        if carry != 0:
            result_node.append_to_tail(carry)

        return result_node

#2.6
#Hint: using different runners
def find_the_loop_beginning(head):

    #when slower goes into the loop, suppose that s=l, f=l+nx+k, where l is the 
    #distance from beginning of the loop to the head, n is the size of the loop
    #, k is the distances between slower(s) and faster(f).

    #when colliding, s=l+n-k, f=l+nx+k+n-k=(x+1)n+l, which means 
    #it is n-l far away from the beginning.

    #if we reset the s=0, it takes slower l steps to the beginnig if the loop
    #and so does faster.

    slow_runner = head
    fast_runner = head

#the first collision point on loop
    while fast_runner != None or fast_runner.next != None:
        #if fast_runner.next == None, fast_runner.next.next causes error.
        fast_runner = fast_runner.next.next
        slow_runner = slow_runner.next
        if fast_runner == slow_runner:
            break

    if fast_runner == None or fast_runner.next == None:
        return False

#reset slow_runner
    slow_runner = head

#Check the collision
    while slow_runner != fast_runner:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next

    return slow_runner

#2.7
#Hint: Using two runners to find the middle.
def is_palindrome(head):
    slow_runner = head
    fast_runner = head
    stack = list()

    while fast_runner != None and fast_runner.next != None:
        stack.append(slow_runner.data)
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

    if fast_runner != None: # odd, skip the middle.
        slow_runner = slow_runner.next

    while slow_runner != None:
        if slow_runner.data != stack.pop():
            return False
        slow_runner = slow_runner.next

    return True

###chapter 3 Stacks and Queues###

###chapter 4 Trees and Graphs###

###chapter 11 Sorting and Searching###

####Additional Review Problems####

###chapter 17 Moderate###

#17.1
def swap_numbers(a, b):
    print 'a: %s' % a
    print 'b: %s' % b

    a = a - b 
    b = a + b #remebered that a = a - b, so b = a - b + b = a
    a = b - a #remebered that a = a - b and b = a now , so b - a = b

    print 'a: %s' % a
    print 'b: %s' % b

    return (a,b)

#17.2
#Hint: Check the rows columns and two diagonals respectively.
#TODO: still bug, need to be fixed!
def has_won_tic_tac_toe(board):
    row_length = len(board)
    column_length = len(board[0])

    #check rows
    for i in range(0, row_length):
        for j in range(0, column_length):
            if board[i][j] != board[i][i]:
                break # if not, go to next outter loop
            if j == column_length - 1: # check all the items in column
                print 'In %sth rows!' % i
                return True

    #check columns
    for i in range(0, row_length):
        for j in range(0, column_length):
            if board[j][i] != board[i][i]:
                break
            if j == column_length - 1:
                print 'In %sth columns!' % i
                return True


    #check diagonal  
    for i in range(0, row_length):
        for j in range(0, column_length):
            if i == j:
                print i, j
                if board[j][i] != board[0][0]:
                    break
                if j == row_length - 1: # check all the items in diagonal
                    print 'In lower diagonal!'
                    return True

    #check diagonal
    for i in range(0, row_length):
        for j in range(0, column_length):
            if i + j == row_length - 1:
                print i,j
                if board[j][i] != board[row_length-1][0]:
                    return False
                if j == row_length - 1:
                    print 'In upper diagonal!'
                    return True

#17.3
#Hint: count the numbers of 5.
def trailing_zeros(n):
# 2x5 = 10, 2 is in every even, just count numbers of 5.
    def _count_zeros(k, count=0):
        if k % 5 == 0:
            count += 1
            k = k / 5
            return _count_zeros(k, count=count)
        else:
            return count

    zeros_count = 0

    for i in range(1, n+1):
        zeros_count += _count_zeros(i)

        if i % 5 == 0:
            print '%s has %s 5' % (i, _count_zeros(i))

    return zeros_count






###chapter 18 Hard###















































