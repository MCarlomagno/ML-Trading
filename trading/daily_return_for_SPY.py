import pandas as pd
import matplotlib.pyplot as plt
import pandas_utils

def compute_daily_return_classic(df):
	daily_return = df.copy()
	daily_return = (df[1:]/df[:-1].values) - 1
	daily_return[0] = 0 #if we want to use a multi variable dataframe we need daily_return[0,:] and so on for each dimension
	return daily_return

def compute_daily_return_pandas(df):
	daily_return = (df/df.shift(1)) - 1
	return daily_return

def test_run():
	#gets the SPY dataframe
	df = pandas_utils.get_spy_dataframe()

	#compute the daily return with the given dataframe
	daily_return = compute_daily_return_pandas(df['Adj Close'])

	#plots data
	ax = daily_return.plot(label="Daily Return", title = "SPY daily return")
	plt.show()

if __name__ == '__main__':
	test_run()