/*List of all Meets where Athletes recorder their Best Mark at*/

SELECT MeetName
FROM Athlete as a, AthleteCompeteIn as b
WHERE a.AthleteName=b.AthleteName AND
a.BestMark=b.Mark
GROUP BY MeetName;

/*Select Athletes who Competed at a Meet on Feb 22-24, 2018 who have won a race*/

SELECT Athlete.AthleteName
FROM Athlete, AthleteCompeteIn, TeamCompetedAt
WHERE Athlete.athletename LIKE 'P%'
AND Athlete.athleteName = AthleteCompeteIn.athleteName
AND AthleteCompeteIn.MeetName = TeamCompetedAt.MeetName
And AthleteCompeteIn.MeetDate = TeamCompetedAt.MeetDate
AND Athlete.AthleteName IN (SELECT AthleteName FROM AthleteCompeteIn WHERE MeetDate = 'Feb 22-24, 2018')
GROUP BY Athlete.AthleteName
HAVING COUNT(AthleteCompeteIn.Place = 1 ) >= 1;

/*list of men in the first round of the 8K event*/
select MIN(Round) AS Men8KFristRound
from Event
where Gender = 'M' and EventName = '8K';

/*all athletes that competed in the ACC Championships on October 26, 2018*/
select DISTINCT AthleteName from AthleteCompeteIn
where AthleteName IN
(select AthleteName from AthleteCompeteIn where MeetName = 'ACC Championships' and MeetDate = 'Oct 26, 2018');

/*all male Duke athletes that have a best mark of 120 seconds or better in the 800 */
select AthleteName, BestMark from Athlete
where Gender = 'M' and SchoolName = 'Duke' and Event='800'
Group by AthleteName, BestMark
having BestMark <= 120;

UPDATE School
SET SchoolName = 'GOAT University'
WHERE SchoolName = 'Duke';

UPDATE School
SET SchoolName='Duke'
WHERE SchoolName='GOAT University';

