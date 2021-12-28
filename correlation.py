import numpy as np
import pandas as pd

#import csv data and convert to pandas data frame
df_bayc = pd.read_csv (r'/Users/daltonnisbett/Desktop/D/CODE/Correlation/bayc-usd-90d.csv')
df_punk = pd.read_csv (r'/Users/daltonnisbett/Desktop/D/CODE/Correlation/punk-usd-90d.csv')

#delete columns from dataframe
del df_bayc['market_cap']
del df_bayc['total_volume']
del df_punk['market_cap']
del df_punk['total_volume']

#rename columns in dataframe
df_bayc = df_bayc.rename(columns={'snapped_at': 'time', 'price': 'bayc_price'})
df_punk = df_punk.rename(columns={'snapped_at': 'time2', 'price': 'punk_price'})

#merge prices dataframe
result = pd.concat([df_bayc, df_punk], axis=1)
del result['time2']

#steps: https://algotrading101.com/learn/python-correlation-guide/
result['step1'] = result.bayc_price - result.bayc_price.mean()
result['step2'] = result.punk_price - result.punk_price.mean()
result['step3'] = result.step1 * result.step2

step4 = result.step3.sum()

result['step5'] = result.step1 ** 2
result['step6'] = result.step2 ** 2

step7 = result.step5.sum() * result.step6.sum()
step8 = np.sqrt(step7)

step4/step8
result.bayc_price.corr(result.punk_price)

print(step4/step8)
print(result.bayc_price.corr(result.punk_price))