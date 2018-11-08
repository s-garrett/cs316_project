/*all athletes that competed in the ACC Championships on October 26, 2018*/
select AthleteName from AthleteCompetedIn
where EXISTS
(select MeetName from Meet where MeetName = "ACC Championships" and MeetDate = "Oct 26, 2018")