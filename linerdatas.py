# QUESTION 1
def find_pairs(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
            
    return pairs

arr = input("Enter a list of integers, separated by spaces: ").split()
arr = [int(x) for x in arr]
target_sum = int(input("Enter a target sum: "))

result = find_pairs(arr, target_sum)
print(result)



# QUESTION 2
def reverse_array(arr):
    start_index = 0
    end_index = len(arr) - 1
    while end_index > start_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index += 1
        end_index -= 1

arr = [ 1,2,3,4,5]
reverse_array(arr)
print(arr)
