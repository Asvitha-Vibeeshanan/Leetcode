
select b.book_id, 
       b.title, 
       b.author, 
       b.genre, 
       b.pages, 
       max(r.session_rating) - min(r.session_rating) as rating_spread,
       round(sum(case when r.session_rating >= 4 or r.session_rating <= 2 then 1 else 0 end)*1.0/count(r.session_id), 2) as polarization_score
from books b
join reading_sessions r on b.book_id = r.book_id
group by b.book_id, b.title, b.author, b.genre, b.pages
having count(r.session_id) >=5
       and max(r.session_rating) >= 4
       and min(r.session_rating) <= 2
       and (sum(case when r.session_rating >= 4 or r.session_rating <= 2 then 1 else 0 end) * 1.0 /count(r.session_id)) >= 0.6
ORDER BY 
    polarization_score DESC,
    b.title DESC;


-- SELECT b.book_id,
--     b.title,
--     b.author,
--     b.genre,
--     b.pages,
--     MAX(r.session_rating) - MIN(r.session_rating) AS rating_spread,
--     ROUND(
--         SUM(CASE WHEN r.session_rating <= 2 OR r.session_rating >= 4 THEN 1 ELSE 0 END) * 1.0 
--         / COUNT(r.session_id), 
--         2
--     ) AS polarization_score
-- FROM books b
-- JOIN reading_sessions r 
--     ON b.book_id = r.book_id
-- GROUP BY b.book_id, b.title, b.author, b.genre, b.pages
-- HAVING 
--     COUNT(r.session_id) >= 5                                       -- at least 5 sessions
--     AND MAX(r.session_rating) >= 4                                 -- has a high rating
--     AND MIN(r.session_rating) <= 2                                 -- has a low rating
--     AND (SUM(CASE WHEN r.session_rating <= 2 OR r.session_rating >= 4 THEN 1 ELSE 0 END) * 1.0 
--          / COUNT(r.session_id)) >= 0.6                             -- polarization score ≥ 0.6
-- ORDER BY 
--     polarization_score DESC,
--     b.title DESC;

