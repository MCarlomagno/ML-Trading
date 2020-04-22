import pandas as pd
import numpy as np
import pandas_utils

def test_run():
	date_range = pandas_utils.get_dates_range()
	df = pandas_utils.create_dataframe()
	print("mean:")
	print(df.mean())
	print("median:")
	print(df.median())
	print("std:")
	print(df.std())
	pandas_utils.plot_data(df)



if __name__ == '__main__':
	test_run()