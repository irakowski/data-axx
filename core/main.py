import pandas as pd
import constants

#%%
df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],index=['row 1', 'row 2'],columns=['col 1', 'col 2'])

#%%
df1.to_excel(constants.OUTPUT_PATH)





             