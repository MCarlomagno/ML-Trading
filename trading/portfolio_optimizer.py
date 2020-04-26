import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spo
import numpy as np
import math

def get_data_frame(start_date, end_date, symbols):
	'''Loads a custom data frame with a given date range and symbols

	Parameters:
	-----------

	start_date: start date (string date)
	end_date: end date (string date)
	symbols: simbols of the portfolio (string array)

	Return:
	-------
	pandas dataframe with date and adj close for each symbol
	
	Date   Symbol1     Symbol2 ...
	date1  adj_close1  adj_close2

	'''
	#Creating empty data frame with custom date range
	dates = pd.date_range(start_date, end_date)
	df = pd.DataFrame(index = dates)

	for symbol in symbols:
		df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col='Date',parse_dates=True, usecols=['Date', 'Adj Close'], na_values="nan")
		df_temp = df_temp.rename(columns = {'Adj Close': symbol})
		df = df.join(df_temp)

	# drops the NaN values
	df.dropna(how='any',inplace=True)
	return df

def normalize_data(df):
	'''divide each value by its first value eg. Goog[i] / Goog[0] so all values starts in 1
	'''
	return df/df.loc[df.index[0],:]

def get_daily_return_and_cum_return(df, initial_inverstment, allocs):
	normed_df = df/df.loc[df.index[0],:]
	alloced_df = normed_df * allocs
	daily_value = alloced_df * initial_inverstment
	total_daily_value = daily_value.sum(axis = 1)
	daily_return = (total_daily_value/total_daily_value.shift(1)) - 1
	daily_return = daily_return[1:]

	#other statistics
	cum_return = (total_daily_value[-1]/total_daily_value[0]) - 1
	##

	return (daily_return, cum_return)

def get_portfolio_value(norm_df, allocs, initial_inverstment):
	alloced_df = norm_df * allocs
	daily_value = alloced_df * initial_inverstment
	total_daily_value = daily_value.sum(axis = 1)
	return total_daily_value

def plot_portfolio_value(df, spy, title="Portfolio value"):
	ax = df.plot(title = title, label = "Portfolio value")
	spy.plot(label = "SPY value")
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	ax.legend(loc = "upper left")
	plt.show()

def compute_sharpe_ratio(df, initial_inverstment, allocs, samples = 256):
	daily_return,_ = get_daily_return_and_cum_return(df, initial_inverstment, allocs)

	# we assume that if you dont put money in the market you gain 0 (array of 0 with the same number of rows)
	risk_free_rate_of_return = np.zeros(daily_return.shape[0])

	return (math.sqrt(samples) * ((daily_return - risk_free_rate_of_return).mean()/ daily_return.std()))

def fun(coef, df, initial_inverstment):

	sharpe_ratio = compute_sharpe_ratio(df, initial_inverstment, coef)

	# we try to minimize the function so miltiply the sharpe ratio by -1
	return (sharpe_ratio * -1)

def fit_coefs(df, fun, initial_guess, initial_inverstment):
	# Call optimizer to minimize the function error
	result = spo.minimize(fun, initial_guess, args =(df,initial_inverstment,), bounds = ((0, 1),(0, 1),(0.0, 1),(0.0, 1)), constraints = ({ 'type': 'eq', 'fun': lambda inputs: 1.0 - np.sum(inputs) }), method= 'SLSQP', options= {'disp': True})
	return result.x


def test_run():
	start_date = '2019-06-01'
	end_date = '2020-03-01'
	symbols = ['JCP', 'GOOG', 'GLD', 'IBM']
	df = get_data_frame(start_date, end_date, symbols)
	df_spy = get_data_frame(start_date, end_date, ['SPY'])
	norm_df = normalize_data(df)
	norm_df_spy = normalize_data(df_spy)

	orig_allocs = [0.25, 0.25, 0.25, 0.25]
	reverse_optim_allocs = [0.0, 0.6, 0.4, 0.0]
	initial_inverstment = 1000000
	coefs = fit_coefs(df, fun, orig_allocs, initial_inverstment)

	print("sharpe ratio function for optimal: ")
	value1 = compute_sharpe_ratio(norm_df, initial_inverstment, coefs)
	print(value1)

	print("sharpe ratio function for reverse optimal: ")
	value2 = compute_sharpe_ratio(norm_df, initial_inverstment, reverse_optim_allocs)
	print(value2)

	reverse_portfolio_value = get_portfolio_value(norm_df, reverse_optim_allocs, initial_inverstment)
	optim_portfolio_value = get_portfolio_value(norm_df, coefs, initial_inverstment)
	spy_portfolio_value = get_portfolio_value(norm_df_spy, [1.0], initial_inverstment)
	plot_portfolio_value(optim_portfolio_value, reverse_portfolio_value)




if __name__ == '__main__':
	test_run()
