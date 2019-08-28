def time_planner(a, b, duration):
    new_a = find_range(a)
    new_b = find_range(b)

    for i in new_a:
        for j in i:
            for k in new_b:
                if j in k:
                    time = j + duration
                    if time in (i and k):
                        return [j, time]

    return []


def find_range(arr):
    expand_arr = []
    for i in arr:
        r = []
        for j in range(i[0], i[-1] + 1):
            r.append(j)
        expand_arr.append(r)
    return expand_arr


print(time_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8))
print(time_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 72]], 12))
print(time_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12))
