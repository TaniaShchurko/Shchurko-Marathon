def studying_hours(a):
    number_non_decreasing = 1
    max = 0
    for i in range(1,len(a)):
        if a[i]>=a[i-1]:
            number_non_decreasing += 1
            if number_non_decreasing > max:
                max = number_non_decreasing
        elif a[i] < a[i - 1]:
            number_non_decreasing = 1
    return max