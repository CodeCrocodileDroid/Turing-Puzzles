from collections import deque

class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        genes = ['A', 'C', 'G', 'T']
        queue = deque([(startGene, 0)])
        visited = set([startGene])

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for g in genes:
                    if g != gene[i]:
                        new_gene = gene[:i] + g + gene[i+1:]
                        if new_gene in bank_set and new_gene not in visited:
                            visited.add(new_gene)
                            queue.append((new_gene, steps + 1))

        return -1


# Example 1
print(Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
# Expected Output: 1

# Example 2
print(Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))
# Expected Output: 2

# Example 3: No possible mutation
print(Solution().minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"]))
# Expected Output: 3

# Example 4: End gene not in bank
print(Solution().minMutation("AACCGGTT", "AACCGCTA", ["AACCGGTA"]))
# Expected Output: -1

# Example 5: Start == End
print(Solution().minMutation("AACCGGTT", "AACCGGTT", ["AACCGGTA"]))
# Expected Output: 0
