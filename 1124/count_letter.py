filename = input("파일명을 입력하세요 : ").strip() # 문자열 양쪽끝의 공백과
infile = open(filename, "r")

freqs = {}

for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1
        else:
            freqs [char] = 1

print(freqs)

infile.close()