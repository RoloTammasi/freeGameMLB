# freeGameMLB
Python script to check the "Free Game of the Day" on MLB.tv


### To use:

1. Create an email.txt file and a pw.text file which store your gmail address and password, respectively. Store them in the same directory as the freeGameMLB.py script.

2. Edit the `my_team` variable inside freeGameMLB.py

3. Create a cron job (`$ crontab -e`) like this: 

`02 5 * * * PYTHONPATH=/path/where/bs4/is/stored python /path/to/freeGameMLB.py`

(this cron job will run at 5:02AM every day)


### Note:

This script also checks for the "Facebook Game of the Week" and any games broadcast on national television (FOX or ESPN).
