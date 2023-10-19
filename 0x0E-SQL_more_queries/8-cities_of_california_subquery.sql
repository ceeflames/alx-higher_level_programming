-- Script that list all cities of CA in the database
-- results are ordered ASC ascending
SELECT `id`, `name`
	FROM `cities`
	WHERE `state_id` IN
		(SELECT `id`
			FROM `states`
			WHERE `name` = "California")
	ORDER BY `id`;
