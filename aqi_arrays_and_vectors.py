import numpy as np
import ada_c2_labs as lab
aqi_list = lab.fetch_epa('aqi')
import ada_c2_labs as lab
aqi_list = lab.fetch_epa('aqi')

print('Max = ', np.max(aqi_array))
print('Min = ', np.min(aqi_array))
print('Median = ', np.median(aqi_array))
print('Std = ', np.std(aqi_array))

boolean_aqi = (aqi_array<=5)
percent_under_6 = boolean_aqi.sum()/len(boolean_aqi)
percent_under_6