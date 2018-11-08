/*all male Duke athletes that have a best mark of 3 or lower/better */
select * from Athlete
where Gender = "M" and SchoolName = "Duke"
group by BestMark
having BestMark <= 3