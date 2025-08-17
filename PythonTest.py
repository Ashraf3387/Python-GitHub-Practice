import pandas as pd
import numpy as np
# Create a DataFrame with random data
df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
# Display the DataFrame
print("DataFrame with random data:")
print(df)