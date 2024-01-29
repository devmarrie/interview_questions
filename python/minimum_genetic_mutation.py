# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

#     For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

# Example 1:

# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1

# Example 2:

# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        choice = set(['A', 'C', 'G', 'T'])
        q = deque()
        q.append([startGene, 0])
        visited = set(startGene)

        while q:
            gene, count = q.popleft()
            if gene == endGene:
                return count
            for i, s in enumerate(gene):
                for c in choice:
                    if s != c:
                        new_gene = gene[:i] + c + gene[i+1:]
                        if new_gene in bank and new_gene not in visited:
                            q.append([new_gene, count + 1])
                            visited.add(new_gene)
        return -1


