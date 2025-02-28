def sum_of_numbers(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    else:
        return "All arguments must be numeric"


def filter_dict_by_threshold(data, **kwargs):
    threshold = kwargs.get('threshold', 0)  # Default threshold is 0 if not provided
    
    if not isinstance(data, dict):
        return "The first argument must be a dictionary"
    
    # Filters the dictionary based on the threshold and storing the result
    filtered_data = {k: v for k, v in data.items() if v > threshold}
    
    return filtered_data


# Example usage provided by ChatGPT
if __name__ == "__main__":
    print(sum_of_numbers(1, 2, 3, 4.5))  # 10.5
    print(sum_of_numbers(1, '2', 3))  # "All arguments must be numeric"

    sample_data = {
        'a': 5,
        'b': 2,
        'c': 8,
        'd': 1,
    }
    
    filtered_data = filter_dict_by_threshold(sample_data, threshold=3)
    
    # Prints individual values from the filtered dictionary
    if isinstance(filtered_data, dict):  # Only prints if the return is a dictionary
        for key, value in filtered_data.items():
            print(f"{key}: {value}")
    else:
        print(filtered_data)
    
    filtered_data_high = filter_dict_by_threshold(sample_data, threshold=10)
    
    # Prints individual values from the second filtered dictionary
    if isinstance(filtered_data_high, dict):
        for key, value in filtered_data_high.items():
            print(f"{key}: {value}")
    else:
        print(filtered_data_high)