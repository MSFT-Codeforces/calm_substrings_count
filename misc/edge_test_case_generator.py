
def make_alpha_repeat(n: int) -> str:
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return (alpha * (n // 26 + 1))[:n]

cases = []

# 1) Minimum n (length-1 substring is never calm)
cases.append((1, "a"))

# 2) Small all equal (no calm substrings)
cases.append((2, "aa"))

# 3) Small all distinct
cases.append((2, "ab"))

# 4) Odd-length alternating pattern (many odd substrings have strict majority)
cases.append((3, "aba"))

# 5) Even-length alternating (even windows can be exactly half/half -> calm)
cases.append((4, "abab"))

# 6) Exact half-frequency case (e.g., "aa" and "bb" appear exactly m/2 in "aabb")
cases.append((4, "aabb"))

# 7) Skewed distribution with a single different character in the middle
cases.append((7, "aaabaaa"))

# 8) Blocky / run structure (transitions matter)
cases.append((10, "aaaabbbbcc"))

# 9) Periodic over small alphabet (3 letters)
cases.append((12, "abcabcabcabc"))

# 10) Mixed pattern with varying local majorities
cases.append((13, "abacabadabaca"))

# 11) Full alphabet once (max variety; includes 'z')
alpha = "abcdefghijklmnopqrstuvwxyz"
cases.append((26, alpha))

# 12) Wrap-around repetition to test indexing and frequency updates across repeats
cases.append((27, alpha + "a"))

# Large stress tests
n_big = 200000

# 13) Huge two-block string (worst transitions; many substrings with strong majority)
cases.append((n_big, "a" * (n_big // 2) + "b" * (n_big // 2)))

# 14) Huge all equal (answer should be 0; stress for any non-linear approaches)
cases.append((n_big, "a" * n_big))

# 15) Huge 26-cycle (near-maximum calm substrings; stresses 64-bit accumulation)
cases.append((n_big, make_alpha_repeat(n_big)))

print("Test Cases:")
for i, (n, s) in enumerate(cases, start=1):
    print(f"Input {i}:")
    print(n)
    print(s)
    if i != len(cases):
        print()
