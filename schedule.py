
from datetime import datetime
from pprint import pprint
from time import time

import requests as re

year = str(datetime.today().year)
month = int(datetime.today().month)

# spring-term 1, fall-term 9
if month < 6:
    term = 1
else:
    term = 9

url = "https://sis.rutgers.edu/soc/api/courses.json"

querystring = {"year":year,
               "term":term,
               "campus":"NB"} # Newark: NK
                              # Camden: CM

#sends get response to URL
response = re.get(url, params=querystring)
data = response.json()

#takes index and returns information about the individual course
def find_course_times(index, name):
    course_info = []

    for x in range(0, len(data)):
        for y in range(len(data[x]['sections'])):
            
            if(index == data[x]['sections'][y]['index']):        
                for z in range(len(data[x]['sections'][y]['meetingTimes'])):
                        
                    course_info.append({
                                        'personName':name,
                                        'courseName':data[x]['title'], 
                                        'campusNames':data[x]['sections'][y]['meetingTimes'][z]['campusName'],
                                        'startTime':datetime.strptime(data[x]['sections'][y]['meetingTimes'][z]['startTimeMilitary'], "%H%M").strftime("%I:%M %p"), 
                                        'endTime':datetime.strptime(data[x]['sections'][y]['meetingTimes'][z]['endTimeMilitary'], "%H%M").strftime("%I:%M %p"), 
                                        'meetingDay':data[x]['sections'][y]['meetingTimes'][z]['meetingDay']})
                    
    return course_info


# takes list of index and calls 'find_course_times' to combine all courses
def all_course_times(index_list, name):
    all_courses_times = []

    for x in range(0, len(index_list)):
        all_courses_times.append(find_course_times(index_list[x], name))

    return all_courses_times

# number of all courses.

example_list = ['07249', '19922']
name = "Person 1"

pprint(all_course_times(example_list, name))