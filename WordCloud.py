import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patheffects as path_effects
import numpy as np

# Word positions are set by two axes:
# x = collaboration score, y = performance score
# size is a third dimension (e.g., frequency or importance)
words = {
    "Performance": {"collaboration": 0.14, "performance": 0.95, "size": 15},
    "Efficacité": {"collaboration": 0.4, "performance": 0.8, "size": 10},
    "Rendement": {"collaboration": 0.10, "performance": 0.85, "size": 8},
    "Croissance": {"collaboration": 0.35, "performance": 0.98, "size": 8},
    "Dynamiser": {"collaboration": 0.15, "performance": 0.81, "size": 7},
    "Exploit": {"collaboration": 0.25, "performance": 0.75, "size": 5},
    "Stimuler": {"collaboration": 0.1, "performance": 0.78, "size": 7},
    "Développer": {"collaboration": 0.3, "performance": 0.7, "size": 7},
    "Accélération": {"collaboration": 0.12, "performance": 0.9, "size": 5},
    "Amélioration": {"collaboration": 0.25, "performance": 0.86, "size": 8},
    "Energie": {"collaboration": 0.10, "performance": 0.70, "size": 6},
    "Optimisation": {"collaboration": 0.35, "performance": 0.9, "size": 10},
    "Productivité": {"collaboration": 0.60, "performance": 0.68, "size": 13},
    "Compétence": {"collaboration": 0.55, "performance": 0.78, "size": 10},
    "Résultat": {"collaboration": 0.60, "performance": 0.82, "size": 12},
    "Succès": {"collaboration": 0.48, "performance": 0.86, "size": 8},
    "Maitrise": {"collaboration": 0.42, "performance": 0.70, "size": 6},
    "Vigueur": {"collaboration": 0.20, "performance": 0.65, "size": 5},
    "Collaboration": {"collaboration": 0.85, "performance": 0.02, "size": 15},
    "Entraide": {"collaboration": 0.72, "performance": 0.25, "size": 6},
    "Partenariat": {"collaboration": 0.85, "performance": 0.25, "size": 8},
    "Synergie": {"collaboration": 0.70, "performance": 0.58, "size": 6},
    "Coopération": {"collaboration": 0.88, "performance": 0.15, "size": 10},
    "Union": {"collaboration": 0.70, "performance": 0.40, "size": 6},
    "Ordre": {"collaboration": 0.50, "performance": 0.15, "size": 6},
    "Arrangement": {"collaboration": 0.7, "performance": 0.22, "size": 6},
    "Uniformisation": {"collaboration": 0.7, "performance": 0.10, "size": 6},
    "Conformité": {"collaboration": 0.6, "performance": 0.2, "size": 6},
    "Solidarité": {"collaboration": 0.82, "performance": 0.42, "size": 8},
    "Alliance": {"collaboration": 0.78, "performance": 0.48, "size": 8},
    "Travail d'équipe": {"collaboration": 0.88, "performance": 0.1, "size": 8},
    "Partage": {"collaboration": 0.76, "performance": 0.38, "size": 6},
    "Alignement": {"collaboration": 0.80, "performance": 0.20, "size": 8},
    "Coordination": {"collaboration": 0.92, "performance": 0.45, "size": 6},
    "Cohérence": {"collaboration": 0.78, "performance": 0.3, "size": 8},
    "Cohésion": {"collaboration": 0.9, "performance": 0.3, "size": 8}

}
colors = ["#00b4d8", "#0077b6"]
custom_cmap = LinearSegmentedColormap.from_list("collab_perf", colors)
fig, ax = plt.subplots(figsize=(10, 6))

# Gradient background using the same colors
bg_grad = np.linspace(0, 1, 256).reshape(1, -1)
ax.imshow(
    bg_grad,
    extent=[0, 1, 0, 1],
    origin="lower",
    aspect="auto",
    cmap=custom_cmap,
    zorder=0,
)

for word, attrs in words.items():
    x = attrs["collaboration"]
    y = attrs["performance"]
    size = attrs["size"]
    color = "#FFFFFF"
    ax.text(
        x,
        y,
        word,
        fontsize=size,
        ha="center",
        va="center",
        color=color,
        alpha=1.0,
    )

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel("Collaboration (x-axis)", fontweight="bold", fontsize=13, color="#FF4400")
ax.set_ylabel("Performance (y-axis)", fontweight="bold", fontsize=13, color="#FF4400")
ax.set_title("Canva Boost vs Canva Align", fontweight="bold", fontsize=18, color="#FF4400")
ax.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()
