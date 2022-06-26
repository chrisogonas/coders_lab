# ======================================================================================
# Program HETEROZYGOSITY: Compute heterozygosity index
# Version: 06 Jun 2022
# (c) Wolfgang Messner, University of South Carolina
# =======================================================================================

# Import libraries
import pandas as pd
from math import sqrt

# Load dataset
df = pd.read_csv('data/Testdata.csv', na_values=['N/A', ' '])  # CHANGE FILE NAME & PATH
rows = df.shape[0]
cols = df.shape[1]


# First calculation method: Vectorization
# =======================================

def vectorization():
    dd_sum = 0
    my_vals = [0 for i in range(cols)]

    # Loop through all respondents - For each row, iterate each column (vector)
    for row in range(rows):
        for col in range(cols):
            a_sum = df.iloc[:, col].loc[lambda s: s > df.iloc[row, col]].sum()
            a_count = df.iloc[:, col].loc[lambda s: s > df.iloc[row, col]].count()

            b_sum = df.iloc[:, col].loc[lambda s: s < df.iloc[row, col]].sum()
            b_count = df.iloc[:, col].loc[lambda s: s < df.iloc[row, col]].count()

            my_vals[col] = ((abs(a_sum - a_count * df.iloc[row, col]) + abs(b_sum - b_count * df.iloc[row, col])) / (
                    rows - 1)) ** 2

        dd_sum += sqrt(sum(my_vals))

    print(f'Cultural heterozygosity H = {dd_sum / rows}')


# Second calculation method: Double loop
# ======================================
def double_loop():
    my_vals_rows = [0] * rows

    for row in range(rows):
        my_vals_a = [0] * cols
        my_counts_a = my_vals_a.copy()
        my_vals_b = my_vals_a.copy()
        my_counts_b = my_vals_a.copy()
        my_vals_sum = my_vals_a.copy()

        # for each respondent
        for row_2 in range(rows):

            # for each attribute/feature, run the computation
            for col in range(cols):
                if df.iloc[row_2, col] > df.iloc[row, col]:
                    my_vals_a[col] += df.iloc[row_2, col]
                    my_counts_a[col] += 1
                if df.iloc[row_2, col] < df.iloc[row, col]:
                    my_vals_b[col] += df.iloc[row_2, col]
                    my_counts_b[col] += 1

                my_vals_sum[col] = ((abs(my_vals_a[col] - my_counts_a[col] * df.iloc[row, col]) + abs(
                    my_vals_b[col] - my_counts_b[col] * df.iloc[row, col])) / (
                                        rows - 1))
        # sum up the squared values
        my_vals_rows[row] = sqrt(sum(map(lambda x: x**2, my_vals_sum)))

    print(f'Cultural heterozygosity H = {sum(my_vals_rows) / rows}')


vectorization()
double_loop()
