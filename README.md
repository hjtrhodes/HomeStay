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

### Planning: User Stories, Table and Multi Class Design
We started by mapping the user journey though the app an annotating the classes which would hold the actions for each user interaction: 
![User Journey](https://res.cloudinary.com/dut4qf1bt/image/upload/v1708613820/HomeStay/User_Journey_r4mv9n.png "User Journey")

Then we designed our PostgreSQL tables considering the values we would need each object to hold:
![Table Design](https://res.cloudinary.com/dut4qf1bt/image/upload/v1708613820/HomeStay/Table_Design_jqqzdx.png "Table Design")

And completed a fraft of our multiclass design:
![Multiclass Design](https://res.cloudinary.com/dut4qf1bt/image/upload/v1708613820/HomeStay/Multiclass_design_jif71n.png "Multiclass Design")

## Final Acheived MVP Functionality:
- Locally Hosted PostgreSQL Database
- Login: Starts user session
- Sessions: Session functionality integrated to store user data, authenticate and timeout users
- Book: User could request a single date booking of a space
- Testing: 41 tests passing in test suite after TDD focus
- Bookings: User could view their bookings
- NavBar: Simple navbar navigation
- User can see their own spaces

### My responsibilities:

Planning:
- Collaboratively completing the Multiclass design and Tbale design trying to preempt what data we would need about out user.

Project Sprints:
- Individual responsibilities: Integration of sessions into the login/logout/timeout functionality, using sessions to store user information which was then fed to routes, testing
- Supported others by pair programming on: Knowledge sharing around sessions, creating routes, creating backend functions

## Functionality Added Since Project Completion

- [x] Table Schema now supports images which display for a space
- [x] Pending booking displayed to user on My Spaces Page  
- [x] User can confirm/Deny a booking on their space
- [x] Pending bookings will be updated with their new status
- [x] Conditional rendering of pending and confirmd bookings using Javascript
- [x] User can see list of booked spaces with updated status
- [x] User can delete a booking - New routes
- [x] Booking now display with booking length
- [x] Whole website re-stlyed

## Challenges/Actions we took to overcome
Table Design:
- Although we planned our table design as we went through the project we had to continuously add new fields to hold more user data. With PostgreSQL this can cause issues as the objects going to and from the database didn't always match the table schema. We also had to remake our seed data every time we made a change. To move past this we communicated and delegated tasks to update functions and classes with new object information. We did a lot of refactoring, testing and mobbing to ensure the app was working as it should.

Nested Loops:
- Because we were still learning about joins and weren't always utlising them to display information in some instances we would have to use a nested loop e.g. a loop displying spaces information inside a loop displaying booking information. This caused issues with rendering, because often the inner loop would iterate multiple times causing duplicates on the page. We didn't resolve this issue in time during the project but I have since gone back to refactor the code and utilised indexing in the nested loop to ensure it only display the correct information once.

Risk Aversion:
- We worked well as a team on the project, we collaborated and communicated well and our TDD was strong. However because the repo was so small we knew that as soon as we split to individual taks we would cause merge conflicts. As a result we spent a lot of time mobbing features. This had positives and negatives - we all learnt a lot form working together and the code was robust, well tested and functioning as it should, however our progress suffered as a result of our teamwork (because it made us slower) and we didn't reach our MVP by the end of the week. We also did not suffer any merge conflicts which is a positive, but meant we didn't learn how to resolve them. 



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
