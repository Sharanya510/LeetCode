class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        date_split_list = date.split(" ")
        day = date_split_list[0]
        mon = date_split_list[1]
        if mon in months:
            date_split_list[1] = months[mon]
        day = day[:-2]
        if len(day) == 1: day = "0" + day
        year = date_split_list[2]
        month = date_split_list[1]
        return f"{year}-{month}-{day}"
        
        