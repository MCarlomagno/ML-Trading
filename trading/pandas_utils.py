import pandas as pd
import matplotlib.pyplot as plt

def test_run():
	'''
	Test run function
	'''
	df = create_dataframe()
	plot_data(normalize_data(df))


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

def slicing():
	df = create_dataframe()
	sliced_rows = df['2019-08-01':'2019-08-05']
	print("sliced_rows")
	print(sliced_rows)

	sliced_columns = df[['SPY','GOOG']]
	print("Sliced columns")
	print(sliced_columns)

	slided_rows_and_columns = df.loc['2019-08-01':'2019-08-05', ['SPY','GOOG']]
	print(slided_rows_and_columns)

def plot_data(df, title="Stock Prices"):
	ax = df.plot(title = title)
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	plt.show()

def normalize_data(df):
	return df/df.loc[df.index[0],:]

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
	return df


if __name__ == "__main__":
    test_run()