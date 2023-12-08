-- You are given a table of product launches by company by year. 
-- Write a query to count the net difference between the number of products companies 
-- launched in 2020 with the number of products companies launched in the previous year. 
-- Output the name of the companies and a net difference of net products released for 2020 compared to the previous year.
-- year	company_name	product_name
-- 2019	Toyota	Avalon
-- 2019	Toyota	Camry
-- 2020	Toyota	Corolla
-- 2019	Honda	Accord
-- 2019	Honda	Passport
with nine  as (
select year as yr, company_name, count(product_name)  as ntt
from car_launches
where year = 2019
group by company_name
),
twenty  as (
select year as yr, company_name, count(product_name)  as tt
from car_launches
where year = 2020
group by company_name
)
select t.company_name, t.tt - n.ntt as total_launch
from twenty t
inner join nine n
on t.company_name = n.company_name