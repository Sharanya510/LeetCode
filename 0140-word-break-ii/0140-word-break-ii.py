class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        seen = set()
        for word in wordDict:
            if s.startswith(word):
                queue = collections.deque()
                queue.append([len(word), "{} ".format(word)])
                seen.add("{} ".format(word))
                # print(queue, seen)
                while queue:
                    matched_length, sentence = queue.popleft()
                    if matched_length == len(s):
                        seen.add(sentence)
                        res.append(sentence.strip(" "))
                        continue
                    rest_s = s[matched_length:]
                    for word in wordDict:
                        if rest_s.startswith(word):
                            if sentence + "{} ".format(word) not in seen:
                                queue.append([matched_length + len(word), sentence + "{} ".format(word)])
                                seen.add(sentence + "{} ".format(word))
        return res
