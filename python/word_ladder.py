# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

#     Every adjacent pair of words differs by a single letter.
#     Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#     sk == endWord

# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append([beginWord, 1])
        wordSet = set([beginWord])
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList: #this is the trick
            for l in range(len(word)):
                pattern = word[:l] + "*" + word[l+1:] 
                nei[pattern].append(word)
        while q:
            for i in range(len(q)): #limits the checks to len of q
                val, count = q.popleft()
                if val == endWord:
                    return count
                for x in range(len(val)):
                    pattern_x = val[:x] + '*' + val[x+1:]
                    for neiWord in nei:
                        if neiWord not in wordSet:
                            wordSet.add(neiWord)
                            q.append([neiWord, count + 1])
        return 0
