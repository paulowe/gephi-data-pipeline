# Gephi data pipeline
This is a notebook that mines data from twitter and preprocesses it into the right form for network analysis on Gephi

## Workflow Overview
1. Identify users in the network by querying for hashtags, parts-of-speech, and other indicators using twint (OSINT)
2. Extract list of users. Because twint's followers/following functionality is broken, I am borrowing code I wrote from a previous client I wrote using tweepy API to extract each user's followers/following list. You may access the full repo of this client here -> www.github.com/paulowe/mining-twitter
3. Create network by populating nodes.csv and edges.csv

After this point, you easily import your files to Gephi for further network analysis such as calculating PageRank, HITS and visualizing your network.

