<!-- USAGE EXAMPLES -->
# RU-Free📅

<!-- Overview -->
## Overview

I got tired of checking my friends schedule manually to see when I could hang out with them, so I decided to create a fix.

I sent a request to the Rutgers API which has all courses offered at Rutgers and parsed through the JSON file to find the index which matched the user's index input.

Here is a snippet of one object, which would be a section of a course.

```
[
	{
		"campusLocation": "1",
		"roomNumber": "2160",
		"campusAbbrev": "CAC",
		"campusName": "COLLEGE AVENUE",
		"startTimeMilitary": "0830",
		"buildingCode": "AB",
		"meetingModeDesc": "LEC",
		"endTimeMilitary": "0950",
		"meetingModeCode": "02",
		"baClassHours": "",
		"pmCode": "A",
		"meetingDay": "M",
		"startTime": "0830",
		"endTime": "0950"
	}
]
```

The following code,
```
example_list = ['07249', '19922']
name = "Person 1"
person_one_schedule = all_course_times(example_list, name)
```
woud return:

```
[{'campusNames': 'COLLEGE AVENUE',
   'courseName': 'DATA STRUCTURES',
   'endTime': '09:50 AM',
   'meetingDay': 'M',
   'personName': 'Person 1',       
   'startTime': '08:30 AM'},       
  {'campusNames': 'COLLEGE AVENUE',
   'courseName': 'DATA STRUCTURES',
   'endTime': '09:50 AM',
   'meetingDay': 'H',
   'personName': 'Person 1',       
   'startTime': '08:30 AM'},       
  {'campusNames': 'BUSCH',
   'courseName': 'DATA STRUCTURES',
   'endTime': '08:40 PM',
   'meetingDay': 'H',
   'personName': 'Person 1',
   'startTime': '07:45 PM'}],
   
 [{'campusNames': 'BUSCH',
   'courseName': 'INTR DISCRET STRCT I',
   'endTime': '08:50 PM',
   'meetingDay': 'M',
   'personName': 'Person 1',
   'startTime': '07:30 PM'},
  {'campusNames': 'BUSCH',
   'courseName': 'INTR DISCRET STRCT I',
   'endTime': '08:50 PM',
   'meetingDay': 'W',
   'personName': 'Person 1',
   'startTime': '07:30 PM'},
  {'campusNames': 'BUSCH',
   'courseName': 'INTR DISCRET STRCT I',
   'endTime': '03:10 PM',
   'meetingDay': 'T',
   'personName': 'Person 1',
   'startTime': '02:15 PM'}]
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>















