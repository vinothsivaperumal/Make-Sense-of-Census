# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#New record
new_record=np.array([50,  9,  4,  1,  0,  0, 40,  0])
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.ndim)
census= np.vstack([data,new_record])
print(census.ndim)
#Code starts here
age = census[:,0]
print(age)
max_age =age.max()
print(max_age)
min_age =age.min()
print(min_age)
age_mean=age.mean()
print(age_mean)
age_std=age.std()
print(age_std)

race_0=census[census[:,2]==0].astype(int)
race_1=census[census[:,2]==1].astype(int)
race_2=census[census[:,2]==2].astype(int)
race_3=census[census[:,2]==3].astype(int)
race_4=census[census[:,2]==4].astype(int)
len_0 =len(race_0)
len_1 =len(race_1)
len_2 =len(race_2)
len_3 =len(race_3)
len_4 =len(race_4)
a=np.array([len_0,len_1,len_2,len_3,len_4])/2
minority_race =a.min()
print(minority_race)
senior_citizens = census[census[:,0]>60].astype(int)
working_hours_sum = np.sum(senior_citizens[:,6],axis=0)
senior_citizens_len = len(senior_citizens) 
avg_working_hours = working_hours_sum/senior_citizens_len
print(working_hours_sum)
print(avg_working_hours)

high = census[census[:,1]>10].astype(int)
low = census[census[:,1]<=10].astype(int)
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

print(avg_pay_high)
print(avg_pay_low)
