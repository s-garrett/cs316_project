/*list of women in the first round of the 8K event*/
select MIN(Round) AS Womens8KFristRound
from Event
where Gender = "F" and EventName = "8K"