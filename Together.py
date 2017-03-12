# This function returns the count of the maximum number of consecutive
# observations in each trajectory such that the observations occur at the same
# time and are close.
# Author: Dixin Zhang
# Student ID: 804604
# Date created: 27th August
# Date modified: 5th September


def together(tr1, tr2, th):
    # use var dic to store each different time span
    dic = dict()

    # check all points
    count = 0
    for i in range(len(tr1)):
        for j in tr2:
            # start counting if two points are both close and time-synchronized
            if tr1[i][2] == j[2]:
                if ((tr1[i][0]-j[0])**2+(tr1[i][1]-j[1])**2)**0.5 <= th:
                    count = True
                else:
                    count = False
                break

        # update dic to store different time span
        if count:
            if tr1[i-1] in dic.keys():
                dic[tr1[i]] = dic[tr1[i-1]]+1
            else:
                dic[tr1[i]] = 1

    # find the maximum time span recorded
    if dic:
        return max(dic.values())
    else:
        return 0
