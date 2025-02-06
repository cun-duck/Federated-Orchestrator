import seaborn as sns
data = {
    'Architecture': ['Centralized Cloud', 'Federated Edge'],
    'Bandwidth (GB)': [120, 35]
}
sns.barplot(x='Architecture', y='Bandwidth (GB)', data=data)
plt.title("Bandwidth Efficiency: Edge vs Cloud")
plt.savefig("bandwidth.png")