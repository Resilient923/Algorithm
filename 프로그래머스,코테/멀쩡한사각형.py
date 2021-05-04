# 처음에는 직선의 방정식을 구해서 for 문으로 x,y값을 넣으려는 방식을 구현했는데 실패
# 직선의방정식이 결국에는 최대공약수 사용
# 최대공약수로 나눠서 최소화해서 구하고 최대공약수를 다시 곱해주는 방식

def solution(w,h):
    import math
    total = w * h
    # (w//gcd + h//gcd -1)*gcd
    answer = total - (w+h-math.gcd(w,h))
    return answer

print(solution(4,5))