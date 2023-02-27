def solution(t, p):
    answer = 0
    l = len(p)
    for i in range(l, len(t)+1) :
        tmp = t[i-l:i]
        if int(p) >= int(tmp) :
            answer += 1
    return answer