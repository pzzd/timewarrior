#!/usr/bin/env python

from datetime import datetime
import json
import sys



data = sys.stdin.read()
decoded = json.loads(data);

# project_hours looks like {'client project desc': 1:50, 'client 2 proj2 desc': .54 }
# key is timewtag and value is cumulative time
project_hours = dict()


for item in decoded:

	# timew date looks like 20240220T214303Z	
	start = datetime.strptime(item['start'], '%Y%m%dT%H%M%SZ')
	end = datetime.strptime(item['end'], '%Y%m%dT%H%M%SZ')
	interval = end - start
	timedelta = interval

	project = item['tags'][0]
	key = project_hours.get(project)
	if key != None:
		timedelta = project_hours[project] + interval

	project_hours.update( { project : timedelta } )


for key in project_hours:
	hours = project_hours[key] / 60
	print(key, hours)

