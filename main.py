call_count = 0


def f(x):
    global call_count
    call_count += 1
    return 3*pow(x, 4) - 8*pow(x, 3) + 6*pow(x, 2)


def bisection():
    iter_count = 0
    a = A
    b = B
    while b - a > EPS:
        iter_count += 1
        x_m = (a + b) / 2
        x_1 = a + (b - a) / 4
        x_2 = b - (b - a) / 4
        f_1 = f(x_1)
        f_2 = f(x_2)
        if f_1 < f(x_m):
            b = x_m
            x_m = x_1
        elif f_2 < f(x_m):
            a = x_m
            x_m = x_2
        else:
            a = x_1
            b = x_2
    return x_m, iter_count


A = -1
B = 0.5
EPS = 0.0001
min, iters = bisection()
print("Min X: ", min)
print("Min Y: ", f(min))
print("Количество итераций: ", iters)
print("Количество вызовов функции: ", call_count)


# call_count = 0
#
#
# def f(x):
#     global call_count
#     call_count += 1
#     return 3 * pow(x, 4) - 8 * pow(x, 3) + 6 * pow(x, 2)
#
#
# def bisectionMethod():
#     iter_count = 0
#     a = A
#     b = B
#
#     xm = (a + b) / 2
#     L = b - a
#     fm = f(xm)
#
#     while L > EPS:
#         iter_count += 1
#
#         x1 = a + L / 4
#         x2 = b - L / 4
#
#         f1 = f(x1)
#         f2 = f(x2)
#
#         if f1 < fm:
#             b = xm
#             xm = x1
#         else:
#             if f2 < fm:
#                 a = xm
#                 xm = x2
#             else:
#                 a = x1
#                 b = x2
#         L = b - a
#     return min(x1, min(x2, xm)), iter_count
#
#
# A = -1
# B = 0.5
# EPS = 0.0001
# min, iters = bisectionMethod()
# print("Число итераций: ", iters)
# print("Количество вычислений функции: ", call_count)
# print("Найденное решение (min): ", min)
# print("Значение функции: ", f(min))
