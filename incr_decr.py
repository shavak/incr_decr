# -*- coding: utf-8 -*-
"""
The Increasing-Decreasing Subsequence Problem.

(a) Prove that within any given sequence of mn + 1 different real
numbers, there exists either a strictly increasing subsequence of
length m + 1 or a strictly decreasing subsequence of length n + 1.

(b) Write an algorithm which when given a sequence of mn + 1
different real numbers, returns either a strictly increasing
subsequence of length m + 1 or a strictly decreasing subsequence of
length n + 1.


Contained herein is a function which, when given a sequence of mn + 1
different real numbers, returns either a strictly increasing
subsequence of length m + 1 or a strictly decreasing subsequence of
length n + 1.

Author: Shavak Sinanan <shavak@gmail.com>
"""

def pigeonholed_subsequence(a, m, n):
    """
    Finds either a strictly increasing subsequence or strictly
    decreasing subsequence. 

    Parameters
    ----------
    a : list
        Sequence of different real numbers.
    m : int
        Integer.
    n : int
        Integer.

    Returns
    -------
    A subsequence of a that is either strictly increasing and of length
    m + 1 or strictly decreasing and of length n + 1.

    """
    L = m * n + 1
    if len(a) != L:
        # Input validation.
        return [-1]
    tower = [[0]]
    prev = [-1] * L
    k = 0
    h = 1
    ans = []
    seq_desc = "increasing"
    for i in range(1, L):
        if a[i] < a[tower[k][-1]]:
            # This element can be placed at the top of the "best" tower.
            tower[k].append(i)
            if len(tower[k]) > n:
                # Tall tower. Decreasing sequence found.
                ans = tower[k]
                seq_desc = "decreasing"
                break
            # Find the new "best" tower.
            for j in range(h):
                if a[tower[k][-1]] < a[tower[j][-1]]:
                    k = j
        else:
            # Add a new tower.
            tower.append([i])
            # Set back-link.
            prev[i] = tower[k][-1]
            # New best tower.
            k = h
            # Update the number of towers.
            h += 1
            if h > m:
                # Many towers. Increasing sequence found.
                ans = [i]
                for j in range(m):
                    ans.append(prev[ans[j]])
                # I put my thing down, flip it, and reverse it.
                ans.reverse()
                break
    return ans, seq_desc
            

if __name__ == "__main__":
    a = [5, 3, 2, 1, 6, 7, 8, 9, 4, 10]
    x, seq_desc = pigeonholed_subsequence(a, 3, 3)