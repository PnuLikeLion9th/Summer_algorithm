# 문제: https://leetcode.com/problems/group-anagrams/
#난이도: Medium
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)  # 디폴트 생성

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)  # 정렬해서 딕셔너리에 추가
        return list(anagrams.values())
