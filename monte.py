import matplotlib.font_manager as fm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

fm.fontManager.addfont("/Library/Fonts/Montserrat-Regular.ttf")
mpl.rcParams['font.family'] = 'Montserrat'

# Example cash-flow means:

cf_means = np.array([-100000, -203898, 143269, 143755, 143755, 143755])

# Example with same standard deviation applied to all CFs:
stddev = 0.40  # 40% standard deviation

cf_stds = np.abs(cf_means) * stddev

discount_rate = 0.08   # 8%
num_samples = 10000         # number of Monte Carlo runs


# Monte Carlo Simulation:

# 42 = seed for reproducibility, leave blank for true randomness
rng = np.random.default_rng(42)

# Sample normally distributed cash flows for each year
cash_flows = rng.normal(
    loc=cf_means,
    scale=cf_stds,
    size=(num_samples, len(cf_means))
)

# Discount factors for each period
discount_factors = 1 / (1 + discount_rate) ** np.arange(0, len(cf_means))

# Compute NPV for every simulation
npvs = np.sum(cash_flows * discount_factors, axis=1)

risk_of_loss = np.mean(npvs < 0)

# Plot results

plt.figure(figsize=(10, 6))
plt.hist(npvs / 1e3, bins=50, color='mediumblue', edgecolor='black', alpha=0.75)
plt.title("Monte Carlo Simulation of NPV")
plt.xlabel("NPV (USD K)")
plt.ylabel("Frequency")
mean_npv_thousands= np.mean(npvs) / 1e3
plt.axvline(0, color='crimson', linestyle='--', label=f"Risk of Loss = {risk_of_loss:,.0%}")
plt.axvline(mean_npv_thousands, color='lightsteelblue', linestyle='--', label=f"Mean NPV = ${mean_npv_thousands:,.0f}K")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Print simulation results
print("Simulated Cash Flow Statistics Across All Years:")

all_simulated_cfs = cash_flows.flatten()

print(f"Mean: {np.mean(all_simulated_cfs):,.0f}")
print(f"Median: {np.median(all_simulated_cfs):,.0f}")
print(f"5th percentile: {np.percentile(all_simulated_cfs, 5):,.0f}")
print(f"95th percentile: {np.percentile(all_simulated_cfs, 95):,.0f}")
print()
# Print summary statistics

print("Summary NPV Statistics Across All Years:")

print(f"Mean NPV: {np.mean(npvs):,.0f}")
print(f"Median NPV: {np.median(npvs):,.0f}")
print(f"5th percentile NPV: {np.percentile(npvs, 5):,.0f}")
print(f"95th percentile NPV: {np.percentile(npvs, 95):,.0f}")
print(f"Risk of loss: {risk_of_loss:.1%}")

# or, find the probability of an NPV other than 0:
target_npv = 50000
prob_miss = np.mean(npvs < target_npv)
print(f"Probability of NPV less than ${target_npv / 1e3}K: {prob_miss:.1%}")

# expected loss - NPV that is the mean of NPVs less than 0
expected_loss = np.mean(npvs[npvs < 0])
print(f"Expected loss: {expected_loss:.0f}")
