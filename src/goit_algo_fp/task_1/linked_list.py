class Node:
    """Node of a singly linked list."""

    def __init__(self, data):
        """Initialize a node with data and None as next reference."""
        self.data = data
        self.next = None

    def __repr__(self):
        """String representation of the node."""
        return f"Node({self.data})"


class LinkedList:
    """Singly linked list implementation."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def append(self, data):
        """Add a node with data to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a node with data to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        """Convert linked list to Python list."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    @classmethod
    def from_list(cls, data_list):
        """Create a linked list from a Python list."""
        linked_list = cls()
        for item in data_list:
            linked_list.append(item)
        return linked_list

    def __repr__(self):
        """String representation of the linked list."""
        return " -> ".join(str(item) for item in self.to_list()) + " -> None"

    def reverse(self):
        """
        Reverse the linked list by changing references between nodes.

        This method modifies the list in-place by reversing the links.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        prev = None
        current = self.head

        while current is not None:
            # Store the next node
            next_node = current.next
            # Reverse the link
            current.next = prev
            # Move pointers forward
            prev = current
            current = next_node

        # Update head to point to the new first node
        self.head = prev

    def sort(self):
        """
        Sort the linked list using merge sort algorithm.

        This method sorts the list in-place.
        Time complexity: O(n log n)
        Space complexity: O(log n) due to recursion
        """
        if self.head is None or self.head.next is None:
            # Empty list or single node is already sorted
            return

        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        """
        Recursively sort a linked list using merge sort.

        Args:
            head: Head node of the list to sort

        Returns:
            Head node of the sorted list
        """
        # Base case: empty list or single node
        if head is None or head.next is None:
            return head

        # Split the list into two halves
        mid = self._get_middle(head)
        right_head = mid.next
        mid.next = None  # Break the link

        # Recursively sort both halves
        left_sorted = self._merge_sort(head)
        right_sorted = self._merge_sort(right_head)

        # Merge the sorted halves
        return self._merge_sorted_lists(left_sorted, right_sorted)

    def _get_middle(self, head):
        """
        Find the middle node of a linked list using slow/fast pointer technique.

        Args:
            head: Head node of the list

        Returns:
            Middle node of the list
        """
        if head is None:
            return head

        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    @staticmethod
    def _merge_sorted_lists(left_head, right_head):
        """
        Merge two sorted linked lists into one sorted list.

        Args:
            left_head: Head node of the first sorted list
            right_head: Head node of the second sorted list

        Returns:
            Head node of the merged sorted list

        Note: This is a static method used internally by merge_sort.
        """
        # Create a dummy node to simplify merging
        dummy = Node(0)
        tail = dummy

        # Merge while both lists have nodes
        while left_head is not None and right_head is not None:
            if left_head.data <= right_head.data:
                tail.next = left_head
                left_head = left_head.next
            else:
                tail.next = right_head
                right_head = right_head.next
            tail = tail.next

        # Attach remaining nodes
        if left_head is not None:
            tail.next = left_head
        else:
            tail.next = right_head

        return dummy.next

    @staticmethod
    def merge_sorted_lists(list1, list2):
        """
        Merge two sorted linked lists into one sorted list.

        This is a static method that takes two LinkedList instances and returns
        a new merged sorted list. The original lists are not modified.

        Args:
            list1: First sorted linked list
            list2: Second sorted linked list

        Returns:
            New LinkedList containing merged sorted elements

        Time complexity: O(n + m) where n and m are the lengths of the lists
        Space complexity: O(n + m) for the new list
        """
        # Handle empty lists
        if list1.head is None:
            result = LinkedList()
            current = list2.head
            while current is not None:
                result.append(current.data)
                current = current.next
            return result

        if list2.head is None:
            result = LinkedList()
            current = list1.head
            while current is not None:
                result.append(current.data)
                current = current.next
            return result

        # Merge the two lists
        merged_head = LinkedList._merge_sorted_lists(list1.head, list2.head)

        # Create a new LinkedList from the merged head
        result = LinkedList()
        result.head = merged_head
        return result
