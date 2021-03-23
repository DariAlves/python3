# x = 0
# while x < 10:
#     print("Not there yet, x=" + str(x))
#     x += 1
# print("x=" + str(x))

# def attempts(n):
#     x = 1
#     while x <= n:
#         print("Attempt " + str(x))
#         x += 1
#     print("Done")
    
# attempts(5)

# def count_down(start_number):
#   current = start_number
#   while (current > 0):
#     print(current)
#     current -= 1
#   print("Zero!")

# count_down(3)


def print_range(start, end):
  n = start
  while n <= end:
    print(n)
    n += 1
  print(n)



print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 
