from linked_list import LinkedList

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Time Complexity: O(log n)
    """
    if linked_list is None or linked_list.head is None:
        return linked_list, None
    else:
        midpoint = linked_list.size()//2
        mid_node = linked_list.node_at_index(midpoint-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list
    Takes O(n) space
    Runs in O(n) time
    """

    merged = LinkedList()
    merged.add(0) #Fake head
    current = merged.head

    left_head = left.head
    right_head = right.head
    
    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node 
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        current = current.next_node
        
    head = merged.head.next_node
    merged.head = head

    return merged
  
def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    1. Recursively divide the linked list into sublists containing a single node
    2. Repeatedly merge the sublists to produce sorted sublists until one remains
    Returns a sorted linked list

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)
