t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    # 양의 정수 중에서 작은 순서대로 N개의 합
    S1 = ((n + 1) * n) // 2

    # 양의 정수 중 홀수 혹은 짝수인 것들 중에서 작은 순서대로 N개의 합
    S2 = n ** 2
    S3 = (n + 1) * n

    print('#%d %d %d %d' % (tc, S1, S2, S3))
    
'''
1. 각 테스트 케이스마다 아래와 같이 S1, S2, S3 를 구한다.
  - S1 : ((n+1) * n) // 2
  - S2 : n ** 2
  - S3 : (n + 1) * n

2. 최종적으로 해당 테스트 케이스 번호와 함께 S1, S2, S3 를 출력한다.

'''
