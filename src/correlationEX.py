import math
#Data for correlation
study_hours = [1, 2, 3, 4, 5]
test = [40, 50, 60, 70, 80]
#Mean function
def mean(values):
    return sum(values)/len(values)
#Variance Helper Function
def de_mean(values):
    mean_value = mean(values)
    return [X - mean_value for X in values]
#Covariance Function
def covariance(x,y):
    n = len(x)
    return sum(a*b for a,b in zip(de_mean(x),de_mean(y)))/(n-1)
#Standard Deviation Function
def standard_deviation(values):
    return math.sqrt(sum([x**2 for x in de_mean(values)])/(len(values)-1))
#Correlation Function
def correlation(x,y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x,y)/stdev_x/stdev_y
    else:
        return 0


cov = covariance(study_hours,test)
print(cov)
cor = correlation(study_hours,test)
print(cor) 
