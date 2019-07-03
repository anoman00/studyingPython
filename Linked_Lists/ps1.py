# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

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