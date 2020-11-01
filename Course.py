# Design and implment a course object that models courses at NAU offerred at NAU.
#  Courses should be initialized with a short name, a number of credits, a
#   start time, and an end time. Include a method that will return True if
#   two course times overlap, and false is they do not.

class Course():
    def __init__(self, name, num_credits, days, start_time, end_time):
        self._name=name
        self._num_credits=num_credits
        self._days=days  # need this to check overlap
        self._start_time=start_time
        self._end_time=end_time

    def getName(self):
        return self._name

    def overlaps(self, other):
        # if days overlap, check times
        if self._daysOverlap(other):
            return self._timesOverlap(other)
        else:
            return False

    def _daysOverlap(self, other):
        if self._days.intersection(other._days):
            return True
        else:
            return False

    def _timesOverlap(self,other):
        # compare all times using minutes since midnight
        self_start = self._getMinutes(self._start_time)
        self_end = self._getMinutes(self._end_time)
        other_start = other._getMinutes(other._start_time)
        other_end = other._getMinutes(other._end_time)
        
        # if start of other falls between start and end of self
        if other_start >= self_start and other_start <= self_end:
            return True
            
        # if end of other falls between start and end of self
        if other_end >= self_start and other_end <= self_end:
            return True
            
        # if other start is less than self start AND other end is greater then self end
        if other_start <= self_start and other_end >= self_end:
            return True
        
        return False

    # method assume timeString is given in 24 hour format HH:MM
    def _getMinutes(self, time):
        time_list = time.split(":")
        return int(time_list[0])*60 + int(time_list[1])

    def __str__(self):
        return self._name + " " + str(self._days) + " " + self._start_time +" " + self._end_time


cs126 = Course("CS126", 3, {'T','Th'},"11:10", "12:25")
cs122 = Course("CS122",2,{'M','W'},"8:00", "8:50")
cs122L = Course("CS122L",1,{'T'},"12:00","14:00")
print(cs122)
print(cs126.overlaps(cs122))
print(cs126.overlaps(cs122L))
