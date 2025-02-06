def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # total = 0 -> 4
    print(total)                      # total = 4 -> 13
                                      # total = 13 -> 15
                                      # total = 15 -> 16

result = tally([4, 9, 2, 1])
###########################################################################################################
def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # new_list = [4]       idx = 0
    print(new_list)                    # new_list = [4, 9]    idx = 1
                                       # new_list = [4,9,2]   idx = 2
                                       # new_list = [4,9,2,1] idx = 3

                                       # A new list was created, and the integers from the original list were added to it

result = copy([4, 9, 2, 1])
###########################################################################################################
def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # new_list = [5]        value = 4
    print(new_list)                    # new_list = [5, 10]    value = 9
                                       # new_list = [5,10,3]   value = 2
                                       # new_list = [5,10,3,2] value = 1

result = increment_all([4, 9, 2, 1])

