# I have done ml before but I have never actually learned pandas/tensorflow and followed guides. Im going to use the attached tutorials to actually learn this time.
# https://www.kaggle.com/code/residentmario/creating-reading-and-writing/tutorial
import pandas as pd

# Table
df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])
print(f"{df}\n")

# Series = table
series = pd.Series([1, 2, 3, 4, 5])

# Read csvs
reviews = pd.read_csv("train.csv")

# Size/largeness: records:columsn
print(reviews.shape)

# .head() & .tail()
print(reviews.head())

### INDEX IG

# Access properties
print(reviews.project_id.head()) # or reviews["project_id"]

# iloc - Index location (loc/iloc: row/column)
print(reviews.iloc[0])

# only columns
print(reviews.iloc[:, 0])
#reviews.iloc[1:3, 0] || reviews.iloc[[1, 3, 2], 0]

# reviews.iloc[-5:] starts at end

# Loc
print(reviews.loc[0, 'project_id']) # print first entry in reviews

# this project loc is better cayse we have meaninflful indices
print(reviews.loc[:, ["log_hours", "project_span_days"]])

print(reviews.set_index("num_commits"))

# Bool statement
print(reviews.commit_cadence == 'daily') # searching: reviews.loc[reviews.country == 'Italy']

# & = and, | = or

# .isin() lets you use a list for loc  | .notnull()