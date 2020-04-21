import pandas as pd
import matplotlib.pyplot as plt

def test_run():
	'''
	Test run function
	'''
	create_dataframe()


def plot_data():
	'''
	Plot data function
	'''
	df = pd.read_csv("data/JCP.csv")
	df[['Close','High']].plot()
	plt.show()

def get_mean_close():
	'''
	get mean close function
	'''
	df = pd.read_csv("data/JCP.csv")
	return df['Close'].mean()

def get_max_close():
	'''
	get max close function
	'''
	df = pd.read_csv("data/JCP.csv")
	return df['Close'].max()

def get_dates_range():
	'''
	date range function
	'''
	start_date = '2019-06-01'
	end_date = '2020-03-01'
	dates = pd.date_range(start_date, end_date)
	return dates

def get_spy_dataframe():
	df = pd.read_csv("data/SPY.csv",index_col= 'Date', parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
	return df

def create_dataframe():
	#Creating empty data frame with custom date range
	df = pd.DataFrame(index = get_dates_range())

	symbols = ['JCP', 'GOOG', 'GLD', 'SPY', 'IBM']

	for symbol in symbols:
		df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col='Date',parse_dates=True, usecols=['Date', 'Adj Close'], na_values="nan")
		df_temp = df_temp.rename(columns = {'Adj Close': symbol})
		df = df.join(df_temp)

	# drops the NaN values
	df.dropna(how='any',inplace=True)
	print(df)


if __name__ == "__main__":
    test_run()