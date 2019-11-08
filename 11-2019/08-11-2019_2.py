from gen_prime_nums import generate_prime_numbers

gen = generate_prime_numbers()

for i in gen:
    if i > 100:
        break
    print(i)