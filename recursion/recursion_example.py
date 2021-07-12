#recursion: a function call itself
#eg:fibonacci series

# def add():
#     add()


def recur_fibo(n):
    if n<=1:
        return n
    else:
        return recur_fibo(n-1)+recur_fibo(n-2)

nterms=10
print("fibonacci series")
for i in range(nterms):
    print(recur_fibo(i))