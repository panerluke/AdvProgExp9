import pandas as pd

dct = {
       'Box': ['Box1', 'Box1', 'Box1', 'Box2', 'Box2', 'Box2'],
       'Dimension': ['Length', 'Width', 'Height', 'Length', 'Width', 'Height'],
       'Value': [6, 4, 2, 5, 3, 4]
       }

messy = pd.DataFrame(dct, columns = ['Box', 'Dimension', 'Value'])

tidy = messy.pivot_table(index = 'Box', columns = 'Dimension', values = 'Value').reset_index()
height = tidy['Height']
tidy = tidy.drop(columns = 'Height')
tidy = pd.concat([tidy, height], axis = 1)
tidy['Volume'] = tidy.Length * tidy.Width * tidy.Height