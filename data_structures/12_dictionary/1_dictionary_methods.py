"""
Dictionary Methods
"""

class MyDictionary:

    def __init__(self) -> None:
        self.my_dict = {'name': 'Edy', 'age': 26}

    # Insert/Update a dictionary
    def insert(self):
        self.my_dict['address'] = 'London'
        return self.my_dict

    # Traversing through a dictionary
    def traverse(self):
        for key in self.my_dict:
            print(key, self.my_dict[key])
    
    # Search through a dictionary
    def search(self, value):
        for key in self.my_dict:
            if self.my_dict[key] == value:
                return key, value
        return 'The value doesn\'t exist'
    
    # Remove an element from a dictionary
    def remove(self, key):
        self.my_dict.pop(key)

    # Remove the last item
    def remove_last(self):
        self.my_dict.popitem()
        return self.my_dict

    # Remove everything
    def remove_everything(self):
        self.my_dict.clear()
        return self.my_dict

    # Del an element
    def delete(self, key):
        del self.my_dict[key]
        return self.my_dict
    
    # Copy dictionary
    def copy(self):
        this_dict = self.my_dict.copy()
        return this_dict
    
    # Create a dictionary of the same value
    def from_keys(self):
        new_dict = {}.fromkeys([1,2,3], 0)
        return new_dict

    # Obtain a value from key
    def get(self, key):
        return self.my_dict.get(key)
    
    # Items of a dictionary
    def items(self):
        return self.my_dict.items()
    
    # Keys of a dictionary
    def keys(self):
        return self.my_dict.keys()

    # Set default an element
    def set_default(self):
        self.my_dict.setdefault('education', 'master')
        return self.my_dict
    
    # All values of a dictionary
    def values(self):
        return self.my_dict.values()
    
    # Update a dictionary
    def update(self, new_dict):
        self.my_dict.update(new_dict)
        return self.my_dict

    # "in" operator
    def in_operator(self, key):
        found_key = key in self.my_dict.keys()
        found_value = key in self.my_dict.values()
        return self.my_dict
    
    # "for" operator
    def for_operator(self):
        for key in self.my_dict:
            print('key: ', key)
        return self.my_dict
    
    # "all" operator
    def all_operator(self):
        bool_dict = {0: True, 1: False, 2: False}
        all(bool_dict) # False

        new_dict = {}
        all(new_dict) # True

        return self.my_dict

    # "any" operator
    def any_operator(self):
        bool_dict = {0: True, 1: False, 2: False}
        any(bool_dict) # True

        new_dict = {}
        any(new_dict) # False

        return self.my_dict
    
    # "len" operator
    def len_operator(self):
        return len(self.my_dict)
    
    # "sorted" operator
    def sorted_operator(self):
        num_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
        print(sorted(num_dict))

        print(sorted(num_dict, reverse=True))

        new_dict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}
        print(sorted(new_dict, key=len))
        # ['aas', 'udd', 'sse', 'werwi', 'eooooa']
        return self.my_dict
