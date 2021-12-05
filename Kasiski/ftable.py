import math
import sys

s = open(sys.argv[1]).read()
period = int(sys.argv[2])

def ftable(s, period = 1, skip = 0):

    slen = 0
    count = [0 for i in range(26)]
    for i in range(skip, len(s), period):
        slen += 1
        count[ord(s[i]) - 65] += 1

    out = "Total chars of the group(skip = " + str(skip) + "): %d\n" % slen
    for c, n in enumerate(count):
        c = chr(c + 65)
        percent = 100.0 * n / slen
        out += "%s: %10d (%6.2f%%) %s\n" % (c, n, percent, '*' * math.ceil(percent))

    ic = (
        1.00 / (slen * (slen - 1))
        * sum([f * (f - 1) for f in count])
    )
    out += "\nIndex of Coincidence: %.4f\n" % ic

    return out

if __name__ == '__main__':
    for i in range(period):
        print(ftable(s, period, i))
        