#Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true(elements):
    return all(elements)

# Example usage
tuple_example = (False, True, True, True)
result = all_true(tuple_example)

print(f"All elements in the tuple are true: {result}")
