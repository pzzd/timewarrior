# I, TimeWarrior

I use [TimeWarrior](https://timewarrior.net) because I like to start and stop a timer while I am working. I use accurate time records later (sometimes much later!) to estimate time on similar projects. But I also need to record time for my job.

By default, data is saved to ~/.local/share/timewarrior. It's not a bad idea to back this data up periodically.

## Record time with timer

I use a tag like '[client] [project] [type of work]'.

`timew start 'self stub-app composer-dependency'`

Later, if I need to report by client or by project, I can split up the tag for queries.


## Report hours

Here is a python script to export my timer data so I can report it to my org's timesheet software. We have to report hours per project per day.

Send TimeWarrior data to json file:

`timew export 2024-02-19 | python3 timew-report-for-workotter.py`

Output gives time spent on a project on the given day.
```
self prof-dev combinatorics 0:00:30
self php-8.3 fws 0:01:00
f&a admin time-tracking 0:00:30
self php-8.3 study-abroad 0:00:21.333333
uc-comms intranet reindex 0:02:47.533333
```

## TODO

- convert time to floats

