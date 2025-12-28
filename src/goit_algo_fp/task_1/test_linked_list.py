from goit_algo_fp.task_1.linked_list import LinkedList


def test_reverse():
    """Test the reverse function."""
    print("Testing reverse function...")

    # Test case 1: Normal list
    ll = LinkedList.from_list([1, 2, 3, 4, 5])
    print(f"Original: {ll}")
    ll.reverse()
    print(f"Reversed: {ll}")
    assert ll.to_list() == [5, 4, 3, 2, 1], "Reverse failed!"

    # Test case 2: Single element
    ll2 = LinkedList.from_list([42])
    ll2.reverse()
    assert ll2.to_list() == [42], "Reverse single element failed!"

    # Test case 3: Empty list
    ll3 = LinkedList()
    ll3.reverse()
    assert ll3.to_list() == [], "Reverse empty list failed!"

    print("✓ Reverse function works correctly!\n")


def test_sort():
    """Test the sort function."""
    print("Testing sort function...")

    # Test case 1: Unsorted list
    ll = LinkedList.from_list([4, 2, 7, 1, 3, 6, 5])
    print(f"Original: {ll}")
    ll.sort()
    print(f"Sorted: {ll}")
    assert ll.to_list() == [1, 2, 3, 4, 5, 6, 7], "Sort failed!"

    # Test case 2: Already sorted
    ll2 = LinkedList.from_list([1, 2, 3, 4, 5])
    ll2.sort()
    assert ll2.to_list() == [1, 2, 3, 4, 5], "Sort already sorted list failed!"

    # Test case 3: Reverse order
    ll3 = LinkedList.from_list([5, 4, 3, 2, 1])
    ll3.sort()
    assert ll3.to_list() == [1, 2, 3, 4, 5], "Sort reverse order failed!"

    # Test case 4: Duplicates
    ll4 = LinkedList.from_list([3, 1, 4, 1, 5, 9, 2, 6, 5])
    ll4.sort()
    assert ll4.to_list() == [1, 1, 2, 3, 4, 5, 5, 6, 9], "Sort with duplicates failed!"

    # Test case 5: Single element
    ll5 = LinkedList.from_list([42])
    ll5.sort()
    assert ll5.to_list() == [42], "Sort single element failed!"

    print("✓ Sort function works correctly!\n")


def test_merge_sorted_lists():
    """Test the merge_sorted_lists function."""
    print("Testing merge_sorted_lists function...")

    # Test case 1: Both lists non-empty
    list1 = LinkedList.from_list([1, 3, 5, 7])
    list2 = LinkedList.from_list([2, 4, 6, 8])
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    merged = LinkedList.merge_sorted_lists(list1, list2)
    print(f"Merged: {merged}")
    assert merged.to_list() == [1, 2, 3, 4, 5, 6, 7, 8], "Merge failed!"

    # Test case 2: Different sizes
    list3 = LinkedList.from_list([1, 3, 5])
    list4 = LinkedList.from_list([2, 4, 6, 8, 10])
    merged2 = LinkedList.merge_sorted_lists(list3, list4)
    assert merged2.to_list() == [
        1,
        2,
        3,
        4,
        5,
        6,
        8,
        10,
    ], "Merge different sizes failed!"

    # Test case 3: One empty list
    list5 = LinkedList.from_list([1, 2, 3])
    list6 = LinkedList()
    merged3 = LinkedList.merge_sorted_lists(list5, list6)
    assert merged3.to_list() == [1, 2, 3], "Merge with empty list failed!"

    merged4 = LinkedList.merge_sorted_lists(list6, list5)
    assert merged4.to_list() == [1, 2, 3], "Merge empty list first failed!"

    # Test case 4: Both empty
    list7 = LinkedList()
    list8 = LinkedList()
    merged5 = LinkedList.merge_sorted_lists(list7, list8)
    assert merged5.to_list() == [], "Merge two empty lists failed!"

    # Test case 5: Duplicates
    list9 = LinkedList.from_list([1, 3, 3, 7])
    list10 = LinkedList.from_list([2, 3, 6])
    merged6 = LinkedList.merge_sorted_lists(list9, list10)
    assert merged6.to_list() == [1, 2, 3, 3, 3, 6, 7], "Merge with duplicates failed!"

    print("✓ Merge_sorted_lists function works correctly!\n")


def main():
    """Run all tests."""
    print("=" * 50)
    print("Linked List Implementation Tests")
    print("=" * 50 + "\n")

    test_reverse()
    test_sort()
    test_merge_sorted_lists()

    print("=" * 50)
    print("All tests passed! ✓")
    print("=" * 50)


if __name__ == "__main__":
    main()
