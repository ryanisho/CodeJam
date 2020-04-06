def solve(times):
    times = [(times[i][0], times[i][1], i) for i in range(len(times))]

    times.sort(key=lambda x: x[0])

    result = []

    c_end = 0 
    j_end = 0 

    for start, end, idx in times:
        if start < c_end and start < j_end:
            return "IMPOSSIBLE"
        elif start >= c_end:
            result.append(("C", idx))
            c_end = end
        else: # elif start >= j_end:
            result.append(("J", idx))
            j_end = end

    result.sort(key=lambda x: x[1]) #Sort according to the IDX

    str_result = ''

    for person, idx in result:
        str_result += person

    return str_result


T = int(input().strip())
list_result = []

for i in range(1, T+1):
    n = int(input().strip())

    times = []

    for ni in range(n):
        interval = list(map(int, input().strip().split()))

        times.append(interval)

    result = solve(times)

    list_result.append(result)

for index in range(len(list_result)):
    print("Case #{}: {}".format(index+1, list_result[index]))