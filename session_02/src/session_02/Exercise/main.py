def sum_of_numbers(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    else:
        return "All arguments must be numeric"


def filter_dict_by_threshold(data, **kwargs):
    threshold = kwargs.get('threshold', 0)  # Default threshold is 0 if not provided
    
    if not isinstance(data, dict):
        return "The first argument must be a dictionary"
    
    return {k: v for k, v in data.items() if v > threshold}


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
    print(filter_dict_by_threshold(sample_data, threshold=3))  # {'a': 5, 'c': 8}
    print(filter_dict_by_threshold(sample_data, threshold=10))  # {}