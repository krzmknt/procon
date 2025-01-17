(n, m), a, *b = [[*map(int, line.split())] for line in open(0)]

# no one visited at the day-0
num_of_visitors_until_the_day = [0]

for num_of_visitors in a:
    num_of_visitors_until_the_day.append(
        num_of_visitors_until_the_day[-1] + num_of_visitors
    )

for start_day, end_day in b:
    print(
        num_of_visitors_until_the_day[end_day]
        - num_of_visitors_until_the_day[start_day - 1]
    )
