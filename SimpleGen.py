import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(0)

# Generate mock data
data = {
    "Patient_ID": range(1, 101),
    "Age": np.random.randint(20, 80, 100),
    "Diagnosis": np.random.choice(["Breast Cancer", "Lung Cancer", "Prostate Cancer", "Colon Cancer"], 100),
    "Treatment": np.random.choice(["Chemotherapy", "Radiation", "Surgery", "Immunotherapy"], 100),
    "Outcome": np.random.choice(["Improved", "Stable", "Worsened", "Deceased"], 100)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV (optional)
df.to_csv("oncology_data.csv", index=False)
