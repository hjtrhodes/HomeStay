# HOMESTAY

- Project Timeline: 6 days to MVP
- Main Language: Python, SQL
- Tech Stack: Flask, PostgreSQL
- Testing: Pytest
  
## Functionality Demo - Opens on Youtube
[![Video](https://img.youtube.com/vi/RZVKPn00WF8/0.jpg)](https://www.youtube.com/watch?v=pBcMyL0oLbo&t=3s)

## Project Description
BaldBible is my final Makers project. It was created working in a team of 4 Software Developers and 2 Quality Engineers. The idea for the app came from my own experiences of hair loss and feeling that there should be a more obvious alternative to the hair loss prevention industry to help individuals embrace this natural change. The process of pitching, discussing and communicating the importance of this idea and having the rest of my developers choose it as the final project was very personal and gratifying to me, as was the process of creating it. After conception and discussion Bald Bible became a Pinterest style, hair loss positivity website leveraging the power of images to inspire users to be more accepting of themselves.

This is my cloned version of the project repo to continue development at project completion.
I was responsible for integration of sessions into the login/logout/timeout functionality as well as using sessions to store user information which was then fed to routes. As a team we decided to mob a lot of the features, particularly testing and routes.

We worked in a team of 4 on this project using Flask, Python, PostgreSQL and testing with Pytest. The aim was to practice using version control and agile working practices to create an AirBnB clone from a legacy codebase in 1 week.
Key learning was around the use of sessions to store information and autheticate/timeout users, using relational databases and a multiclass system with individual routes for pages.
Group members were Megan Folsom, Harry Rhodes, Ray Brown and Ben Dixon. 


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
