-- Find all wineries which produce wines by possessing aromas of plum, cherry, rose, or hazelnut. To make it more simple, look only for singular form of the mentioned aromas. HINT: if one of the specified words is just a substring of another word, this should not be a hit, but a miss.

-- Example Description: Hot, tannic and simple, with cherry jam and currant flavors accompanied by high, tart acidity and chile-pepper alcohol heat.

-- Therefore the winery Bella Piazza is expected in the results.
-- Table: winemag_p1
-- Expected output

-- winery
-- Boudreaux Cellars
-- Goldeneye
-- Pine Ridge
-- Hopler
-- Bella Piazza

SELECT winery
FROM winemag_p1
WHERE description REGEXP '([^a-zA-Z0-9_]|^)plum([^a-zA-Z0-9_]|$)' OR
      description REGEXP '([^a-zA-Z0-9_]|^)cherry([^a-zA-Z0-9_]|$)' OR
      description REGEXP '([^a-zA-Z0-9_]|^)rose([^a-zA-Z0-9_]|$)' OR
      description REGEXP '([^a-zA-Z0-9_]|^)hazelnut([^a-zA-Z0-9_]|$)'
ORDER BY winery;