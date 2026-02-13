
def main():
    tests = [
        "a",                    # 1) n=1 minimal
        "aa",                   # 2) n=2 all equal
        "ab",                   # 3) n=2 distinct
        "aba",                  # 4) n=3 alternating odd (majority exists)
        "abab",                 # 5) n=4 alternating even (ties possible)
        "ababa",                # 6) n=5 alternating odd (parity sensitivity)
        "aaaaaa",               # 7) longer all equal (answer should be 0)
        "aaabbb",               # 8) two balanced runs
        "aaaabb",               # 9) skewed distribution (one letter dominates locally)
        "aabaaab",              # 10) tricky mixed runs (barely-majority windows)
        "aabbccdd",             # 11) many duplicates but spread across letters
        "abcabcabc",            # 12) periodic (3 letters)
        "abcdefghij",           # 13) high diversity (many substrings calm)
        "zzzzazzzzzz",          # 14) majority letter is 'z', with a single break
        "abcdefghijklmnopqrstuvwxyz",  # 15) 26 distinct letters (high diversity)
    ]

    print("Test Cases:")
    for i, s in enumerate(tests, 1):
        print(f"Input {i}:")
        print(len(s))
        print(s)
        if i != len(tests):
            print()

if __name__ == "__main__":
    main()
