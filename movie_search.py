from os import error
import requests 
import pandas as pd
from pprint import pprint
from bs4 import BeautifulSoup
import numpy as np
import omdb
import csv
import matplotlib.pyplot as plt
import re
 
# Scraping information from wikipedia to get the titles of movies

url = "https://en.wikipedia.org/wiki/2000s_in_film"
r = requests.get(url)
search_info= r.text
soup = BeautifulSoup(search_info, features="lxml")
x = soup.get_text()

# Slicing the required part and storing to a txt file 

with open(r"wiki.txt", mode = "r", encoding="utf-8") as textfile:
    file = textfile.read().split("\n")
adj = file[333:984]
adj = list(filter(None, adj))
c = np.array_split(adj, 50)
title = [c[i][1] for i in range(len(c))]
with open(r"names.txt", mode = "w") as adjust:
    for i in title:
        adjust.write(f"{i}\n")

# Retrieving the data stored to pass to omdbapi 

with open(r"names.txt") as title:
    title2 = title.read().split("\n")

#  Obtaining information from the given title and storing to a csv file  

for diy in title2:
    r = requests.get(f"http://www.omdbapi.com/?i=tt3896198&apikey=72bc447a&t={str(diy)}")
    doc = r.json()
    df = pd.DataFrame([doc])
    fields = list(doc.keys())
    row = [i for i in doc.values()]
    with open(r"hoping12.csv", mode = "a") as textfile:
            writer = csv.writer(textfile)
            writer.writerow(row)

# Trying to make sense of the information by cleaning some of the columns  

df['BoxOffice'] = df['BoxOffice'].str.replace('$', '', regex=True).str.replace(',', '', regex=True)
df['BoxOffice'] = pd.to_numeric(df['BoxOffice'], errors="raise")
df['imdbVotes'] = df['imdbVotes'].str.replace(',', '', regex=True)
df['imdbVotes'] = pd.to_numeric(df['imdbVotes'], errors="raise")
df = pd.read_csv(r"hoping12.csv")
filtered = df[["Title", "Genre", "imdbRating", "imdbVotes",  "BoxOffice"]]
rated = filtered[filtered.imdbRating >= 7 ]
ratedvotes = rated[rated.imdbVotes >= 500000]
boxed = ratedvotes[ratedvotes.BoxOffice >= 1000000]
plt.scatter(df["imdbVotes"],df["BoxOffice"])
plt.ylabel("BoxOffice")
plt.xlabel("imdbVotes")
plt.show()