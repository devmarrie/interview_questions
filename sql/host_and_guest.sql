-- Find matching hosts and guests pairs in a way that they are both of the same gender and nationality.
-- Output the host id and the guest id of matched pair.
-- Tables: airbnb_hosts
-- host_id:int
-- nationality:varchar
-- gender:varchar
-- age:int

-- airbnb_guests
-- guest_id:int
-- nationality:varchar
-- gender:varchar
-- age:int

select distinct h.host_id, g.guest_id
from airbnb_hosts h
inner join airbnb_guests g
on h.gender = g.gender and h.nationality = g.nationality;