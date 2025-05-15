f = open("text.txt", "r")
total = 0

valid_strings = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"  
]

test = ["threthreetwthree", "2one9eightwone"]


for line in f:
    toAdd_Str = "0"
    nums = []

    subStr = ""

    for char in line:

        subStr += char
        for string in valid_strings:
            if string in subStr:
                # line = line.replace(string, str(valid_strings.index(string) + 1))
                nums.append(valid_strings.index(string) + 1)
                subStr = subStr[len(subStr) - 1 : len(subStr)]

        if char.isdigit():
            nums.append(char)

    print(nums)
    if len(nums) == 1:
        toAdd_Str = str(nums[0]) + str(nums[0])
    if len(nums) >= 2:
        toAdd_Str = str(nums[0]) + str(nums[len(nums) - 1])
    total += int(toAdd_Str)

print(total)    
