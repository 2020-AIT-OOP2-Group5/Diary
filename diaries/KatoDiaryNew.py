from diaries.AbstractDiary import AbstractDiary


class KatoDiary(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "眠い"

    def get_author(self):
        return "Kato"