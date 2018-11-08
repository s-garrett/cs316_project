/*List of all Meets where Athletes recorder their Best Mark at*/

SELECT MeetName
FROM Athlete as a, AthleteCompeteIn as b
WHERE a.AthleteName=b.AthleteName AND
a.BestMark=b.Mark
GROUP BY MeetName;