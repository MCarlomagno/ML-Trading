import pandas_utils
import math
import numpy as np

def compute_average_daily_return(df, initial_inverstment):
	daily_return,_ = get_daily_return_and_cum_return(df, initial_inverstment)
	return daily_return.mean()

def compute_cumulative_return(df, initial_inverstment):
	_,cumulative_return = get_daily_return_and_cum_return(df, initial_inverstment)
	return cumulative_return

def compute_sharpe_ratio(df, initial_inverstment):
	daily_return,_ = get_daily_return_and_cum_return(df, initial_inverstment)

	# we assume that if you dont put money in the market you gain 0 (array of 0 with the same number of rows)
	risk_free_rate_of_return = np.zeros(daily_return.shape[0])

	return ((daily_return - risk_free_rate_of_return).mean()/ daily_return.std())

def get_sharpe_ratio(df, initial_inverstment, samples = 256):
	# by default, the sharpe ratio is computed annually
	sr = compute_sharpe_ratio(df, initial_inverstment)
	return math.sqrt(samples) * sr

def get_daily_return_and_cum_return(df, initial_inverstment, allocs = [0.1,0.2,0.3,0.3,0.1]):
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

def test_run():
	initial_inverstment = 1000000
	df = pandas_utils.create_dataframe()
	sr = get_sharpe_ratio(df, initial_inverstment)
	print(sr)



if __name__ == '__main__':
	test_run()