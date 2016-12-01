# G00323639RepProject

Dev diary/overall thoughts:

kicking off this project I was lost as to what programs to use and how to approach it. I had never coded in python, git was something I had only learned last year, and html I hadnt properly used since first year so it all seemed like a big panic at first. I went online to code academy brushed up on their python tutorials got familiar with the language. I also used the inclass exercises as a reference and learning point the flask ones and flask docs online were crucial to my learning, making and understanding of this project. When I finally sat down to do the project occured a few problems. Where to start? what libaries to use? what database to use?

Really I started the project by wittling my way through the databases the mongos, the couch, the pouch, the rethink all the databases some looked promising and easy use but I inucured my first big problem of the project. That was having a 32bit processor laptop and most if not all of the GUI databases online were for 64 bit with no 32 bit alternative. So I looked at the reading material for the project and came across sqllite, seeing it was built into the python library and that it was easy use and was just basic sql commands I decided to choose that as my database.

Once I estabhlished that I brainstormed a few Ideas for my project looking at the sample ideas listed on the moodle page, googling simple web apps and I ended up settling on a simplistic online shopping cart. One that would add to your basket, add the price of what you had added and display the contents. I started by downloading the varioues required software. Then setting up my Github Repo, started doing the flask exercise and looking through the flask docs. created my first two files outside my readme, which were the web app file itself then the index html file. Learned from the flask docs how to set up the link between the 2 so when I ran the python file in cmdr it would run the contents of the html page.

I then using the example sqlite made my database and hardcoded some data in there so id see how it stored. the next bits took the biggest portion between figuring out how to link the database and flask inputs while running it through commander onto the html file. there were alot of different versions of this project and subdirectories I had to delete or change. when I got basic input and output I did a bit of reasearch and realised id need a rendertemplate. So I changed the static folder to templates added my basic.html file as my render template and called it in my flask routes that were carring out my input and output functions. while having it all liked to buttons and forms in my index.html page. the final touches were really comments and getting bootstrap working so the project looked appealing. for most the project I had a supermarket back ground though this proved to make the output unreadable. So using bootstrap and simple background image I made the web app look more appealing.

If I could do this again I would defintely start this earlier and do way more research, add in more abitious ideas aswell. I would also have liked to have known to use sqllite3 alot earlier so I wouldnt have wasted time with the other databases. knowing to clear my cach when running this aswell would have been good as that caused alot of confusion at times. learning the ins and outs of python throughly would have been a major benefit. Overall this was a big learning experience and im equiped with more skills when it comes to app development and will be more prepared for future projects.


Used to make this project:
Python 3.5 and its libary
SQLLite3 used as my database
Cmder
Brackets
Notepad++
BootStrap
Flask
Anaconda for python 3.5

REFERENCES + REASEARCH: Code Adapted from below sources along with methods and practices learn from sources below
https://github.com/data-representation/example-sqlite
https://github.com/data-representation/example-project
http://flask.pocoo.org/
http://jinja.pocoo.org/
https://www.python.org/doc/
https://www.codecademy.com/learn/python
data rep moodle = flask exercises
https://v4-alpha.getbootstrap.com/getting-started/introduction/
http://www.w3schools.com/
http://stackoverflow.com/

