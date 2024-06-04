def is_prime_number(n):

  if n <= 1:
    return False

  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False

  return True


def find_first_n_primes(n):

  count = 0
  num = 2

  while count < n:
    if is_prime_number(num):
      print(num)
      count += 1
    num += 1

print("Prvních 20 prvočísel:")
find_first_n_primes(20)
