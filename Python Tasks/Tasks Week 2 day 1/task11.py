my_list = [1, 2, 3, 4, 5]
print("Length:", len(my_list))
print("Max:", max(my_list))
print("Min:", min(my_list))
print("Sum:", sum(my_list))

sorted_list = sorted(my_list)
mid = len(sorted_list) // 2
median = (sorted_list[mid] + sorted_list[mid - 1]) / 2 if len(sorted_list) % 2 == 0 else sorted_list[mid]
