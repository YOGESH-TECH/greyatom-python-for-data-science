# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)
#Code starts here
census=np.concatenate((data,new_record))
print(census.shape)
age=census[:,0]
max_age=max(age)
print(max_age)
min_age=min(age)
print(min_age)
age_mean=np.mean(age)
print(age_mean)
age_std=np.std(age)
print(age_std)
#race step3
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
print(len_0,len_1,len_2,len_3,len_4)
minority_race=3
senior_citizens=census[age>60]
print(len(senior_citizens))
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=round((working_hours_sum/senior_citizens_len),2)
print(avg_working_hours)
#step5
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=round(((high.sum(axis=0)[7])/len(high)),2)
print(avg_pay_high)
avg_pay_low=round(((low.sum(axis=0)[7])/len(low)),2)
print(avg_pay_low)


