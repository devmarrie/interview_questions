-- What is the overall friend acceptance rate by date? 
-- Your output should have the rate of acceptances by the date the request was sent. 
-- Order by the earliest date to latest.

-- Assume that each friend request starts by a user sending (i.e., user_id_sender) 
-- a friend request to another user (i.e., user_id_receiver) 
-- that's logged in the table with action = 'sent'. 
-- If the request is accepted, the table logs action = 'accepted'. 
-- If the request is not accepted, no record of action = 'accepted' is logged.

-- Table: fb_friend_requests                                                                                                                                                                                                             user_id_sender	user_id_receiver	date	action
-- ad4943sdz	948ksx123d	2020-01-04	sent
-- ad4943sdz	948ksx123d	2020-01-06	accepted
-- dfdfxf9483	9djjjd9283	2020-01-04	sent
-- dfdfxf9483	9djjjd9283	2020-01-15	accepted
-- ffdfff4234234	lpjzjdi4949	2020-01-06	sent
-- fffkfld9499	993lsldidif	2020-01-06	sent
-- fffkfld9499	993lsldidif	2020-01-10	accepted
-- fg503kdsdd	ofp049dkd	2020-01-04	sent
-- fg503kdsdd	ofp049dkd	2020-01-10	accepted
-- hh643dfert	847jfkf203	2020-01-04	sent
-- r4gfgf2344	234ddr4545	2020-01-06	sent
-- r4gfgf2344	234ddr4545	2020-01-11	accepted

-- Expected output:
-- date	count(a.user_id_receiver)/count(b.user_id_sender)
-- 2020-01-04	0.75
-- 2020-01-06	0.667    