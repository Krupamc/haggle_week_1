# I have done ml before but I have never actually learned pandas/tensorflow and followed guides. Im going to use the attached tutorials to actually learn this time.
import pandas as pd

# Table
df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])
print(df)

# Series = table
series = pd.Series([1, 2, 3, 4, 5])

# Read csvs
reviews = pd.read_csv("../train.csv")

# Size/largeness
reviews.shape