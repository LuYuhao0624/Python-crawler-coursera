import re

summation = 0

with open('regex_sum_272790.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        num_list = re.findall('[0-9]+', line)
        for num in num_list:
            summation += int(num)

print(summation)