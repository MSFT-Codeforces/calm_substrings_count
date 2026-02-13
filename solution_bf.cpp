#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) {
        return 0;
    }
    string s;
    cin >> s;

    long long calmCount = 0;

    // Brute force: enumerate all substrings [l..r] and check calmness by counting frequencies.
    for (int l = 0; l < n; l++) {
        for (int r = l; r < n; r++) {
            int m = r - l + 1;

            vector<int> freq(26, 0);
            for (int i = l; i <= r; i++) {
                freq[s[i] - 'a']++;
            }

            bool isCalm = true;
            // A substring is calm iff no letter occurs strictly more than m/2 times.
            // Avoid floating-point: check 2*freq <= m for every letter.
            for (int c = 0; c < 26; c++) {
                if (2 * freq[c] > m) {
                    isCalm = false;
                    break;
                }
            }

            if (isCalm) {
                calmCount++;
            }
        }
    }

    cout << calmCount << "\n";
    return 0;
}