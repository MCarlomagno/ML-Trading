import matplotlib.pyplot as plt
import pandas_utils
import numpy as np
import daily_return_for_SPY

def compute_correlation(df):
	correlation = df.corr(method = 'pearson')
	print(correlation)


def test_run():
	df = pandas_utils.create_dataframe()
	dr = daily_return_for_SPY.compute_daily_return_pandas(df)
	dr.dropna(inplace=True)

	#draws the point clousters between SPY and GOOG dailies returns
	dr.plot(kind = 'scatter', x= 'SPY', y= 'GOOG')

	#gets the m and h values of linear function (y = mx + h)
	alpha_GOOG, beta_GOOG = np.polyfit(dr['SPY'],dr['GOOG'], 1)

	compute_correlation(dr)

	# plots a line (x,y,line_type, color)
	plt.plot(dr['SPY'], dr['SPY']*alpha_GOOG + beta_GOOG, '-', color = 'r')
	plt.show()

if __name__ == '__main__':
	test_run()