### FLAW 1: A07:2021-Identification and Authentication Failures 

In authentication we are using basic username whic his admin. Even thought the password is encrypted it's still vulnurable for brute force attacks. In hackpassword.py we brute force throught some passwords that are given in candidates.txt might give us access to the admin panel. admin panel can be accessed by /admin/ URL which makes is quite easy target for attackers. 

To fix this there are multiple ways to make the authentication much harder to be cracked. By first using default username like admin and root gives the attacker a head start because they probably would start this those usernames, so having some unique username would help on the security. To increase the panel security adding a external library that keeps track of suspicious login attempts and adding a simple brute-force attack blocking measure helps to prevent bruteforcing of the password, for this we could use Django-axes (https://github.com/jazzband/django-axes). Changing the Url address for admin panel also helps on the security, because currently admin panel can be accessed from /admin/ which is quite obvious. Having a strong password that doesnt contain generic words also makes it more resistant for brute-force attacks, also making sure that the password has not been cracked before helps a lot because attacker might use some sort of dictionary to brute force passwords.

### FLAW 2: A09:2021-Security Logging and Monitoring Failures 


https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/config/settings.py#L26

Currently in we have debug activated in the application, which means that if the application crashes it provides the user detailed error messages, stack traces and more information about the cause of crash. All these informations may contain sensitive data, that we dont want to be showed to the user. So turning the Debug mode off we get rid of detailed the detailed messages, that might contains sensitive information.

It's good to take note that logging is important feat for application, because it helps the developers to keep track of the possible failures and bugs in the application. But having logging done badly it might have big side effects for the integrity of the application

To fix this problem DEBUG mode can simply be disabled. ```DEBUG=false``` Debug mode should only be used in development, and not in production environment. When disabling debug, it's important to add logs for the application, so the developers can notice suspicious actions on application server side.





### FLAW 3: A01:2021-Broken Access Control

CODE POINT HERE (View all user, logged in views.)
https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/pages/views.py#L23


In this version the application users can access to adding page without being logged in, in the application by going to /add URL. This should not be allowed because without logging in user doesn't need to have access to adding page.

To fix these kind problems adding we can add @login_required() decorator to top of the function view. With @login_required() it is needed to be authenticated to have permission for to view the wanted function view, in this situtation the addNote view


### FLAW 4: A06:2021-Vulnerable and Outdated Components

https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/pages/views.py#L32

Currently in the application all the users notes can be accessed with user/<username>/notes URL. This component is brings vulnerability to the application, because the notes should be personal, and no one else should have not have acces to them than the writer of the note. There are few ways to fix this problem. 

One is to delete the whole view from the user, because all the notes are already displayed when logged in. Otherway is to make use of request.session and check if the user is actually logged to the user that they try to access. It is good take note that this problem is related to broken access control, but having an component that has this kind vulnerability is quite big security flaw for the application and must be adressed.


### FLAW 5: A03:2021-Injection

https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/pages/views.py#L23

https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/pages/templates/pages/index.html#L30

Injectioning is third most usual security flaw on applications. In injectioning attacker injects malicious code or data to the application, this is mostly possible because the lack of validation or sanitization. Currently the application is vulnurable for XSS attacks, where attacker can inject malicious javascript to the content field because of the lack of validation and sanization.

To fix this the request method should be checked that it's actually a valid value by checking request.method === 'POST', so we can be sure that the value is actually submitted from the form. There should be also added |safe filter to prevent special characters being missread by the application.