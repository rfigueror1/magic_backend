def flatten_array(arr):
    """
    :param arr:
    :return: arr(flattened)
    """
    for i in range(len(arr)):
        if type(arr[i]) == list:
            arr = arr[:i] + flatten_array(arr[i]) + arr[i+1:]
    return arr
