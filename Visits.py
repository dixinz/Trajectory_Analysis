# This function returns the number of times the trajectory enters the box.
# Author: Dixin Zhang
# Student ID: 804604
# Date created: 27th August
# Date modified: 6th September


def visits(tr, b):
    # find all points in the box and store their times in list time_in_box
    time_in_box = []
    for i in range(len(tr)):
        if b[1][0] >= tr[i][0] >= b[0][0] and b[1][1] >= tr[i][1] >= b[0][1]:
            time_in_box.append(tr[i][2])

    # for all time points in the list, if they are not differed by 1, increment
    # count
    count = 0
    for i in range(len(time_in_box)):
        if time_in_box[-i]-1 != time_in_box[-i-1]:
            count += 1

    return count
