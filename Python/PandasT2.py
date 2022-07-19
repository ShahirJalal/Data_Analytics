import pandas as pd
import numpy as np

df5 = pd.DataFrame({'Team' : ['TeamA', 'TeamB', 'TeamA', 'TeamB',
                           'TeamA', 'TeamB', 'TeamA', 'TeamB'],
                    'Month' : ['Jan', 'Jan', 'Feb', 'Feb',
                           'Mar', 'Mar', 'Apr', 'Apr'],
                    'Sales' : np.random.normal(80, 20, 8),
                    'Profit' : np.random.normal (20,20,8)})

print(df5)