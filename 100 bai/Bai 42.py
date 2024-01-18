A = int(input("Nhập vào số nguyên dương A: "))
fibonacci_n_1 = 1
fibonacci_n_2 = 1
while True:
    fibonacci_n = fibonacci_n_1 + fibonacci_n_2
    if fibonacci_n > A:
        break
    fibonacci_n_1, fibonacci_n_2 = fibonacci_n_2, fibonacci_n
print(f"Số trong dãy Fibonacci lớn nhất không vượt quá {A} là: {fibonacci_n_2}")
