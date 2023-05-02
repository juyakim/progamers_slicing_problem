# 문자열 뒤집기
# my_string을 거꾸로 뒤집은 문자열을 return


def solution(my_string):
    answer = my_string[::-1]  # 슬라이싱으로 뒷자리부터 출력
    return answer  # return answer 없어도 출력가능


# 배열의 유사도
# 두 배열이 얼마나 유사한지 확인해보려고 합니다.
# 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return


def solution(s1, s2):
    # 교집합
    return len(set(s1).intersection(s2))  # 중복값 반환함수 set.intersection


# s1 list와 s2의 list의 중복값을 반환한다.
