##Part 1##

import math
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
result1 = math.prod(part1)
print(result1)

##Part 2##

part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
result2 = sum(part2,0)
print(result2)

##Part 3##

part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
result3 = 0
for num in part3:
    if not num%2:
        result3 += num
print(result3)