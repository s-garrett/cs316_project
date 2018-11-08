COPY AthleteCompeteIn
FROM '/home/vagrant/Downloads/ACCmendistance.csv' DELIMITER ',' CSV HEADER;

INSERT INTO Athlete
SELECT AthleteName, SchoolName, Gender, MIN(Mark), EventName
FROM AthleteCompeteIn
WHERE Mark>0 GROUP BY AthleteName, SchoolName, Gender, EventName;

INSERT INTO School SELECT DISTINCT(SchoolName) FROM AthleteCompeteIn;

INSERT INTO Meet SELECT MeetName, MeetDate, Sport FROM AthleteCompeteIn GROUP BY MeetName, MeetDate, Sport; 

INSERT INTO Event SELECT EventName, Round, Gender, MeetName, MeetDate FROM AthleteCompeteIn GROUP BY EventName, Round, Gender, MeetName, MeetDate;

INSERT INTO TeamCompetedAt SELECT MeetName, MeetDate, SchoolName FROM AthleteCompeteIn GROUP BY MeetName, MeetDate, SchoolName;

CREATE INDEX pbs ON Athlete(BestMark);
