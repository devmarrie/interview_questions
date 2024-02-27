-- Find how many times each artist appeared on the Spotify ranking list
-- Output the artist name along with the corresponding number of occurrences.
-- Order records by the number of occurrences in descending order.
-- Table: spotify_worldwide_daily_song_ranking

select artist, count(*) as n_occurences
from spotify_worldwide_daily_song_ranking
group by artist
order by 2 DESC;