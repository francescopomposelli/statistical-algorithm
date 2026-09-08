import math


def variance(data):
    mean = sum(data) / len(data)
    deviations = [n - mean for n in data]
    squared_deviations = [n ** 2 for n in deviations]
    var = sum(squared_deviations) / len(squared_deviations)  
    return var


def standard_deviations(data):
    var_calc = variance(data)
    std_dev = math.sqrt(var_calc)
    return std_dev


def quartiles(data):
    data.sort()
    n = len(data)
    if n % 2 == 0:
        lower_half = data[:n // 2]
        upper_half = data[n // 2:]
    else:
        lower_half = data[:n // 2]
        upper_half = data[n // 2 + 1:]
    if len(lower_half) % 2 == 0:
        q1 = (lower_half[len(lower_half) // 2 - 1] + lower_half[len(lower_half) // 2]) / 2
    else:
        q1 = lower_half[len(lower_half) // 2]
    if len(data) % 2 == 0:
        q2 = (data[len(data) // 2 -1] + data[len(data) // 2]) / 2
    else:
        q2 = data[len(data) // 2]
    if len(upper_half) % 2 == 0:
        q3 = (upper_half[len(upper_half) // 2 - 1] + upper_half[len(upper_half) // 2]) / 2
    else:
        q3 = upper_half[len(upper_half) // 2]
    return q1, q2 ,q3


def iqr(data):
    q1, _, q3 = quartiles(data)
    interquartile_range = q3 - q1
    return interquartile_range


def percentile(data, p):
    data.sort()
    position = (p / 100) * (len(data) - 1)
    low = int(position)
    high = low + 1
    if high >= len(data):
        return data[low]
    fraction = position - low
    return data[low] + fraction * (data[high] - data[low])


def outliers(data):
    q1, _, q3 = quartiles(data)
    interquartile_range = q3 - q1
    lower_bound = q1 - 1.5 * interquartile_range
    upper_bound = q3 + 1.5 * interquartile_range
    return [n for n in data if n < lower_bound or n > upper_bound]


def covariance(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    return sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))) / len(x)


def pearson_correlation(x, y):
    cov = covariance(x,y)
    std_x = standard_deviations(x)
    std_y = standard_deviations(y)
    return cov / (std_x * std_y)


def linear_regression(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    denominator = sum((x[i] - mean_x) ** 2 for i in range(len(x)))
    slope = numerator / denominator
    intercept = mean_y - slope * mean_x
    return slope, intercept


def r_squared(x , y):
    r = pearson_correlation(x,y)
    return r ** 2


def print_results(x , y):
    new_x = float(input("Enter a new x value for prediction: "))
    slope , intercept = linear_regression(x, y)
    predicted_y = slope * new_x + intercept
    cov = covariance(x, y)
    pearson = pearson_correlation(x, y)
    r2 = r_squared(x , y)

    print("Covariance =",cov)
    print("Pearson =",pearson)
    print("R² =", r2)
    print("Prediction for y =", predicted_y)


print("STATISTICAL-ALGORITHM")
while True:
    try:
        x_input = input("Enter the values for variable x: ")
        x = [float(num) for num in x_input.split()]
        y_input = input("Enter the values for variable y: ")
        y = [float(num) for num in y_input.split()]
    except ValueError:
        print("ERROR... YOU MUST ENTER NUMERIC VALUES")
    else:
        if len(x) != len(y):
            print("ERROR: X AND Y must have the same number of values")
        else:
            break

     
print_results(x, y)