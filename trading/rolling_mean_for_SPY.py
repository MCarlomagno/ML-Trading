import pandas_utils
import pandas as pd
import matplotlib.pyplot as plt


def get_rolling_mean(df, window=20):
	df_rolling = df.rolling(window = window)
	return df_rolling.mean()

def get_rolling_std(df, window=20):
	df_rolling = df.rolling(window=window)
	return df_rolling.std()

def get_upper_band(rmean,rstd):
	upper_band = rmean + 2 * rstd
	return upper_band

def get_lower_band(rmean,rstd):
	lower_band = rmean - 2 * rstd
	return lower_band

def test_run():
	#gets the SPY dataframe
	df = pandas_utils.get_spy_dataframe()

	#gets the rolling mean from numbers array and given window
	rmean = get_rolling_mean(df['Adj Close'],20)

	#gets the rolling standard desviation from numbers array and given window
	rstd = get_rolling_std(df['Adj Close'],20)

	#gets the bollinger upper band
	upper_band = get_upper_band(rmean, rstd)

	#gets the bollinger lower band
	lower_band = get_lower_band(rmean, rstd)


	#plots data
	ax = df['Adj Close'].plot(label="SPY Price", title = "SPY rolling mean and Bollinger bands")
	rmean.plot(label = "SPY rolling mean", ax = ax)
	upper_band.plot(label = "Bollinger upper band", ax = ax)
	lower_band.plot(label = "Bollinger lower band", ax = ax)
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	ax.legend(loc="upper left")
	plt.show()


if __name__ == '__main__':
	test_run()