import datetime
import pytz

timezone = pytz.timezone('America/Chicago')
time_in_timezone = datetime.datetime.now(timezone)

time = [int(time_in_timezone.strftime('%H')), int(time_in_timezone.strftime('%M')), int(time_in_timezone.strftime('%S'))]
today = datetime.datetime.today().weekday()

"""
Wednesday can be divided into 46 min chunks (2760 seconds)
dayEnd in military time would be at the 54,600th second of the day
"""

wedTimes = (
    32400, 34920,   # Period 1 (09:00, 09:42)
    35220, 37740,   # Period 2 (09:47, 10:29)
    38040, 40560,   # Period 3 (10:34, 11:16)
    40860, 43380,   # Period 4 (11:21, 12:03)
    43680, 46140,   # Period 5 (12:08, 12:49)
    46440, 48960,   # Period 6 (12:54, 13:36)
    49260, 51780,   # Period 7 (13:41, 14:23)
    52080, 54600    # Period 8 (14:28, 15:10)
)

monFriTimes = (
    27900, 30900,   # Period 1 (07:45, 08:35)
    31260, 34440,   # Period 2 (08:41, 09:34)
    34800, 37800,   # Period 3 (09:40, 10:30)
    38160, 41160,   # Period 4 (10:36, 11:26)
    41520, 44520,   # Period 5 (11:32, 12:22)
    44880, 47880,   # Period 6 (12:28, 13:18)
    48240, 51240,   # Period 7 (13:24, 14:14)
    51600, 54600    # Period 8 (14:20, 15:10)
)

tueThursTimes = (
    27900, 30600,   # Period 1 (07:45, 08:30)
    30900, 33600,   # Period 2 (08:35, 09:20)
    33900, 36600,   # SOAR      (09:25, 10:10)
    36900, 39600,   # Period 3 (10:15, 11:00)
    39900, 42600,   # Period 4 (11:05, 11:50)
    42900, 45600,   # Period 5 (11:55, 12:40)
    45900, 48600,   # Period 6 (12:45, 13:30)
    48900, 51600,   # Period 7 (13:35, 14:20)
    51900, 54600    # Period 8 (14:25, 15:10)
)

elapsed = None
remaining = None
def scheduleCheck(givenList):
    for i in range(len(givenList)):
        if i == 0:
            continue
        if timeInSecs <= givenList[i]:
            lengthOfPeriod = givenList[i] - givenList[i - 1]
            elapsedTimeAsPercent = ((timeInSecs - givenList[i - 1]) / lengthOfPeriod) * 100
            timeRemaining = givenList[i] - timeInSecs
            if i % 2 == 1:
                print("You're in a period")
            else:
                print("You're in a passing period")
            break
    return "{:.2f}".format(elapsedTimeAsPercent), timeRemaining


timeInSecs = (time[0] * 3600) + (time[1] * 60) + (time[2])

#$ ========CHECK FOR PAST SATURDAY/SUNDAY===========
if today == 5 or today == 6:
    print("It's the weekends.")

#$ ========CHECK FOR PAST 3:10PM===========
elif timeInSecs > 54600:
    print("School is over!")

#$ ========LATE START SCHEDULE==========
elif today == 2:
    #$ ========CHECK BEFORE 9:00AM==========
    if timeInSecs < 32400:
        print("School hasn't started yet!")
    else:
        elapsed, remaining = scheduleCheck(wedTimes)
#$ ========NOT LATE START==========
else:
    #$ ========CHECK BEFORE 7:45AM==========
    if timeInSecs < 27900:
        print("School hasn't started yet!")
    elif today == 0 or today == 4:
        elapsed, remaining =  scheduleCheck(monFriTimes)
    elif today == 1 or today == 3:
        elapsed, remaining = scheduleCheck(tueThursTimes)

print(f'{elapsed}% of the period is done')
print(f'{remaining} seconds remaining')
