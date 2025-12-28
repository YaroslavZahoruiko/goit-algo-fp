from goit_algo_fp.task_1.linked_list import LinkedList


def main() -> None:
    print("=" * 60)
    print("Example: Singly Linked List Operations")
    print("=" * 60)
    print()

    print("1. REVERSE OPERATION")
    print("-" * 60)
    ll1 = LinkedList.from_list([1, 2, 3, 4, 5])
    print(f"Original list: {ll1}")
    ll1.reverse()
    print(f"Reversed list: {ll1}")
    print()

    print("2. SORT OPERATION")
    print("-" * 60)
    ll2 = LinkedList.from_list([64, 34, 25, 12, 22, 11, 90])
    print(f"Original list: {ll2}")
    ll2.sort()
    print(f"Sorted list:   {ll2}")
    print()

    print("3. MERGE SORTED LISTS OPERATION")
    print("-" * 60)
    list1 = LinkedList.from_list([1, 3, 5, 7, 9])
    list2 = LinkedList.from_list([2, 4, 6, 8, 10])
    print(f"First sorted list:  {list1}")
    print(f"Second sorted list: {list2}")
    merged = LinkedList.merge_sorted_lists(list1, list2)
    print(f"Merged sorted list: {merged}")
    print()

    print("4. MERGE LISTS WITH DIFFERENT SIZES")
    print("-" * 60)
    list3 = LinkedList.from_list([10, 20, 30])
    list4 = LinkedList.from_list([5, 15, 25, 35, 45])
    print(f"First list:  {list3}")
    print(f"Second list: {list4}")
    merged2 = LinkedList.merge_sorted_lists(list3, list4)
    print(f"Merged list: {merged2}")
    print()

    print("=" * 60)
    print("All operations completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
