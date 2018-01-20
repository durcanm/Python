class Time:
     """ time class"""
     def __init__(self, hour=0, minute=0, second=0):
          self.hour = hour # stores the value of the parameter hour as an attribute of self.
          self.minute = minute
          self.second = second
     def __str__(self):
          return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
     def __add__(self, other):
          if isinstance(other,Time): # type-based dispatch
               return self.add_time(other)
          else:
               return self.increment(other)
     def __radd__(self,other):
          return self.__add__(other)
     def add_time(self,other):
          seconds=self.time_to_int() + other.time_to_int()
          return int_to_time(seconds)
     def print_time(self):
          print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
     def increment(self, seconds):
          seconds += self.time_to_int()
          return int_to_time(seconds)
     def time_to_int(self):
          minutes = self.hour * 60 + self.minute
          i = minutes * 60 + self.second
          return i
     def is_after(self,other):
          return self.time_to_int() > other.time_to_int()


def int_to_time(seconds):
     minutes,seconds = divmod(seconds,60)
     hours,minutes = divmod(minutes,60)
     t = Time()
     t.hour = hours
     t.minute = minutes
     t.second = seconds
     return t

#-----------------------------
start = Time()
start.hour = 9
start.minute = 45
start.second = 00

start.print_time()

#Time.print_time(start) == start.print_time()

end = start.increment(1337)
end.print_time()

print('end is after start?:',end.is_after(start))
#-----------------------------
time = Time()
time.print_time()

time = Time(9)
time.print_time()

time = Time(9,45)
time.print_time()

time = Time(9,45,18)
time.print_time()

print(time)
#-----------------------------
start = Time(9,45)
duration = Time(1,35)
print('duration:',start+duration)
print(start+11)
print(11+start) #__radd__
#-----------------------------
t1 = Time(7, 43)
t2 = Time(7, 41)
t3 = Time(7, 37)
total = sum([t1, t2, t3])
print(total)

