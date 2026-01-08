import numpy_financial as npf

# Define the cash flows
cash_flows = [-100000, -203898, 143269, 143755, 143755, 143755]

# Calculate the IRR
irr_value = npf.irr(cash_flows)

# Print the result
print(f"The IRR is: {irr_value:.4f}")
