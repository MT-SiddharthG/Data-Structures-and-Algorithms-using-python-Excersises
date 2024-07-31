"""
1.7 Design and implement a TimeDate ADT that can be used to represent both
a date and time as a single entity.
"""

class TimeDate:
    def __init__(self, year, month, day, hours, minutes, seconds):
        self.year = year
        self.month = month
        self.day = day
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.total_seconds = hours * 3600 + minutes * 60 + seconds

    def year(self):
        return self.year

    def month(self):
        return self.month

    def day(self):
        return self.day

    def hour(self):
        return self.hours

    def minutes(self):
        return self.minutes

    def seconds(self):
        return self.seconds

    def numSeconds(self, otherTimeDate):
        return abs(self.total_seconds - otherTimeDate.total_seconds)

    def isAM(self):
        return self.hours < 12

    def isPM(self):
        return self.hours >= 12

    def __eq__(self, otherTimeDate):
        return (self.year == otherTimeDate.year and
                self.month == otherTimeDate.month and
                self.day == otherTimeDate.day and
                self.total_seconds == otherTimeDate.total_seconds)

    def __lt__(self, otherTimeDate):
        if self.year!= otherTimeDate.year:
            return self.year < otherTimeDate.year
        elif self.month!= otherTimeDate.month:
            return self.month < otherTimeDate.month
        elif self.day!= otherTimeDate.day:
            return self.day < otherTimeDate.day
        else:
            return self.total_seconds < otherTimeDate.total_seconds

    def __le__(self, otherTimeDate):
        if self.year!= otherTimeDate.year:
            return self.year <= otherTimeDate.year
        elif self.month!= otherTimeDate.month:
            return self.month <= otherTimeDate.month
        elif self.day!= otherTimeDate.day:
            return self.day <= otherTimeDate.day
        else:
            return self.total_seconds <= otherTimeDate.total_seconds

    def __gt__(self, otherTimeDate):
        if self.year!= otherTimeDate.year:
            return self.year > otherTimeDate.year
        elif self.month!= otherTimeDate.month:
            return self.month > otherTimeDate.month
        elif self.day!= otherTimeDate.day:
            return self.day > otherTimeDate.day
        else:
            return self.total_seconds > otherTimeDate.total_seconds

    def __ge__(self, otherTimeDate):
        if self.year!= otherTimeDate.year:
            return self.year >= otherTimeDate.year
        elif self.month!= otherTimeDate.month:
            return self.month >= otherTimeDate.month
        elif self.day!= otherTimeDate.day:
            return self.day >= otherTimeDate.day
        else:
            return self.total_seconds >= otherTimeDate.total_seconds

    def __str__(self):
        am_pm = "AM" if self.isAM() else "PM"
        hours = self.hours % 12 if self.hours!= 12 else 12
        return f"{self.month}/{self.day}/{self.year} {hours}:{self.minutes:02d}:{self.seconds:02d} {am_pm}"


if __name__ == "__main__":
    time_date1 = TimeDate(2022, 12, 25, 10, 30, 0)
    time_date2 = TimeDate(2022, 12, 25, 11, 30, 0)
    print("Time Date 1:", time_date1)
    print("Time Date 2:", time_date2)
    print("Time Date 1 is AM:", time_date1.isAM())
    print("Time Date 2 is PM:", time_date2.isPM())
    print("Time Date 1 is equal to Time Date 2:", time_date1 == time_date2)
    print("Time Date 1 is less than Time Date 2:", time_date1 < time_date2)
    print("Number of seconds between Time Date 1 and Time Date 2:", time_date1.numSeconds(time_date2))