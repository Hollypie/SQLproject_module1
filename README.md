## Overview

This project was an experiment with working with SQlite as a database option for a small gaming project I eventually wish to do with C# and Unity.  I decided it would be easier to code this in Python first as a demo before attempting a more complicated project in C#. I also attempted some experiements in working with PostgreSQL, some of which can be seen in my python_to_prostgres.py file, something that was eventually abandoned in favor of the SQlite.

My project which is in main.py is a leaderboard maintenance program.  It generates a leaderboard that the user can view. The user can view the scores in a range of dates, add new game sessions, and delete a player. 

I would like the ability to display a leaderboard with my Unity game, so I created this one to demo the organization of my game data for my bigger project. 

I separated database connection logic (db.py), schema creation (schema.py), seed data (seed.py), and query operations (repository.py) into separate modules to improve encapsulation, reduce accidental data modification, and make the code easier to maintain and extend for future Unity integration.

{Provide a link to your YouTube demonstration. It should be a one minute demo of the software running and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

## Development Environment

SOFTWARE
VS code
Github
Git
PostgreSQL
SQlite

LANGUAGES
Python language
SQL scripting

## Useful Websites

{Make a list of websites that you found helpful in this project}

- [PostgreSQL documentation](https://www.postgresql.org/docs/current/)
- [Crash Course PostgreSQL youtube video](https://www.youtube.com/watch?v=miEFm1CyjfM)
- [Connect to PostgreSQL from Python](https://www.youtube.com/watch?v=M2NzvnfS-hI)
- [SQlite documentation](https://www.sqlite.org/docs.html)
- [Python Documentation](https://docs.python.org/3/)
- [Python code cheat sheet](https://www.datacamp.com/cheat-sheet/getting-started-with-python-cheat-sheet?utm_cid=22770233230&utm_aid=187827285531&utm_campaign=230119_1-ps-other~dsa-tofu~cheat-sheet_2-b2c_3-nam_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=9029718-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-other~nam-en~dsa~tofu~cheat-sheet~python&gad_source=1&gad_campaignid=22770233230&gbraid=0AAAAADQ9WsEty7pwmb8Y20CqIHt_G9J_H&gclid=CjwKCAiAybfLBhAjEiwAI0mBBo52UggdhU-ih3Kqr-bMLiTB7LziL98DL3R_j7OY6ysPyw9vUsORCxoCn8wQAvD_BwE)
- [Stack Overflow - python help](https://stackoverflow.com/search?q=if+statement+python&s=8e2acfee-01c8-4a69-8d66-5942725c9e45)
- [Web Site Name](http://url.link.goes.here)


## Useful Search Terms

PostgreSQL Basics -

“PostgreSQL tutorial for beginners”
“PostgreSQL CREATE TABLE INSERT SELECT tutorial”
“SQL joins and aggregate functions PostgreSQL tutorial”
“PostgreSQL database tutorial YouTube”
“PostgreSQL queries insert update delete tutorial”

Basics / Setup

sqlite3 python tutorial
how to create sqlite database python
python sqlite3 create table if not exists
sqlite python connection commit close
sqlite python cursor execute fetchall fetchone

CRUD Operations

python sqlite3 insert row example
python sqlite3 update row
python sqlite3 delete row
python sqlite3 select query
sqlite python update multiple rows
sqlite python delete with foreign key

Joins & Aggregates

sqlite join tables python
sqlite inner join example python
sqlite left join example python
sqlite aggregate functions max sum count python
sqlite group by example python
python sqlite max score group by

Date/Time Handling

sqlite python insert datetime
sqlite python filter by date range
sqlite strftime python datetime
sqlite compare dates python
