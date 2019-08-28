def time_planner(a, b, duration):
    new_a = find_range(a)
    new_b = find_range(b)

    


def find_range(arr):
    expand_arr = []
    for i in arr:
        r = []
        for j in range(i[0], i[-1] + 1):
            r.append(j)
        expand_arr.append(r)
    return expand_arr


time_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8)
