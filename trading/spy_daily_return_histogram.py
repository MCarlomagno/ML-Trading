import pandas as pd
import pandas_utils
import matplotlib.pyplot as plt
import daily_return_for_SPY

def compute_stats(symbol, dr):
	mean = dr[symbol].mean()
	std = dr[symbol].std()
	kur = dr[symbol].kurtosis()
	print("daily return mean: " + str(mean))
	print("daily return std: " + str(std))
	print("daily return kurtosis: " + str(kur))
	return (mean,std,kur)

def plot_comparing_histogram(mean, std, dr, df):
	#dr.plot()
	
	dr['GOOG'].hist(bins=20, label = 'GOOG')
	dr['SPY'].hist(bins=20,label = 'SPY')
	plt.axvline(mean,linewidth=2,color="w", linestyle="dashed")
	plt.axvline(mean + std ,linewidth=2,color="r", linestyle="dashed")
	plt.axvline(mean - std ,linewidth=2,color="r", linestyle="dashed")
	#df.plot()
	plt.legend(loc = 'upper right')
	plt.show()

def get_all_data():
	return pandas_utils.create_dataframe()

def get_spy_data():
	return pandas_utils.get_spy_dataframe()

def test_run():
	df = get_all_data()
	dr = daily_return_for_SPY.compute_daily_return_pandas(df)
	mean, std, kur = compute_stats('SPY', dr)
	plot_comparing_histogram(mean, std, dr, df)

if __name__ == '__main__':
	test_run()