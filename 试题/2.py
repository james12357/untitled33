"""
@author:蔡俊熙
"""
lovelist1 = ["真功夫", "面点王", "Starbucks", "Burger King", "KFC", "必胜客"]
lovelist2 = ["萨莉亚", "McDonald", "吉野家", "真功夫", "Starbucks"]
same = []
round = 0
count = 0
round2 = 0
for i in lovelist1:
    for s in lovelist2:
        if not len(lovelist2) == round2:
            if lovelist1[round] == lovelist2[round2]:
                same.append(lovelist1[round])
        else:
            continue
        round2 = round2 + 1
    round = round + 1
    round2 = 0
print(same)
