SELECT Athlete 
FROM Athlete, AthleteCompeteIn, TeamCompetedAt
WHERE Athlete.name LIKE "t%"
AND Athlete.Name = AthleteCompeteIn.Name
AND AthleteCompeteIn.MeetName = TeamCompetedAt.MeetName
And AthleteCompeteIn.MeetDate = TeamCompetedAt.MeetDate
AND Athlete.AthleteName IN (SELECT * FROM AthleteCompeteIn WHERE MeetDate = "Feb 22-24, 2018")
HAVING COUNT(AthleteCompeteIn.Place = 1 ) >= 1;
