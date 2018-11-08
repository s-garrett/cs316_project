SELECT TeamCompetedAt.Name
FROM Event as a, Meet as b, TeamCompetedAt as c
WHERE a.MeetName = b.MeetName
AND c.MeetName = b.MeetTime
AND c.SchoolName = 'Duke'
And c.WomenPlace = 1;