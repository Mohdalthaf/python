def print_dictionary_items(dictionary):
    for key, value in dictionary.items():
        print(key, ":", value)


student = {
    "name": "Althaf",
    "age": 23,
    "grade": "A",
    "city": "Ernakulam"
}

print("Dictionary items:")
print_dictionary_items(student)
