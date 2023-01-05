Secret Santa Application: 
Project by Joshua Siderius

Instructions:
- Make sure the python email library is installed (pip install email)
- Make sure you have a developer password for your email, or have allowed 3rd party access in some way
- Add the names and emails you would like to use in main() in santa.py as documented there 
- Run the command: python3 santa.py
- input your email address and developer password as prompted 
- have fun

Purpose:
This project takes names and emails for a group of people who want to do secret santa. 
It randomly orders names into a way tha will be fun to play (no one has themselves, no 2 people have each other)
It then sends each person and email informing them of which person in the group they will be giving a gift to 
Finally it prints the results to results.txt to save the result for any future changes or disputes
The person who runs the program can choose whether or not to read the results

I made this project because Family does secret santa every year and I ofter end up doing it with friends as well. 
This app ensures a good result, makes it quick and easy to set up, and also makes it to personalize things such as the message or amount.


Technologies:
pip install email
smtplib is part of pythons standard library

I decided to use the email and smtplib libraries.
The EmailMessage class from email is a simplified way to store all the elements an email.
SMTP ports (Simple Mail Transfer Protocol)
The SMTP_SSL class from smtplib 


Challenges:
The most challenging part of this project was connecting the code to my email.
When I made this, google had recently made security changes that disallowed third party application access to email accounts.
Because of the recency, there was little documentation on what the work around was, and I had to do alot of research and trial/error.
I eventually found a way to make a developer access password which is necessarily used over the regular password.


