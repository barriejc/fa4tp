import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

fm.fontManager.addfont("/Library/Fonts/Montserrat-Regular.ttf")
mpl.rcParams['font.family'] = 'Montserrat'

# Variables and their low/high impact values
variables = ["Capex", "Opex", "Sales"]
low_values = [-37, -152, -417]
high_values = [341, 455, 720]

# Calculate total impact
impact = np.abs(np.array(high_values) - np.array(low_values))

# Sort by impact
sorted_impact = np.argsort(impact)

variables = [variables[i] for i in sorted_impact]
low_values = [low_values[i] for i in sorted_impact]
high_values = [high_values[i] for i in sorted_impact]
mean_npv = (np.array(high_values) + np.array(low_values))/2
low_delta  = low_values - mean_npv
high_delta = high_values - mean_npv

# Plot the chart
y_pos = range(len(variables))

plt.figure(figsize=(8, 5))

# Left (negative) bars
plt.barh(y_pos, low_delta, left=mean_npv, color="cornflowerblue", label="Low case")

# Right (positive) bars
plt.barh(y_pos, high_delta, left=mean_npv, color="royalblue", label="High case")

plt.yticks(y_pos, variables)
plt.axvline(0, color="crimson", linestyle='--', label="Break-even")
plt.axvline(mean_npv[0], color='lightsteelblue', linestyle='--', label=f"Mean NPV = ${mean_npv[0]:,.0f}K")
plt.xlabel("Impact on NPV ($K)")
plt.ylabel("50% variation")
plt.title("Tornado Chart")
plt.legend()

plt.tight_layout()
plt.show()

