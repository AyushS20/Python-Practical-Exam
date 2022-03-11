# Part (a): Sum of First Odd Numbers
def odd_sum():
    sum = 0
    n = int(input("Enter the Number:   "))
    for i in range (0, n + 1):
        if i % 2 == 1:
            sum += i
            print("term = ", i, ", sum till this step =", sum)
        else:
            continue
odd_sum()

# Part (b): Sum of first even numbers 
def even_sum():
    sum = 0
    n = int(input("Enter the Number:   "))
    for i in range (0, n + 1):
        if i % 2 == 0:
            sum += i
            print("term = ", i, ", sum till this step =", sum)
        else:
            continue
even_sum()

# Part (c): sum of Series
def sumodd(n):
    return (n * n)

def sumeven(n):
    return (n * (n + 1))

def findSum(num):
        sumo = 0
        sume = 0
        x = 1
        cur = 0
        ans = 0
        while (num > 0):
            inc = min(x, num)
            num -= inc
            if (cur == 0):
                ans = ans + sumodd(sumo + inc) - sumodd(sumo)
                sumo += inc
            else:
                ans = ans + sumeven(sume + inc) - sumeven(sume)
                sume += inc
            x *= 2
            cur ^= 1
        return ans
findSum(num = int(input("Enter:  ")))
