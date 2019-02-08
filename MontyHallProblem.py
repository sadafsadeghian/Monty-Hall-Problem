import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

x = ['Car', 'Goat']
# out of 3 doors, there is only 1 Car and 2 Goats
probability =[1/3, 2/3]

# Strategi 1: Not change your chosen door when Monty asks you to
result = {'Win': 0, 'Lose': 0}
iter = 0
for iter in range(1, 1001):
    y = np.random.choice(x, p=probability)
    if (y == "Car"):
        result['Win'] += 1
    else:
        result['Lose'] += 1

no_change_result_df = pd.DataFrame.from_dict(result, orient="index")
no_change_result_df.columns = ['Counts']
plt.bar(np.arange(2), no_change_result_df['Counts'], color='blue')
plt.xticks(np.arange(2), result.keys())
plt.show()
no_change_result_df


# Calculating the probability of winning when you have not changed your chosen door when Monty aksed
# Based on the simulation results

p_win_org = result['Win']/(result['Win']+result['Lose'])
print ('\nWinning in this game without switching your decision has a probability of {0} \n '.format(p_win_org))

print ('\nProbability of winning: {0}'.format(p_win_org))

print ('\nConsidering the result of the game, whit the original choice, as a Bernoulli distribution would have below mean and std')

print ('\nmean: ', (p_win_org))
print ('standard deviation: ', ((p_win_org)*(1-p_win_org))**0.5)

# Strategy 2: Switching to the other door when Monty has already eliminated one of the doors with the Goat behind it

result = {'Win': 0, 'Lose': 0}
for iter in range(1, 1001):
    y = np.random.choice(x, p=probability)
    if (y == 'Car'):
        result['Lose'] += 1  # Because we are switching the door we had initially picked
    else:
        result['Win'] += 1

changed_result_df = pd.DataFrame.from_dict(result, orient="index")
changed_result_df.columns = ['Counts']
plt.bar(np.arange(2), changed_result_df['Counts'], color='red')
plt.xticks(np.arange(2), result.keys())
plt.show()
changed_result_df

# Calculating the probability of winning when you have changed your chosen door when Monty aksed
# Based on the simulation results

p_win_switch = result['Win']/(result['Win']+result['Lose'])
print ('\nWinning in this game with switching your choice has a probability of {0}'.format(p_win_switch))

print ('\nProbability of winning: {0}'.format(p_win_switch))

print ('\nConsidering the result of the game, whit the changing your choice, as a Bernoulli distribution would have below mean and std')
print ('\nmean: ', (p_win_switch))
print ('standard deviation: ', ((p_win_switch)*(1-p_win_switch))**0.5)

print ('Based on the simulation results: the prrobability of wining a car with switching your original chosen door after Monty has eliminated one door ({0}) is higher than the probability of winning when you do not switch your chosen door ({1}). \nAlso, comparing the mean value of both 1000 games ( which is the same as the probability in Bernoulli distribution), it is obvious that the best strategy is to change your chosen door when Monty asks you to.'.format(p_win_switch, p_win_org))
print ('\nBasically, if you choose not to swtich the door, you would only win the game, if you have chosen the door with the Car behind on your first choice=> probability of winning: 1/3')
print('\nAnd if you choose to switch the door when Monty has eliminated one of the doors with the goat behind it, you would only win the game if you have initially chosen a door that had a goat behind it=> probability of winning: 2/3')
