def hash_function(key, table_size):
    return key % table_size

def insert_into_table(table, key, table_size):
    index = hash_function(key, table_size)
    
    while table[index] is not None:
        index = (index + 1) % table_size
    
    table[index] = key

def construct_closed_hash_table(keys, table_size):
    table = [None] * table_size
    
    for key in keys:
        insert_into_table(table, key, table_size)
    
    return table

def search_in_table(table, key, table_size):
    index = hash_function(key, table_size)
    comparisons = 1  
    
    while table[index] is not None:
        if table[index] == key:
            return index, comparisons  
        index = (index + 1) % table_size
        comparisons += 1
    
    return None, comparisons  


keys = [30, 20, 56, 75, 31, 19]
table_size = 11


hash_table = construct_closed_hash_table(keys, table_size)


search_key = 56
index_found, comparisons = search_in_table(hash_table, search_key, table_size)


for i, value in enumerate(hash_table):
    print(f"Index {i}: {value}")


if index_found is not None:
    print(f"\nKey {search_key} found at index {index_found} with {comparisons} comparisons.")
else:
    print(f"\nKey {search_key} not found with {comparisons} comparisons.")
