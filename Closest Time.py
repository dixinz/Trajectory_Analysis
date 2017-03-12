# This function takes an argument tr that represents the trajectory and returns
# the time of the earliest observation in tr that is closest to the point pt.
# Author: Dixin Zhang
# Student ID: 804604
# Date created: 25th August
# Date modified: 6th September


def closestTime(tr, pt):
    # check all points, put all distance and time in variable distance
    distance = []
    for i in tr:
        distance.append([((pt[0]-i[0])**2+(pt[1]-i[1])**2)**1/2, i[2]])

    # return the earliest time of the minimum distance
    return min(distance)[1]
