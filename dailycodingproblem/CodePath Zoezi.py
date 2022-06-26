# def add_fun(n: int) -> int:
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 2
#     return add_fun(n - 1) + add_fun(n - 2)
#
#
# print(add_fun(6))

# def print_alpha_nums(abc_list, num_list):
#     for char in abc_list:
#         for num in num_list:
#             print(char, num)
#
#     return print_alpha_nums(['a', 'b', 'c'], [1, 2, 3])

# def fizzbuzz(nums):
#     for num in nums:
#         if num % 3 == num % 5 == 0:
#             print('fizzbuzz')
#         elif num % 3 > 0 and num % 5 > 0:
#             print(num)
#         elif num % 5 == 0:
#             print('buzz')
#         elif num % 3 == 0:
#             print('fizz')
#
#
# fizzbuzz([5,3,5,15,2,10])

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        current = prev = 1
        for num in range(1, n):
            temp_current = current
            current = current + prev
            prev = temp_current

        return prev


print(fibonacci(1))
