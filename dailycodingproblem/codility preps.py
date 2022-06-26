# strr = str(487)
# lst = list(map(int, strr.strip()))
# print(sum(lst))

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def case_nines(lst):
#     counter = len(lst)-1
#     carry_over = 0
#     for i in lst[::-1]:
#         if i + 1 == 10:
#             if counter == 0:
#                 lst[counter] = lst[counter] + 1
#             else:
#                 lst[counter] = 0
#             carry_over = 1
#         counter = counter-1
#
#     return lst

# sum of digits of N
#     strr = str(N)
#     lst = list(map(int, strr.strip()))
#     n_sum = sum(lst)
#
#     # special  case
#     if n_sum == 1:
#         return N * 10
#
#     # special case - last digit is zero
#     # if lst[-1] == 0:
#     #     nine_list = case_nines(lst)
#     #     new_lst = [str(int) for int in nine_list]
#     #     new_n = int(''.join(new_lst))
#     #     return new_n
#
#     last_digit = N % 10
#     prev_digit = (N // 10) % 10
#
#     new_prev = prev_digit + 1
#     new_last = last_digit -1
#
#     # convert
#     lst[-1] = new_last
#     lst[-2] = new_prev
#
#     new_lst = [str(int) for int in lst]
#     new_n = int(''.join(new_lst))
#
#     return new_n
#
def solution(N):
    # write your code in Python 3.6

    # sum of digits of N
    strr = str(N)
    lst = list(map(int, strr.strip()))
    n_sum = sum(lst)

    # special  case
    if n_sum == 1:
        return N * 10

    # special case - last digit is zero
    # if lst[-1] == 0:
    #     nine_list = case_nines(lst)
    #     new_lst = [str(int) for int in nine_list]
    #     new_n = int(''.join(new_lst))
    #     return new_n

    last_digit = N % 10
    prev_digit = (N // 10) % 10

    new_prev = prev_digit + 1
    new_last = last_digit -1

    # convert
    lst[-1] = new_last
    lst[-2] = new_prev

    new_lst = [str(int) for int in lst]
    new_n = int(''.join(new_lst))

    return new_n


n = solution(487)

print(n)