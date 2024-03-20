-- Make a report showing the number of survivors and non-survivors by passenger class.

-- Classes are categorized based on the pclass value as:

-- pclass = 1: first_class

-- pclass = 2: second_classs

-- pclass = 3: third_class

-- Output the number of survivors and non-survivors by each class.
-- Table: titanic

with cte as (
select passengerid, survived, 
case when pclass = 1 then 'first_class' 
     when pclass = 2 then 'second_class' 
    else 'third_class' end as class
from titanic
)
select survived,
    sum(case when class = 'first_class' then 1 else 0 end) as first_class,
    sum(case when class = 'second_class' then 1 else 0 end) as second_class,
    sum(case when class = 'third_class' then 1 else 0 end) as third_class
from cte
group by survived
