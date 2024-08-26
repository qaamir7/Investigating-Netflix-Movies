import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

movies_only = netflix_df[netflix_df['type']=='Movie']
movies_1990s = netflix_df[np.logical_and(netflix_df['release_year']>=1990,netflix_df['release_year']<=1999)]

plt.hist(movies_1990s['duration'])
plt.xlabel('Duration of Movie (mins)')
plt.ylabel('Number of Movies')
plt.show()

# From histogram, we can see number of movies is highest(around 50) for the duration of around 100 minutes. 
Duration = 100

movies_action = movies_1990s[movies_1990s['genre']=='Action']

short_action_movieCount = 0
for label, row in movies_action.iterrows():
    if row['duration'] < 90:
        short_action_movieCount = short_action_movieCount+1
    else:
        short_action_movieCount = short_action_movieCount

print(short_action_movieCount)        

