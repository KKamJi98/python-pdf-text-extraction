import pandas as pd
import pdfplumber
import re

# PDF 파일 열기
with pdfplumber.open("toeic_voca.pdf") as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

# 단어-뜻 구분
word_pairs = []
lines = text.split("\n")

# 형식: 첫 번째 숫자 + 영어 단어 + 한글 뜻 + 두 번째 숫자 + 영어 단어 + 한글 뜻
pattern = re.compile(r"(\d+)\s+([A-Za-z]+)\s+(.+?)\s+(\d+)\s+([A-Za-z]+)\s+(.+)")

"""test"""
# for i in range(100):
#     if english_korean_pattern.match(lines[i]):
#         print(lines[i])

for line in lines:
    line = line.strip()
    match = pattern.match(line)
    if match:
        english_1 = match.group(2).strip()  # 영어 단어
        korean_1 = match.group(3).strip()  # 한글 뜻
        word_pairs.append({"English": english_1, "Korean": korean_1})
        # print(f"English: {english_1} \t Korean: {korean_1}")

        english_2 = match.group(5).strip()  # 영어 단어
        korean_2 = match.group(6).strip()  # 한글 뜻
        word_pairs.append({"English": english_2, "Korean": korean_2})
        # print(f"English: {english_2} \t Korean: {korean_2}")

"""test"""
# for i in range(100):
#     print(word_pairs[i])

df = pd.DataFrame(word_pairs)

print(df)

df.to_excel("toeic_voca.xlsx", index=False)
