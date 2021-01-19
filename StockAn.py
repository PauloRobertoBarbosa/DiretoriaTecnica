import datetime as dt
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2020, 3, 1)
end = dt.datetime(2020, 12, 31)

df = web.DataReader('AZUL4.SA', 'yahoo', start, end)
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

print(df_ohlc.head())
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
# ax1 = plt.subplot2grid((6,1), (0, 0), rowspan=5, colspan=1)
# ax2 = plt.subplot2grid((6,1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])

# plt.show()
# df.dropna(inplace = True)
# print(df.head())

# df['Adj Close'].plot()
# plt.show()