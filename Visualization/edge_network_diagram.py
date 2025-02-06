
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title("Federated LLM Orchestration", fontsize=14)


ax.scatter([0.2, 0.5, 0.8], [0.5, 0.8, 0.5], s=500, c='skyblue', edgecolors='navy')
ax.text(0.5, 1.1, 'Cloud Aggregator', ha='center', fontsize=12)

for i in range(3):
    ax.annotate("", xy=(0.5, 0.9), xytext=(0.2 + i*0.3, 0.6),
                arrowprops=dict(arrowstyle="->", lw=2))

plt.savefig("edge_arch.png", dpi=300, transparent=True)
