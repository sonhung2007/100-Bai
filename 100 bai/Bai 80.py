def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_primes_in_list(L, a):
    prime_list = [x for x in L if is_prime(x)]
    if len(prime_list) < a:
        print("Không có đủ số nguyên tố trong danh sách để tạo ra một list mới có", a, "phần tử.")
        return None
    return prime_list[:a]
L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
a = 5
result_list = find_primes_in_list(L, a)
print("List mới chứa", a, "số nguyên tố từ danh sách L là:", result_list)
