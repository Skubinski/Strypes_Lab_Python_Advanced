from math import sqrt
def finding_roots(a,b,c):
    dis = b*b - 4*a*c

    if dis <= 0:
        return
    x1 = (-b + sqrt(dis)) / 2
    x2 = (-b - sqrt(dis)) / 2

    return f'Roots are x1: {x1}, x2{x2}'


a = int(input())
b = int(input())
c = int(input())

print(finding_roots(a,b,c))