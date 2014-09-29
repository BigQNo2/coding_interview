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
def partition_by_x(head, x):



















