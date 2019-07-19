# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

'''
Given a singly linked list of integers l and an integer k, 
remove all elements from list l that have a value equal to k.
'''

def removeKFromList(l, k):
    currentNode = l
    if currentNode is None:
        return None
    while currentNode is not None and currentNode.next is not None:
        if currentNode.next.value == k:
            currentNode.next = currentNode.next.next
        else:
            currentNode = currentNode.next
    if l.value == k:
        l = l.next
    if l is None:
        return []
    return l

'''
Finds the length of a linked list
'''
def lenList(l):
    c = l
    count = 0
    while c is not None:
        count += 1
        c = c.next
    return count
def getValue(l,index):
    if l is None:
        return None
    while index > 0:
        l = l.next
        index -= 1
    return l.value

'''
Given a singly linked list of integers, determine whether or not it's a palindrome.
'''

#isListPalindrome11 is the better performing function

def isListPalindrome2(l):
    k = -1
    j = lenList(l) - 1
    while k < (j+1)//2:
        k += 1
        if getValue(l, k) != getValue(l, j-k):
            return False
    return True

def isListPalindrome1(l):
    c = l
    dictionary = {}
    count = 0
    if c is None:
        return True
    while c is not None:
        dictionary[count] = c.value
        count += 1
        c = c.next
    k = -1
    j = count - 1
    while k < (j+1)//2:
        k += 1
        if dictionary[k] != dictionary[j-k]:
            return False
    return True

'''
You're given 2 huge integers represented by linked lists. 
Each linked list element is a number from 0 to 9999 that 
represents a number with exactly 4 digits. The represented 
number might have leading zeros. Your task is to add up 
these huge integers and return the result in the same format.
'''

def addTwoHugeNumbers(a, b):
    # a and b are linked lists
    anumber = ''
    bnumber = ''
    while a is not None:
        astr = str(a.value)
        alen = len(astr)
        zero_count = 4 - alen
        for i in range(zero_count):
            astr = '0' + astr
        anumber = anumber + astr
        a = a.next
    while b is not None:
        bstr = str(b.value)
        blen = len(bstr)
        zero_count = 4 - blen
        for i in range(zero_count):
            bstr = '0' + bstr
        bnumber = bnumber + bstr
        b = b.next
    sum = str(int(anumber)+int(bnumber))
    z = 4 - len(sum) % 4
    if z is not 4:
        for i in range(z):
            sum = '0' + sum
    n = 4
    sum_list = [int(sum[i:i+n]) for i in range(0, len(sum), n)]
    
    # turn list into linked list below
    l = ListNode(sum_list[0])
    nd = l
    for i in range(len(sum_list) - 1):
        nextt = ListNode(sum_list[i+1])
        nd.next = nextt
        nd = nd.next
    return l

'''
Given two singly linked lists sorted in non-decreasing order, 
your task is to merge them. In other words, return a singly 
linked list, also sorted in non-decreasing order, that contains 
the elements from both original lists.
'''

def mergeTwoLinkedLists(l1, l2):
    empty = []
    while l1 is not None or l2 is not None:
        try:
            if l1.value <= l2.value:
                empty.append(l1.value)
                l1 = l1.next
            else:
                empty.append(l2.value)
                l2 = l2.next
        except:
            if l1 is None:
                empty.append(l2.value)
                l2 = l2.next
            elif l2 is None:
                empty.append(l1.value)
                l1 = l1.next
    if empty == []:
        return None
    else:
        node = ListNode(empty[0])
        l =node
        for i in range(len(empty)-1):
            new_node = ListNode(empty[i+1])
            l.next = new_node
            l = l.next
        return node

'''
Given a linked list l, reverse its nodes k at a time and 
return the modified list. k is a positive integer that is 
less than or equal to the length of l. If the number of 
nodes in the linked list is not a multiple of k, then the 
nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes 
themselves can be changed.
'''

def reverseNodesInKGroups(l, k):
    # first flip the first set of k integers and give it a name called `new`
    curr = l
    prev = None
    for i in range(k):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        new = prev
    for i in range(k-1):
        new = new.next
    while curr is not None:
        prevv = None
        count = 0
        # this takes the next k numbers and flips them then turns it into a linked list called `prevv`
        for i in range(k):
            next = curr.next
            curr.next = prevv
            prevv = curr
            curr = next
            count += 1
            if curr is None:
                break
        if count == k:
            # this appends `prevv` to the new linked list only if count is k
            new.next = prevv
            for i in range(count):
                new = new.next
        else:
            # this unflips `prevv` if it's count is less than k
            rev = prevv
            p = None
            for i in range(count):
                nextt = rev.next
                rev.next = p
                p = rev
                rev = nextt
            new.next = p
    return prev

'''
Given a singly linked list of integers l and a non-negative 
integer n, move the last n list nodes to the beginning of 
the linked list.
'''

def rearrangeLastN(l, n):
    c = l
    count = 0
    listt = []
    while c is not None:
        count += 1
        listt.append(c.value)
        c = c.next
    ind = count - n
    new_list = listt[ind:] + listt[:ind]
    if new_list == []:
        return None
    new_link = ListNode(new_list[0])
    nl = new_link
    for i in range(count - 1):
        j = ListNode(new_list[i+1])
        nl.next = j
        nl = nl.next
        
    return new_link

# better solution 
def rearrangeLastN2(l, n):
    if n == 0:
        return l
    front, back = l, l
    for _ in range(n):
        front = front.next
    if not front:
        return l
    while front.next:
        front = front.next
        back = back.next
    out = back.next
    back.next = None
    front.next = l
    return out