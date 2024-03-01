-- Find the Olympics with the highest number of athletes. 
-- The Olympics game is a combination of the year and the season, and is found in the 'games' column. 
-- Output the Olympics along with the corresponding number of athletes.
-- Table: olympics_athletes_events

select games, count(distinct name) as  athletes_count
from olympics_athletes_events
group by games
order by 2 desc
limit 1;