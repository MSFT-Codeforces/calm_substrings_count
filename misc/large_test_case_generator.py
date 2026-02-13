
import random
import string

def make_cycle(cyc: str, n: int) -> str:
    L = len(cyc)
    return (cyc * (n // L)) + cyc[: n % L]

def make_blocks(n: int, base_size: int = 4000) -> str:
    # Alternating blocks with varying sizes to create many boundaries and run transitions
    parts = []
    total = 0
    chs = ['a', 'b']
    i = 0
    while total < n:
        size = base_size + ((i * 37) % 2000)  # sizes in [base_size, base_size+1999]
        if total + size > n:
            size = n - total
        parts.append(chs[i % 2] * size)
        total += size
        i += 1
    return "".join(parts)

def make_skewed(n: int) -> str:
    # Mostly 'a' with periodic separators
    arr = ['a'] * n
    for i in range(0, n, 50):
        arr[i] = 'b'
    for i in range(0, n, 333):
        arr[i] = 'c'
    return "".join(arr)

def make_alphabet_with_spikes(n: int) -> str:
    base = make_cycle(string.ascii_lowercase, n)
    arr = list(base)
    # Force local repeats / heavier 'a' at regular positions to perturb "max calm" pattern
    for i in range(0, n, 997):
        arr[i] = 'a'
    for i in range(500, n, 1999):
        arr[i] = 'z'
    return "".join(arr)

cases = []

# 1) All equal (min answer), maximum n
n1 = 200000
s1 = "a" * n1
cases.append((n1, s1))

# 2) Alternating two letters (parity/strictness), maximum n
n2 = 200000
s2 = make_cycle("ab", n2)
cases.append((n2, s2))

# 3) 26-letter cycle (near-max calm), maximum n
n3 = 200000
s3 = make_cycle(string.ascii_lowercase, n3)
cases.append((n3, s3))

# 4) Two huge runs (block structure), maximum n
n4 = 200000
s4 = ("a" * (n4 // 2)) + ("b" * (n4 - n4 // 2))
cases.append((n4, s4))

# 5) Highly skewed distribution with periodic separators, maximum n
n5 = 200000
s5 = make_skewed(n5)
cases.append((n5, s5))

# 6) Random large string (stress / average-case), maximum n
n6 = 200000
rng = random.Random(123456)
letters = string.ascii_lowercase
s6 = "".join(rng.choice(letters) for _ in range(n6))
cases.append((n6, s6))

# 7) Three blocks with repeated majority shifts (boundary/prefix off-by-one), maximum n
n7 = 200000
s7 = ("a" * 70000) + ("b" * 60000) + ("a" * 70000)
cases.append((n7, s7))

# 8) Many varying-sized blocks (two-pointer worst-ish patterns), maximum n
n8 = 200000
s8 = make_blocks(n8, base_size=4000)
cases.append((n8, s8))

# 9) Alphabet cycle with forced spikes (perturbed near-max calm), maximum n
n9 = 200000
s9 = make_alphabet_with_spikes(n9)
cases.append((n9, s9))

# 10) Large odd n (parity edge + off-by-one), n = 199999
n10 = 199999
s10 = make_cycle("abcde", n10)
cases.append((n10, s10))

print("Test Cases:")
for i, (n, s) in enumerate(cases, 1):
    print(f"Input {i}:")
    print(n)
    print(s)
    if i != len(cases):
        print()
