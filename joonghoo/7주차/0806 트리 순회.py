# 백준_1991_트리 순회_트리_실버 1
# 기본적인 이진 트리 문제
# 정점을 문자열로 나타내기 때문에 dictionary로 구현하였다

import sys
input = sys.stdin.readline


def preorder(root): # 전위 순회 함수 (루트 -> 왼쪽 자식 -> 오른쪽 자식 순서로 출력)
    print(root, end='')
    if tree[root][0] != '.':
        preorder(tree[root][0])
    if tree[root][1] != '.':
        preorder(tree[root][1])


def inorder(root): # 중위 순회 함수 (왼쪽 자식 -> 루트 -> 오른쪽 자식 순서로 출력)
    if tree[root][0] != '.':
        inorder(tree[root][0])
    print(root, end='')
    if tree[root][1] != '.':
        inorder(tree[root][1])


def postorder(root): # 후위 순회 함수 (왼쪽 자식 -> 오른쪽 자식 -> 루트 순서로 출력)
    if tree[root][0] != '.':
        postorder(tree[root][0])
    if tree[root][1] != '.':
        postorder(tree[root][1])
    print(root, end='')


n = int(input())
tree = {}
for _ in range(n):
    p, l, r = input().strip().split() # 부모, 왼쪽 자식, 오른쪽 자식을 입력받는다
    tree[p] = [l, r] # 부모 정점에 왼쪽 자식, 오른쪽 자식을 저장한다

preorder('A') # 전위 순회 실행
print()
inorder('A') # 중위 순회 실행
print()
postorder('A') # 후위 순회 실행
