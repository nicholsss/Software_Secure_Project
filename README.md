### Flaw 1: A07:2021-Identification and Authentication Failures 

In here we are using the basic username which is admin. Even thought the password is encrypted its still not good idea to use username basic username like admin. Because attacker usually starts with the most obvious usernames, like admin and root. It's good idea to have some sort customized username to make the admin panel security more stronger. It might be a good idea to restrict the access of the admin panel with some external libraries, for example using django-axes(https://github.com/jazzband/django-axes). One thing that user can also do it to change the admin panel url address, so it wont be too obvious for the attacker (LINKKI TÄSSÄ KOODIN URLIIN). As it can be seen hackpassword.py brute-forces throught some of the passwords that are included in the candidates.txt file. So using a stronger password that have not been cracked before is important also.

### Flaw 2: A09:2021-Security Logging and Monitoring Failures 


### Flaw 3: A01:2021-Broken Access Control

CODE POINT HERE (View all user, logged in views.)

In this version the application users can access to adding page without being logged in, in the application by going to /add URL. This should not be allowed because without logging in user doesn't need to have access to adding page.

To fix these kind problems adding we can add @login_required() decorator to top of the function view. With @login_required() it is needed to be authenticated to have permission for to view the wanted function view, in this situtation the add view


