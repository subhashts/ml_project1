# Step 1: Create and Save Dummy Dataset
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression

# Generate regression dataset
X, y = make_regression(
    n_samples=200,
    n_features=10,
    n_informative=5,
    noise=15,
    random_state=42
)

# Convert to DataFrame
df = pd.DataFrame(X, columns=[f'Feature_{i+1}' for i in range(X.shape[1])])
df['Target'] = y

# Save to CSV file
df.to_csv('dummy_data.csv', index=False)

print("✅ Dummy dataset saved as 'dummy_data.csv'")
