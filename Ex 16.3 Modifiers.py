class Time():
    """attributes: hour, minute, second"""


def increment(time, seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    time.minute += minutes

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    time.hour += hours

    if time.hour >= 24:
        time.hour -= 24
        time.day = 1

    time.day += days

sec_incr = 5000

time1 = Time()
time1.day = 0
time1.hour = 5
time1.minute = 00
time1.second = 00

print '%.2d:%.2d:%.2d:%.2d' % (time1.day, time1.hour, time1.minute, time1.second)
print 'incremented by %d seconds ' % sec_incr

increment(time1, sec_incr)

print '%.2d:%.2d:%.2d:%.2d' % (time1.day, time1.hour, time1.minute, time1.second)
