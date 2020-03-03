# tortoise and hare algorithm ( find 1 duplicate)

def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

stuff = []
for i in range(1,999999):
    stuff.append(i)

stuff.append(990000)


print(findDuplicate(stuff))

var = 990000
if var in stuff:
    stuff.remove(var) 
    if var in stuff:
        print(var)