def slices(series, length):
    if not (0 < length <= len(series)):
        raise ValueError("Invalid length")
    return [series[i:i+length] for i in range(len(series)-length+1)]
