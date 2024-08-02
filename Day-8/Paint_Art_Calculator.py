import math


def cal_cans(hei, wid, cov):
    return math.ceil((hei * wid)/cov)


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

print(cal_cans(test_h, test_w, coverage))