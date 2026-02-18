Time Limit: **1 seconds**

Memory Limit: **32 MB**

You are given a string $s$ of length $n$ consisting of lowercase English letters. A substring (contiguous segment) of length $m$ is called **calm** if no letter occurs in it **strictly more** than $\frac{m}{2}$ times.

Formally, a substring $t$ of length $m$ is calm if for every letter $x$:
$$
\text{freq}_t(x) \le \frac{m}{2}.
$$

Count the number of calm substrings of $s$.

**Input Format:-**

- The first line contains an integer $n$ $(1 \le n \le 2 \cdot 10^5)$.
- The second line contains a string $s$ of length $n$, consisting of lowercase Latin letters.

**Output Format:-**

Print one integer — the number of calm substrings.

**Constraints:-**

- $1 \le n \le 2 \cdot 10^5$
- $s$ contains only lowercase English letters
**Examples:-**
 - **Input:**
```
11
zzzzazzzzzz
```

 - **Output:**
```
2
```

 - **Input:**
```
26
abcdefghijklmnopqrstuvwxyz
```

 - **Output:**
```
325
```

**Note:-**

In the first example, $s=$ "zzzzazzzzzz". Almost every substring has a strict majority of 'z', so it is not calm. The only calm substrings are the two length-$2$ substrings "za" and "az", because each letter appears exactly once and thus the maximum frequency is $1 \le \frac{2}{2}=1$.

In the first example, $s=$ "abcdefghijklmnopqrstuvwxyz". Any substring of length $m \ge 2$ has all distinct letters, so every letter appears at most once, and $1 \le \frac{m}{2}$ holds for all $m \ge 2$. Therefore, all substrings of length at least $2$ are calm, and the answer equals
$$
\frac{n(n+1)}{2}-n=\frac{26\cdot 27}{2}-26=325.
$$