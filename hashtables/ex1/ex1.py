
# key (index) value (weight)


def get_indices_of_item_weights(weights, length, limit):

    # Create a hastable to base on the weights, and length provided
    weight_dict = { index : weight for index, weight in zip(weights, range(0, length - 1))}

    # Loop through all weights
    for index in range(0, length-1):
        # Grab the weight at the index
        cur_weight = weights[index]
        # Get the value for the difference of the current weight and the limit
        diff_weight = limit - cur_weight
        # Check if the hashtable contains the difference
        if diff_weight in weight_dict:
            # If it is in the list, grab the index of the second number
            index2 = weight_dict[diff_weight]
            #  compare the two indices
            if index > index2:
                return (index, index2)
            else:
                return (index2, index)
    return None

