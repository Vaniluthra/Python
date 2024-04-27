'''
There will be a batch of 3 trainees, appearing for running test in track for 3 rounds. 
You need to record their oxygen level after every round. After trainee are finished 
with all rounds, calculate for each trainee his average oxygen level over the 3 rounds 
and select one with highest oxygen level as the most fit trainee. If more than one 
trainee attains the same highest average level, they all need to be selected.
Display the most fit trainee (or trainees) and the highest average oxygen level.
Note:
• The oxygen value entered should not be accepted if it is not in the range 
between 1 and 100.
• If the calculated maximum average oxygen value of trainees is below 70 then 
declare the trainees as unfit with meaningful message as “All trainees are 
unfit.
• Average Oxygen Values should be rounded.
Example 1:
• INPUT VALUES
 95
 92
 95
 92
 90
 92
 90
 92
 90
• OUTPUT VALUES
o Trainee Number : 1
o Trainee Number : 3
'''

t1,t2,t3=[],[],[]
for i in range(9):
    inp=int(input())
    if inp>0 and inp<100:
        
        if i%3==0:
            t1.append(inp)
        elif i%3==1:
            t2.append(inp)
        else:
            t3.append(inp)

    else:
        print('invalid')
        break
            
import statistics
avg = {'trainee 1': statistics.mean(t1),
       'trainee 2': statistics.mean(t2),
       'trainee 3': statistics.mean(t3)}
if max(avg.values())<=70:
    print('all are unfit')
else:
    max_mean = max(avg.values())
    max_keys = [key for key, value in avg.items() if value == max_mean]
    for key in max_keys:
        print(key)
