class Time:
     """ time class """


def time_to_int(time):
     #print('%d:%d:%d'%(time.hour,time.minute,time.second))
     minute = time.hour * 60 + time.minute
     second = minute * 60 + time.second
     return second


def int_to_time(i):
     minute,second = divmod(i, 60)
     hour, minute = divmod(minute, 60)
     t = Time()
     t.hour=hour
     t.minute=minute
     t.second=second
     #print('%d:%d:%d'%(hour,minute,second))
     return t

def add_time(t1,t2):
     t=time_to_int(t1) + time_to_int(t2)
     return int_to_time(t)



t=Time()
t.hour=12
t.minute=59
t.second=0

x=time_to_int(t)
y=int_to_time(x)


for x in range(0,10_000_000,25):
     assert time_to_int(int_to_time(x)) == x

