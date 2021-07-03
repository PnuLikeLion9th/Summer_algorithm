# 문제: https://leetcode.com/problems/reorder-data-in-log-files/
#난이도: Easy
# 풀이 정리: https://breathtaking-life.tistory.com/116

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # identifier를 제외한 문자열을 키로 두어 정렬, 동일한 경우에는 [0]을 기준으로 정렬
        letters.sort(key=lambda x:  (x.split()[1:], x.split()[0]))
        return letters+digits
