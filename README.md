# HOMESTAY

- Project Timeline: 6 days to MVP
- Main Language: Python, SQL
- Tech Stack: Flask, PostgreSQL
- Testing: Pytest
  
## Functionality Demo - Opens on Youtube
[![Video](https://img.youtube.com/vi/pBcMyL0oLbo/0.jpg)](https://www.youtube.com/watch?v=pBcMyL0oLbo&t=3s)

## Project Description
This is my cloned version of the project repo to continue development at project completion - details of my work after project completion can be found below in 'Functionality Added Since Project Completion'

We worked in a team of 4 on this project using Flask, Python, PostgreSQL and testing with Pytest. The aim was to practice using version control and agile working practices to create an AirBnB clone from a legacy codebase in 1 week.
This was the first project in which I had used routes to access backend functions or render frontend pages. There was also key learning around the use of sessions to store information and autheticate/timeout users, using relational databases, test driven development, navigating multiclass systems and avoiding merge conflicts.

### Planning: Useer Stories, Table and Multi Class Design
We started by mapping the user journey though the app an annotating the classes which would hold the actions for each user interaction: 
![User Journey](https://res.cloudinary.com/dut4qf1bt/image/upload/v1708613820/HomeStay/User_Journey_r4mv9n.png "User Journey")

Then we designed our PostgreSQL tables considering the values we would need each object to hold:
![Table Design](https://res.cloudinary.com/dut4qf1bt/image/upload/v1708613820/HomeStay/Table_Design_jqqzdx.png "Table Design")

And completed a fraft of our multiclass design:
![Multiclass Design](https://res.cloudinary.com/dut4qf1bt/image/upload/v1708613820/HomeStay/Multiclass_design_jif71n.png "Multiclass Design")



I was responsible for integration of sessions into the login/logout/timeout functionality as well as using sessions to store user information which was then fed to routes. As a team we decided to mob a lot of the features, particularly testing and routes.


## For Codebase Local Setup

```shell
# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_TEST

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py

# Now visit http://localhost:5000/index in your browser
```
