# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

# Human Readable Time

def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
