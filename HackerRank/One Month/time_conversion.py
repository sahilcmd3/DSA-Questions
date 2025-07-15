# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock


def timeConvert(s):
    hh = int(s[0:2])
    mm = s[3:5]
    ss = s[6:8]
    period = s[8:10]

    if period == "AM" and hh == 12:
        hh = 0
    elif period == "PM" and hh < 12:
        hh += 12

    hour = f"{hh:02d}" if hh < 10 else str(hh)
    return f"{hour}:{mm}:{ss}"


if __name__ == "__main__":
    print(timeConvert(s="04:59:59AM"))
