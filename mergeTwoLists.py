class ListNode:
    def __innit__(self, val = 0, next = None):
        self.val = val
        self.next = next


def MergeTwoLists(list1, list2):

    # if one is empthy, check the other one
    if not list1:
        return list2
    if not list2:
        return list1
    
    # starting with the first value

    if list1.val < list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next
    

    # keeping track of where we are in the new list
    current = head


    #looping through both lists

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list.next
        
        current = current.next

    # in case if one list done but we have another full list we can attach it to current dirctly

    if list1:
        current.next = list1
    if list2:
        current.next = list2






