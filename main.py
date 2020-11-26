from diaries.DiarySample import DiarySample
from diaries.TakahashiDiaryNew import TakahashiDiary

diaries = [DiarySample(), TakahashiDiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()