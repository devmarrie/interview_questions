-- Count the number of movies that Abigail Breslin was nominated for an oscar.
-- Table: oscar_nominees
-- year:int
-- category:varchar
-- nominee:varchar
-- movie:varchar
-- winner:bool
-- id:int

select count(*) as n_movies_by_abi from oscar_nominees
where nominee = 'Abigail Breslin';