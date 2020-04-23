import pandas as pd
import matplotlib.pyplot as plt

def get_fake_data():
	return pd.read_csv("data/incomplete_data/fakeSPY.csv", usecols=['Date', 'Adj Close'],index_col="Date", na_values="nan", parse_dates=True)

def test_run():
	df = pd.DataFrame()
	df = get_fake_data()

	###### IMPORTANT ######
	# Always fill first in ffill and then in bfill

	# method ffill fills in forward direction (empty values after a valid value)
	df.fillna(method="ffill", inplace=True)

	# method bfill fills in back direction (empty values before a valid value)
	df_data.fillna(method="bfill", inplace=True)
	df.plot()
	plt.show()


if __name__ == '__main__':
	test_run()