def id_validator(verified_ids, feedback_ids):

# Convert verified_ids and feedback_ids to sets for faster membership checking
    verified_ids_set = set(verified_ids)
    feedback_ids_set = set(feedback_ids)
    
    # Calculate the number of unverified IDs
    unverified_ids = len(feedback_ids_set - verified_ids_set)
    
    # Calculate the percentage of unverified IDs
    total_feedback_ids = len(feedback_ids_set)
    percent_unverified = (unverified_ids / total_feedback_ids) * 100
    
    # Print the results
    print(f'{unverified_ids} of {total_feedback_ids} IDs unverified.')
    print(f'{percent_unverified:.2f}% unverified.')
    
id_validator(verified_ids=['1', '2'], feedback_ids=['1', '2', '3'])

# RUN THIS CELL TO TEST YOUR FUNCTION
import ada_c2_labs as lab

# TEST SCENARIOS:                                   # SHOULD OUTPUT:
print('Test 1:')
ver1, fb1 = lab.lists_gen(8, 20, 15, 15)            # 4 of 15 IDs unverified.
id_validator(ver1, fb1)                             # 26.67% unverified.

print('\nTest 2:')
ver2, fb2 = lab.lists_gen(8, 1000, 900, 600)        # 357 of 900 IDs unverified.
id_validator(ver2, fb2)                             # 39.67% unverified.

print('\nTest 3:')
ver3, fb3 = lab.lists_gen(8, 15000, 14925, 13788)   # 1208 of 14925 IDs unverified.
id_validator(ver3, fb3)                             # 8.09% unverified.