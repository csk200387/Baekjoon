morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# 입력 받기
s = input()

# 입력 받은 문자열에서 알파벳과 숫자만 추출
s = ''.join(filter(str.isalnum, s))

# 모스 부호 변환하기
morse_s = ''
for c in s.upper():
    morse_s += morse_code_dict[c]

# 모스 부호가 펠린드롬인지 확인하기
if morse_s == morse_s[::-1] and len(morse_s) != 0:
    print('YES')
else:
    print('NO')