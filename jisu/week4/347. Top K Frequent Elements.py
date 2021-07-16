# 문제: https://leetcode.com/problems/top-k-frequent-elements/
# 난이도: Medium

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
        # collections.Counter(nums).most_common(k) : 빈도 수가 높은 2개 검출
        # * : 언패킹으로 리스트를 풀어줌
        # list(zip(*~~~)) : 현재 [수, 빈도]로 저장되어 있으므로, zip으로 '수'를 검출하여 list로 변환 (zip을 사용하면 tuple로 반환 됨)
