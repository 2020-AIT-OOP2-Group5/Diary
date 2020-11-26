from diaries.DiarySample import DiarySample
from diaries.TakahashiDiaryNew import TakahashiDiaryNew

diaries = [DiarySample(), TakahashiDiaryNew(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()