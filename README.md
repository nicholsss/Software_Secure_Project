1. Create virtual environment: python3 -m venv myenv
2. activate myenv: source myenv/bin/activate
3. install packages: pip install -r requirements.txt
4. start locally: python3 manage.py runserver
5. available at localhost:8000
6. Two accounts in use. username: admin Password: admin. Second account username:bob  password:sieni



### FLAW 1: A07:2021-Identification and Authentication Failures 

1. https://github.com/nicholsss/Software_Secure_Project/blob/cada1cda76bf1914afc04c4f56b482fd3844bfe1/server/db.sql#L127
2. https://github.com/nicholsss/Software_Secure_Project/blob/cada1cda76bf1914afc04c4f56b482fd3844bfe1/server/config/urls.py#L21
3. https://github.com/nicholsss/Software_Secure_Project/blob/cada1cda76bf1914afc04c4f56b482fd3844bfe1/server/config/settings.py#L33

In authentication we are using basic username whic his admin. Even thought the password is encrypted ,it is still vulnerable to brute force attacks. In hackpassword.py we brute force throught some passwords that are given in candidates.txt might give us access to the admin panel. admin panel can be accessed by ```/admin/``` URL which makes is quite easy target for attackers. 

To fix this there are multiple ways to make the authentication much harder to be cracked. By first using default usernames like ```admin``` and ```root``` gives the attacker a head start because they would probably start this these usernames. Having a unique username help would increase security of the application. To increase the panel security adding a external library that keeps track of suspicious login attempts and adding a simple brute-force attack blocking measure helps to prevent bruteforcing of the password, for this we could use Django-axes (https://github.com/jazzband/django-axes). Applying maximum failed login attempts from Django Axes increases the security of the application. Adding ```AXES_FAILURE_LIMIT = 5``` to the root of 'settings.py' allows the user to try 5 login attempts, before they are locked out from the application for certain amount of time.  Changing the Url address for admin panel also helps on the security, because currently admin panel can be accessed from /admin/ which is quite obvious. Having a strong password that does not contain generic words also makes it more resistant to brute-force attacks, also making sure that the password has not been cracked before helps a lot because an attacker might use some sort of dictionary to brute force passwords.

### FLAW 2: A09:2021-Security Logging and Monitoring Failures 


1. https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/config/settings.py#L26
2. https://github.com/nicholsss/Software_Secure_Project/blob/000f2f701ed40aa553c3dfbf7ae12f6eba091ebf/server/config/settings.py#L70

Currently in we have debug activated in the application, which means that if the application crashes it provides  detailed error messages, stack traces and more information about the cause of crash for the user of the application. All this information may contain sensitive data, that we dont want to be show to the user. So turning the Debug mode off can we get rid of the detailed the detailed messages, stack traces and the risk of leaking sensitive data on these kinds of situations.

It's good to take note that logging data is important feat for application, because it helps the developers to keep track of  possible failures and bugs in the application. But having logging not done correctly., it might have big side effects for the integrity of the application.

To fix this problem DEBUG mode can simply be disabled. ```DEBUG=false``` Debug mode should only be used in development, and not in production environment. When disabling debug, it's important to add logs for the application, so the developers can notice suspicious actions on application server side.





### FLAW 3: A01:2021-Broken Access Control

1. https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/pages/views.py#L23


In this version the application users can access to add note page without being logged in, in the application by going to ```/add``` URL. This should not be allowed because without logging in. user does not need to have access to adding page, if they are not logged in. It's mainly good approach to restrict user from accessing funtionalities that they dont have use for, if they are not logged in.

To fix these kind problems we can apply ```@login_required()``` decorator to top of the function view. With ```@login_required()``` it is needed to be authenticated to have permission for to view the wanted function view. If user tries to access page with ```@login_required()``` they are redirected back to login form to authenticate. in this situtation adding ```@login_required()``` protects the addNoteView being accessed without authentication.


### FLAW 4: A06:2021-Vulnerable and Outdated Components

1. https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/pages/views.py#L32

In the application all users notes can be accessed with the URL ```user/username/notes```. This component introduces vulnerability to the application, because the notes should be personal and only available to the writer. 

To fix this problem,  One solution is to delete the whole view from the user, because all the notes are already displayed when logged in. secondd option is to make use of request.session and check if the user is actually logged to the account that they try to access. It is good take note that this problem is related to broken access control, but having an component that has this kind vulnerability is quite big security flaw for the application and must be adressed.


### FLAW 5: A03:2021-Injection

1. https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/pages/views.py#L23
2. https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/pages/templates/pages/index.html#L30

Injectioning is third most usual security flaw on applications. In injectioning attacker injects malicious code or data to the application, this is mostly possible because the lack of validation or sanitization. Currently the application is vulnurable for XSS attacks, where attacker can inject malicious javascript to the content field because of the lack of validation and sanization.

To fix this the request method should be checked that it's actually a valid value by checking ```request.method === 'POST'```, so we can be sure that the value is actually submitted from the form. There should be also added |safe filter to prevent special characters being missread by the application. Also using forms that django is providing helps to filter the form data to be correct.