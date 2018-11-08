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
