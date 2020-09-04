def intersection(arrays):
  # Find the intersection between multiple lists of integers.
    # Create a hashtable for all the values present
    comparison_dict = {}
    # Create storage for the return results
    result = []

    # Loop through all the arrays
    for array in arrays:
        # Loop through each index in the arrays
        for value in array:
            # Check if the value at the index is in the hashtable
            if value not in comparison_dict:
                # If not, add it, and increment the count
                comparison_dict[value] = 1
            else:
                # If the value is in the hashtable, add to the intersection list
                if value in result:
                    continue
                else:
                    result.append(value)
                
    
                
    # Return the results
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
