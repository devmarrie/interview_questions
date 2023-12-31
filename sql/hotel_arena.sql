-- Find the number of rows for each review score earned by 'Hotel Arena'. 
-- Output the hotel name (which should be 'Hotel Arena'), 
-- review score along with the corresponding number of rows with that score for the specified hotel.
-- Table: hotel_reviews

-- Expected Output
-- hotel_name	reviewer_score	count(*)
-- Hotel Arena	7.5	2
-- Hotel Arena	9.6	2
-- Hotel Arena	4.6	1
-- Hotel Arena	3.8	1
-- Hotel Arena	4.2	1

select hotel_name, reviewer_score, count(*)
from hotel_reviews
where hotel_name = 'Hotel Arena'
group by reviewer_score;