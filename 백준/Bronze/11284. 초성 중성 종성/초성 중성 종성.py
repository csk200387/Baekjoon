초성 = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
중성 = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
종성 = " ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"
def 함수(인자):
 초 = (ord(인자) - ord('가')) // 588
 중 = ((ord(인자) - ord('가')) - (588 * 초)) // 28
 종 = (ord(인자) - ord('가')) - (588 * 초) - 28 * 중
 return 초성[초], 중성[중], 종성[종]
print(*함수(input()), sep="\n")