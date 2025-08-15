"""
    A linked list is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence.Think of it like a treasure hunt where each clue (node) tells you where to find the next clue.
"""


class ListNode:
    
    '''
        In summary , you nead a data(value) and a pointer to the next node
    '''
    def __init__(self, val=0, next=None):
        self.val = val      #data/value in this node
        self.next = next    #Pointer to the next node
    
    def __str__(self):
        return f"LinkedList"
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)


node1.next = node2
node2.next = node3
print(node1)

#Traversing through a linked list

def print_list(head):
    """Print all Values in the linked list
    In summary , you need a head and a current which will point to the next node
    """
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    
print_list(node3)

def list_to_linked_list(arr):
    """Convert Python list to linked list
    
    In summary , you need to create a head node and then iterate through the array to create nodes
    
    """
    if not arr: #if not(hing is in) array
        return None
    head = ListNode(arr[0]) #convert the first item in the list into a linked list
    current = head #pointer node
    
    for value in arr[1:]: #begin iteration from the second item of the list
        current.next = ListNode(value) #make the next value of the list become the next node
        current = current.next # move the pointer to the next node
    
    return head #it is returning head because it will start from the first node (forward traversal, meanwhile if I  am wrong correct me)
    

my_list = [1, 2, 3, 4, 5]
linked_list = list_to_linked_list(my_list)
print("\n")
print_list(linked_list)


