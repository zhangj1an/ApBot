import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

# p-value matrix
p_values = np.array([
    [1.000, 0.000, 0.007, 0.000, 0.275, 0.000],
    [0.000, 1.000, 0.032, 0.000, 0.000, 0.000],
    [0.007, 0.032, 1.000, 0.000, 0.000, 0.000],
    [0.000, 0.000, 0.000, 1.000, 0.000, 0.000],
    [0.275, 0.000, 0.000, 0.000, 1.000, 0.000],
    [0.000, 0.000, 0.000, 0.000, 0.000, 1.000],
])

labels = [
    "cot + image", 
    "cot + action", 
    "ours w/o button policy", 
    "ours w/o structured reasoning", 
    "ours w/o close loop update", 
    "ours"
]

# Create DataFrame
df = pd.DataFrame(p_values, index=labels, columns=labels)

# Mask 1.0 values
mask_diag = df == 1.0
masked_values = df.mask(mask_diag)
vmin = masked_values.min().min()
vmax = masked_values.max().max()

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(masked_values, annot=df, fmt=".3f", cmap="YlGn", linewidths=0.5,
            cbar_kws={'label': 'p-value'}, vmin=vmin, vmax=vmax, ax=ax)

# Overlay grey for p = 1.000
for i in range(len(labels)):
    ax.add_patch(plt.Rectangle((i, i), 1, 1, fill=True, color='#d3d3d3', ec='white', lw=0.5))
    ax.text(i + 0.5, i + 0.5, "1.000", ha='center', va='center', color='black', fontsize=9)

# Add legend to top-right outside plot (next to title)
grey_patch = mpatches.Patch(color='#d3d3d3', label='Not Applicable') #  (p = 1.000)
ax.set_title("p-value matrix", fontsize=14, pad=20)
fig.legend(handles=[grey_patch], loc='upper center', bbox_to_anchor=(0.83, 1), frameon=True)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("sig.png", dpi=300, bbox_inches='tight')
plt.close()


#srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “vlm” python3 