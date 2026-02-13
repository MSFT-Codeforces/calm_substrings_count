#include <iostream>
#include <string>
#include <vector>

/**
 * @brief Fenwick Tree (Binary Indexed Tree) supporting point updates and prefix-sum queries.
 */
class FenwickTree {
public:
    /**
     * @brief Creates a Fenwick tree and initializes it to a given size with all zeros.
     *
     * @param treeSize One-based maximum index supported by the tree.
     */
    explicit FenwickTree(int treeSize) {
        resetTree(treeSize);
    }

    /**
     * @brief Resets the tree to a given size and clears all stored values.
     *
     * @param treeSize One-based maximum index supported by the tree.
     */
    void resetTree(int treeSize) {
        this->treeSize = treeSize;
        binaryIndexedTree.assign(treeSize + 1, 0LL);
    }

    /**
     * @brief Adds a value to a single index.
     *
     * @param oneBasedIndex One-based index to update.
     * @param delta Value to add at the index.
     */
    void addValue(int oneBasedIndex, long long delta) {
        while (oneBasedIndex <= treeSize) {
            binaryIndexedTree[oneBasedIndex] += delta;
            oneBasedIndex += oneBasedIndex & -oneBasedIndex;
        }
    }

    /**
     * @brief Computes the prefix sum from index 1 to oneBasedIndex.
     *
     * @param oneBasedIndex One-based index (inclusive).
     * @return Sum of values in range [1..oneBasedIndex].
     */
    long long getPrefixSum(int oneBasedIndex) const {
        long long result = 0;
        while (oneBasedIndex > 0) {
            result += binaryIndexedTree[oneBasedIndex];
            oneBasedIndex -= oneBasedIndex & -oneBasedIndex;
        }
        return result;
    }

private:
    int treeSize = 0;
    std::vector<long long> binaryIndexedTree;
};

/**
 * @brief Reads input, counts calm substrings, and prints the result.
 *
 * @return Exit code 0 on successful execution.
 */
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int stringLength = 0;
    std::string inputString;
    std::cin >> stringLength >> inputString;

    const long long totalSubstrings = 1LL * stringLength * (stringLength + 1) / 2;

    // Prefix sums lie in [-n, n]. Shift them to be valid 1-based Fenwick indices.
    const int prefixSumOffset = stringLength + 2;
    const int fenwickTreeSize = 2 * stringLength + 5;

    FenwickTree fenwickTree(fenwickTreeSize);
    long long totalOverlordSubstrings = 0;

    for (char targetChar = 'a'; targetChar <= 'z'; ++targetChar) {
        fenwickTree.resetTree(fenwickTreeSize);

        int prefixSumValue = 0;
        fenwickTree.addValue(prefixSumValue + prefixSumOffset, 1);

        long long positiveSumSubarrays = 0;

        for (int positionIndex = 0; positionIndex < stringLength; ++positionIndex) {
            prefixSumValue += (inputString[positionIndex] == targetChar) ? 1 : -1;
            const int mappedPrefixSumIndex = prefixSumValue + prefixSumOffset;

            positiveSumSubarrays += fenwickTree.getPrefixSum(mappedPrefixSumIndex - 1);
            fenwickTree.addValue(mappedPrefixSumIndex, 1);
        }

        totalOverlordSubstrings += positiveSumSubarrays;
    }

    const long long calmSubstrings = totalSubstrings - totalOverlordSubstrings;
    std::cout << calmSubstrings << "\n";
    return 0;
}