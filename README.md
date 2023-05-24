Github repo: https://github.com/nicholsss/Software_Secure_Project

1. Create virtual environment: python3 -m venv myenv
2. activate myenv: source myenv/bin/activate
3. install packages: pip install -r requirements.txt
4. start locally: python3 manage.py runserver
5. available at localhost:8000
6. Two accounts in use. username: admin Password: admin. Second account username:bob  password:sieni



### FLAW 1: A07:2021-Identification and Authentication Failures 

1. https://github.com/nicholsss/Software_Secure_Project/blob/cada1cda76bf1914afc04c4f56b482fd3844bfe1/server/db.sql#L127
2. https://github.com/nicholsss/Software_Secure_Project/blob/cd4ff4b409df498a6f1e4c443dbe5dab0871a878/server/config/urls.py#L21
3. https://github.com/nicholsss/Software_Secure_Project/blob/cada1cda76bf1914afc04c4f56b482fd3844bfe1/server/config/settings.py#L33

In authentication we are using basic username whic his admin. Even thought the password is encrypted ,it is still vulnerable to brute force attacks. In hackpassword.py we brute force throught some passwords that are given in candidates.txt might give us access to the admin panel. admin panel can be accessed by ```/admin/``` URL which makes is quite easy target for attackers. 

To fix this there are multiple ways to make the authentication much harder to be cracked. By first using default usernames like ```admin``` and ```root``` gives the attacker a head start because they would probably start this these usernames. Having a unique username help would increase security of the application. To increase the panel security adding a external library that keeps track of suspicious login attempts and adding a simple brute-force attack blocking measure helps to prevent bruteforcing of the password, for this we could use Django-axes (https://github.com/jazzband/django-axes). Applying maximum failed login attempts from Django Axes increases the security of the application. Adding ```AXES_FAILURE_LIMIT = 5``` to the root of 'settings.py' https://github.com/nicholsss/Software_Secure_Project/blob/5d5d9f95e05e2b4c94fb8ac7c54fc36ef6b71a47/server/config/settings.py#L33 allows the user to try 5 login attempts, before they are locked out from the application for certain amount of time.  Changing the Url address for admin panel also helps on the security, because currently admin panel can be accessed from /admin/ which is quite obvious. Having a strong password that does not contain generic words also makes it more resistant to brute-force attacks, also making sure that the password has not been cracked before helps a lot because an attacker might use some sort of dictionary to brute force passwords.

### FLAW 2: A09:2021-Security Logging and Monitoring Failures 


1. https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/config/settings.py#L26


Currently in we have debug activated in the application, which means that if the application crashes it provides  detailed error messages, stack traces and more information about the cause of crash for the user of the application. All this information may contain sensitive data, that we dont want to be show to the user. So turning the Debug mode off can we get rid of the detailed the detailed messages, stack traces and the risk of leaking sensitive data on these kinds of situations.

It's good to take note that logging data is important feat for application, because it helps the developers to keep track of  possible failures and bugs in the application. But having logging not done correctly., it might have big side effects for the integrity of the application.

To fix this problem DEBUG mode can simply be disabled. ```DEBUG=false``` Debug mode should only be used in development, and not in production environment. When disabling debug, it's important to add logs for the application, so the developers can notice suspicious actions on application server side.
https://github.com/nicholsss/Software_Secure_Project/blob/000f2f701ed40aa553c3dfbf7ae12f6eba091ebf/server/config/settings.py#L70



## Flaw 3: A06:2021-Vulnerable and Outdated Components
There might come situations where dependecies are outdated or their development is depricated. Having an oudated dependecy might be big security risk, because an updated version from the depedency might contain a fix for a security flaw that have been patched with the newer version. So thats why it's important to have dependecies up to date.

There are ways to update requirements.txt which contains the dependecies and their version number which is used for installing them. One way is to manually check and update the version number of the dependecies and update them in requirements.txt. Way to get most recent versions is to run `pip list --outdated` in virtual env. In example the current Django 4.2 version is outdated, because there is 4.2.1 available. In this situation 4.2.1 contains only minor bugfixes, but there might be situtation where the newer update contains a critical bugfix, so then it should be updated immediately.


### FLAW 4: A01:2021-Broken Access Control

1. https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/pages/views.py#L32

In the application all users notes can be accessed with the URL ```user/username/notes```. This component introduces vulnerability to the application, because the notes should be personal and only available to the writer. 

To fix this problem, there is option to make use of request.session and check if the user is actually logged to the account that they try to access. If they are not the correct user, then they are redirected back to the homepage.https://github.com/nicholsss/Software_Secure_Project/blob/cd4ff4b409df498a6f1e4c443dbe5dab0871a878/server/pages/views.py#L22
So 



### FLAW 5: A03:2021-Injection

1. https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/pages/views.py#L23
2. https://github.com/nicholsss/Software_Secure_Project/blob/79692dcc5a1d46d203bc07a8250558559fadcb57/server/pages/templates/pages/index.html#L30

Injectioning is third most usual security flaw on applications. In injectioning attacker injects malicious code or data to the application, this is mostly possible because the lack of validation or sanitization. Currently the application is vulnurable for XSS attacks, where attacker can inject malicious code to the content field because of the lack of validation and sanization.


To fix this the keyword safe should be removed from the list. Because what `| safe` does it says to the Django app that the current content `note.content` is correctly sanitized and thats why it doesnt need escaping. To actually use `| safe` the validation and sanitization should be done on the server side. But in this case just removing the keyword `| safe` is enought, because then the Django app automatically takes over the validation and sanitization.


## Flaw 3: A06:2021-Vulnerable and Outdated Components
There might come situations where dependecies are outdated or their development is depricated. Having an oudated dependecy might be big security risk, because an updated version from the depedency might contain a fix for a security flaw that have been patched with the newer version. So thats why it's important to have dependecies up to date.

There are ways to update requirements.txt which contains the dependecies and their version number which is used for installing them. One way is to manually check and update the version number of the dependecies and update them in requirements.txt. Way to get most recent versions is to run `pip list --outdated` in virtual env. In example the current Django 4.2 version is outdated, because there is 4.2.1 available. In this situation 4.2.1 contains only minor bugfixes, but there might be situtation where the newer update contains a critical bugfix, so then it should be updated immediately.