def delete_element_by_index(lst, index):
    if index < 0 or index >= len(lst):
        return False
    del lst[index]
    return True


numbers = [5, 2, 8, 10, 3, 7]
print("Original list:", numbers)

index = int(input("Enter the index of the element to delete: "))

if delete_element_by_index(numbers, index):
    print("Element deleted successfully.")
    print("Updated list:", numbers)
else:
    print("Invalid index. Element not deleted.")