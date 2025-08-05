def calculate_mean(data):
    if len(data) == 0:
        return 0
    total = sum(data)
    mean = total / len(data)
    return mean
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        mid_left = sorted_data[n // 2-1]
        mid_right = sorted_data[n // 2]
        median = (mid_left + mid_right) / 2
    else:
        median = sorted_data[n // 2]
        return median
data = [5, 2, 1, 7, 9, 3, 6]
mean = calculate_mean(data)
median = calculate_median(data)
print("Mean:", mean)
print("Median:", median)