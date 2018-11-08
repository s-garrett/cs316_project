/*all athletes that competed in the ACC Championships on October 26, 2018*/
select DISTINCT AthleteName from AthleteCompeteIn
where AthleteName IN
(select AthleteName from AthleteCompeteIn where MeetName = 'ACC Championships' and MeetDate = 'Oct 26, 2018');