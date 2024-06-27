import constants
import pandas # data manipulation, loading csv as dataframe
from analysis import *

# Load the dataset
data_frame = pandas.read_csv(constants.data_path)
data_frame["Type 2"] = data_frame["Type 2"].fillna("None") # Replace null values in 'Type 2'' with 'None'
constants.data_frame = data_frame

power_levels = PowerLevelsAnalysis()
stats = StatsAnalysis()
counts = CountsAnalysis()

power_levels.average_power_level_analysis().save_plots()
power_levels.total_power_comparision_per_generation().save_plots()
stats.correlation_of_stats().save_plots()
counts.count_per_type().save_plots()
stats.cdfs_of_stats_for_top_pokemon().save_plots()