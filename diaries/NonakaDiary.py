from diaries.AbstractDiary import AbstractDiary


class NonakaDiary(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "ちょい眠い"

    def get_author(self):
        return "Nonaka"