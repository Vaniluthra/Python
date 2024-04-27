'''
Stephan is a vampire. And he is fighting with his brother Damon. Vampires get energy from human blood, so they need to feed on human blood, killing human beings. Stephan is also less inhuman, so he will like to take less life in his hand. Now all the people’s blood has some power, which increases the powers of the Vampire. Stephan just needs to be more powerful than Damon, killing the least human possible. Tell the total power Stephan will have after drinking the blood before the battle.
Note: Damon is a beast, so no human being will be left after Damon drinks everyone’s blood. But Stephan always comes early to the town.

Input Format:
First line with the number of people in the town, n.
Second line with a string with n characters, denoting the one-digit power in every blood.

Output Format:
Total minimum power Stephan will gather before the battle.

Sample Input :
0 9 3 2 1 2
Sample output:
9
Explanation: Stephan riches the town and drinks the blood with power 9. Now Damon cannot reach 9 by drinking all the other blood.
'''

a=list(map(int, input('enter space separated list elements:').split()))
minsum,maxsum=0,0
while True:
    minval=min(a)
    maxval=max(a)
    if minval!=maxval:
        minsum+=minval
        maxsum=maxval
        if minsum<maxsum:
            a.remove(minval)
            
        if minsum>maxsum:
            a.remove(maxval)
            maxsum=maxsum+max(a)
    else:
        print(maxsum)
        break
