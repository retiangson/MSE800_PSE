import numpy as np

rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

rainfallArray = np.array(rainfall)
print("Rainfall array:", rainfallArray)

totalRainfall = np.sum(rainfallArray)
print("Total rainfall for the week:", np.round(totalRainfall, 2), "mm")

averageRainfall = np.mean(rainfallArray)
print("Average rainfall for the week:", np.round(averageRainfall, 2), "mm")

noRainDays = np.count_nonzero(rainfallArray == 0)
print("Number of days with no rain:", noRainDays)

highRainfallDays = np.where(rainfallArray > 5.0)[0]
print("More than 5 mm rainfall:", highRainfallDays)

percentile75 = np.percentile(rainfallArray, 75)
print("75th percentile of rainfall:", percentile75)

above75 = rainfallArray[rainfallArray > percentile75]
print("More than 75th percentile:", above75)