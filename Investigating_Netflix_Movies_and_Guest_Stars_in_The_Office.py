# Create the years and durations lists
years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary with the two lists
movie_dict = {
    "years": years,
    "durations": durations
}

# Import pandas under its usual alias
import pandas as pd

# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)

# Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt
fig = plt.figure()

# Draw a line plot of release_years and durations
plt.plot(durations_df['years'], durations_df['durations'])

# Create a title
plt.title("Netflix Movie Durations 2011-2020")

# Show the plot
plt.show()

# Read in the CSV as a DataFrame
netflix_df = pd.read_csv(r"datasets/netflix_data.csv")

# Print the first five rows of the DataFrame
print(netflix_df.head(5))

netflix_df_movies_only = netflix_df[netflix_df.type == "Movie"]
# print(netflix_df_movies_only.head(5))
netflix_movies_col_subset = netflix_df_movies_only[["title", "country", "genre", "release_year", "duration"]]
print(netflix_movies_col_subset.head(5))

# Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"])
plt.title( "Movie Duration by Year of Release")
plt.xlabel("Release_year")
plt.ylabel("Duration")
plt.show()

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset.duration < 60]

# Print the first 20 rows of short_movies
print(short_movies.head(20))

# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
colors = []
for gen in netflix_movies_col_subset["genre"]:
    if gen == "Children":
        colors.append("red")
    elif gen == "Documentaries":
        colors.append("blue")
    elif gen == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")
# Inspect the first 10 values in your list        
print(colors[0:10])

# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], c = colors, alpha = 0.8)

# Create a title and axis labels
plt.title( "Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Show the plot
plt.show()

# Are we certain that movies are getting shorter?
are_movies_getting_shorter = "YES THEY ARE GETTING SHORTER"



'https://app.datacamp.com/workspace/w/84b40707-db85-47e0-bbd0-225100307093/edit'