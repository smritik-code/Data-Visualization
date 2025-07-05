import numpy as np 
import random


def markov_chains(init,states):
    def nex_state_calc(init):
        transformation_mat = np.array([[0.6, 0.1, 0.3],[0.3, 0.3, 0.4],[0.1, 0.7, 0.2]])
        
        p = np.dot(init,transformation_mat)

        return p


    p = nex_state_calc(init)
    p /= p.sum()  #normalising p 
    
    next = np.cumsum(p)  #cumulative probability

    r = random.random()

    weather=''

    for i in range(len(next)):
        if r<next[i]:
            weather=states[i]
            break


    return(p, weather)



states=["Sunny", "Rainy", "Cloudy"]
init = np.array([0,1,0])

trend_p=[init]
trend = ["Rainy"]

for i in range(7):
    init,weather=markov_chains(init,states)
    trend_p.append(init)
    trend.append(weather)

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#print(trend_p)

plot_data = pd.DataFrame(trend_p, columns=states).reset_index().melt(
    id_vars="index", var_name="State", value_name="Probability"
)
#print(plot_data,'\n')
plot_data.rename(columns={"index": "Day"}, inplace=True)

sns.lineplot(data=plot_data, x="Day", y="Probability", hue="State", marker="o")
plt.title("State Probabilities Over Time")
plt.xlabel("Day")
plt.ylabel("Probability")
plt.show()



color_map = {
    "Sunny": "#FFD700",
    "Rainy": "#1E90FF",
    "Cloudy": "#A9A9A9"
}
fig, ax = plt.subplots(figsize=(10, 2))

for day, weather in enumerate(trend):  # iterates over index, value
    color = color_map.get(weather, "#FFFFFF")
    rect = plt.Rectangle((day, 0), 1, 1, facecolor=color, edgecolor='black')
    ax.add_patch(rect)

    ax.text(day + 0.5, 0.5, f"Day {day}\n{weather}", 
            ha='center', va='center', fontsize=10, color='black')


ax.set_xlim(0, len(trend))
ax.set_ylim(0, 1)
ax.axis('off')
plt.title("Weather Prediction")
plt.show()
