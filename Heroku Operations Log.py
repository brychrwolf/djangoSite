Step 1: Sign up
	Email confirmation -> done
Step 2: Install Heroku Toolbelt
	Full Install -> done
Step 3: Login 
	C:\>heroku login
	Enter your Heroku credentials.
	Email: bryan@wolfford.com
	Password (typing will be hidden):
	Found existing public key: ****
	Uploading SSH public key ****
	Authentication successful.
Step 4: Deploy an Application
	Prerequisites: 
		Get started with Python on Heroku
			MORE Prerequisites
				Must have Python v2.7 installed
					FFFFFUUUUUUUUUUUUUUUUU
					Install Python v2.7
						Download Python2.7
						Run installer to C:\Python27\
						Change PATH Environmental Variables
							C:\Python26 to C:\Python27
							C:\Python26\site-packages\django\bin to C:\Python27\site-packages\django\bin
					Copy django folder from C:\Python26\site-packages to C:\Python27\site-packages
					Test django in new directory
						C:\djangoSite>python manage.py syncdb
						Traceback (most recent call last):
						  File "manage.py", line 8, in <module>
							from django.core.management import execute_from_command_line
						ImportError: No module named django.core.management
						-_-
					Research how to install a site-package
					Discover in <a href=http://docs.python.org/install/index.html#how-installation-works target=_blank class=liveBlog>the python documentation</a> that the default directory in Python is Lib/site-packages unlike the Unix default of ~/site-packages
					Again, change the PATH. This time only from C:\Python27\site-packages\django\bin to C:\Python27\Lib\site-packages\django\bin
					Test django in new directory again
						C:\djangoSite>python manage.py syncdb
						Creating tables ...
						Installing custom SQL ...
						Installing indexes ...
						Installed 0 object(s) from 0 fixture(s)
					pause for a breath!
				Must use have Virtualenv installed
					Register with <a href=http://pypi.python.org/pypi/virtualenv target=_blank class=liveBlog>pypi.python.org</a>
						opt to login with use google account
						follow email confirmation
						fail at several attempts to login through the popup prompt
						refresh the page = more failures
						manually type in the address to the OpenId login link = success
					pypi.python.org says that "You can install virtualenv with pip install virtualenv"
					Come back to this after installing Pip
				Must have Pip installed
					Follow link Heroku website to 
					Continue to <a href=http://www.pip-installer.org/en/latest/installing.html target=_blank class=liveBlog>www.pip-installer.org</a>
					*MORE* Prerequisites
						Must have <a href=http://pypi.python.org/pypi/setuptools target=_blank class=liveBlog>Setuptools</a> installed
							Since we have to use Python2.7, the link to this is <a href=http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11.win32-py2.7.exe#md5=57e1e64f6b7c7f1d2eddfc9746bbaf20 target=_blank class=liveBlog>Setuptools for Python2.7</a>
							Install to default "\Lib\site-packages"
					Download and install <a href=https://raw.github.com/pypa/pip/master/contrib/get-pip.py target=_blank class=liveBlog>get-pip.py</a> using the Python interpreter
						open CMD prompt
						C:\>cd C:\Downloads
						C:\Downloads>python get-pip.py
						Downloading/unpacking pip
						  Downloading pip-1.1.tar.gz (95Kb): 95Kb downloaded
						  Running setup.py egg_info for package pip

							warning: no files found matching '*.html' under directory 'docs'
							warning: no previously-included files matching '*.txt' found under directory 'docs\_build'
							no previously-included directories found matching 'docs\_build\_sources'
						Installing collected packages: pip
						  Running setup.py install for pip

							warning: no files found matching '*.html' under directory 'docs'
							warning: no previously-included files matching '*.txt' found under directory 'docs\_build'
							no previously-included directories found matching 'docs\_build\_sources'
							Installing pip-script.py script to C:\Python27\Scripts
							Installing pip.exe script to C:\Python27\Scripts
							Installing pip.exe.manifest script to C:\Python27\Scripts
							Installing pip-2.7-script.py script to C:\Python27\Scripts
							Installing pip-2.7.exe script to C:\Python27\Scripts
							Installing pip-2.7.exe.manifest script to C:\Python27\Scripts
						Successfully installed pip
						Cleaning up...
				Install Virtualenv
					Try using the one line of code from the site
						>>> pip install virtualenv
						File "<stdin>", line 1
							pip install virtualenv
					Google first = little help
					Proceed to StackOverflow = <a href=http://stackoverflow.com/questions/8548030/syntax-error-on-install-when-doing-pip-install-for-python target=_blank class=liveBlog>don't use interpreter and add Scripts to the Environment Variables</a>
					Edit Environment Variable
					Add C:\Python27\Scripts
					Realize that the django-admin.py file DOES belong in here too
					Remove C:\Python27\Lib\site-packages\django\bin
					Copy django-admin.py over to Scripts directory
					Try code from the site again (this time in the cmd prompt)
						C:\>pip install virtualenv
						Downloading/unpacking virtualenv
						  Downloading virtualenv-1.7.1.2.tar.gz (2.1Mb): 2.1Mb downloaded
						  Running setup.py egg_info for package virtualenv

						    warning: no previously-included files matching '*.*' found under directory 'docs\_templates'
						Installing collected packages: virtualenv
						  Running setup.py install for virtualenv

						    warning: no previously-included files matching '*.*' found under directory 'docs\_templates'
						    Installing virtualenv-script.py script to C:\Python27\Scripts
						    Installing virtualenv.exe script to C:\Python27\Scripts
						    Installing virtualenv.exe.manifest script to C:\Python27\Scripts
						Successfully installed virtualenv
						Cleaning up...
					Try again for another breath!!!!
				Must use Pip to manage dependencies
			Loginto Heroku
				C:\>heroku login
				Enter your Heroku credentials.
				Email: bryan@wolfford.com
				Password (typing will be hidden):
				Authentication successful.
			Start App in Virtualenv
				C:\djangoSite>virtual venv --distribute
				'virtual' is not recognized as an internal or external command,
				operable program or batch file.

				C:\djangoSite>virtualenv venv --distribute
				New python executable in venv\Scripts\python.exe
				Installing distribute...............................................................................
				....................................................................................................
				............done.
				Installing pip.................done.

				C:\djangoSite>venv\Scripts\activate.bat
				(venv) C:\djangoSite>pip install flask
				Downloading/unpacking flask
				  Downloading Flask-0.8.tar.gz (494Kb): 494Kb downloaded
				  Running setup.py egg_info for package flask

					warning: no files found matching '*' under directory 'tests'
					warning: no previously-included files matching '*.pyc' found under directory 'docs'
					warning: no previously-included files matching '*.pyo' found under directory 'docs'
					warning: no previously-included files matching '*.pyc' found under directory 'tests'
					warning: no previously-included files matching '*.pyo' found under directory 'tests'
					warning: no previously-included files matching '*.pyc' found under directory 'examples'
					warning: no previously-included files matching '*.pyo' found under directory 'examples'
					no previously-included directories found matching 'docs\_build'
					no previously-included directories found matching 'docs\_themes\.git'
				Downloading/unpacking Werkzeug>=0.6.1 (from flask)
				  Downloading Werkzeug-0.8.3.tar.gz (1.1Mb): 1.1Mb downloaded
				  Running setup.py egg_info for package Werkzeug

					warning: no files found matching '*' under directory 'werkzeug\debug\templates'
					warning: no files found matching '*' under directory 'tests'
					warning: no previously-included files matching '*.pyc' found under directory 'docs'
					warning: no previously-included files matching '*.pyo' found under directory 'docs'
					warning: no previously-included files matching '*.pyc' found under directory 'tests'
					warning: no previously-included files matching '*.pyo' found under directory 'tests'
					warning: no previously-included files matching '*.pyc' found under directory 'examples'
					warning: no previously-included files matching '*.pyo' found under directory 'examples'
					no previously-included directories found matching 'docs\_build'
				Downloading/unpacking Jinja2>=2.4 (from flask)
				  Downloading Jinja2-2.6.tar.gz (389Kb): 389Kb downloaded
				  Running setup.py egg_info for package Jinja2

					warning: no previously-included files matching '*' found under directory 'docs\_build'
					warning: no previously-included files matching '*.pyc' found under directory 'jinja2'
					warning: no previously-included files matching '*.pyc' found under directory 'docs'
					warning: no previously-included files matching '*.pyo' found under directory 'jinja2'
					warning: no previously-included files matching '*.pyo' found under directory 'docs'
				Installing collected packages: flask, Werkzeug, Jinja2
				  Running setup.py install for flask

					warning: no files found matching '*' under directory 'tests'
					warning: no previously-included files matching '*.pyc' found under directory 'docs'
					warning: no previously-included files matching '*.pyo' found under directory 'docs'
					warning: no previously-included files matching '*.pyc' found under directory 'tests'
					warning: no previously-included files matching '*.pyo' found under directory 'tests'
					warning: no previously-included files matching '*.pyc' found under directory 'examples'
					warning: no previously-included files matching '*.pyo' found under directory 'examples'
					no previously-included directories found matching 'docs\_build'
					no previously-included directories found matching 'docs\_themes\.git'
				  Running setup.py install for Werkzeug

					warning: no files found matching '*' under directory 'werkzeug\debug\templates'
					warning: no files found matching '*' under directory 'tests'
					warning: no previously-included files matching '*.pyc' found under directory 'docs'
					warning: no previously-included files matching '*.pyo' found under directory 'docs'
					warning: no previously-included files matching '*.pyc' found under directory 'tests'
					warning: no previously-included files matching '*.pyo' found under directory 'tests'
					warning: no previously-included files matching '*.pyc' found under directory 'examples'
					warning: no previously-included files matching '*.pyo' found under directory 'examples'
					no previously-included directories found matching 'docs\_build'
				  Running setup.py install for Jinja2

					warning: no previously-included files matching '*' found under directory 'docs\_build'
					warning: no previously-included files matching '*.pyc' found under directory 'jinja2'
					warning: no previously-included files matching '*.pyc' found under directory 'docs'
					warning: no previously-included files matching '*.pyo' found under directory 'jinja2'
					warning: no previously-included files matching '*.pyo' found under directory 'docs'
				Successfully installed flask Werkzeug Jinja2
				Cleaning up...
			Create app.py
			Create requirements txt
				(venv) C:\djangoSite>pip freeze > requirements.txt
				(venv) C:\djangoSite>cat requirements.txt
				Flask==0.8
				Jinja2==2.6
				Werkzeug==0.8.3
				distribute==0.6.24
			Declare process Types with Foreman/Procfile
				Create Procfile
				Add web: python app.py to Procfile
				C:\djangoSite>foreman start
					20:47:15 web.1     | process terminated
					20:47:15 system    | sending SIGTERM to all processes
				C:\djangoSite>
				*Allow access through firewall*
				Test at localhost:5000 = "HelloWorld!" 
				Celebrate!
			Store App with Git
				create djangoSiute\.gitignore containing venv and *.pyc
				C:\djangoSite>git init
				Reinitialized existing Git repository in C:/djangoSite/.git/
				C:\djangoSite>git add .
				C:\djangoSite>git commit -m "Added Heroku's Flask app"
					[master 680a9a2] Added Heroku's Flask app
					 12 files changed, 284 insertions(+)
					 create mode 100644 .gitignore
					 create mode 100644 Heroku Operations Log.py
					 create mode 100644 Heroku Operations Log.txt
					 create mode 100644 Procfile
					 create mode 100644 app.py
					 create mode 100644 requirements.txt
				C:\djangoSite>git push origin
					warning: push.default is unset; its implicit value is changing in
					Git 2.0 from 'matching' to 'upstream'. To squelch this message
					and maintain the current behavior after the default changes, use:
					  git config --global push.default matching
					To squelch this message and adopt the new behavior now, use:
					  git config --global push.default upstream
					See 'git help config' and search for 'push.default' for further information.
					Enter passphrase for key '/c/.ssh/id_rsa':
					Counting objects: 26, done.
					Delta compression using up to 4 threads.
					Compressing objects: 100% (15/15), done.
					Writing objects: 100% (17/17), 5.41 KiB, done.
					Total 17 (delta 9), reused 0 (delta 0)
					To git@github.com:brychrwol/djangoSite.git
					4bf2b6e..680a9a2  master -> master
			Deploy to Heroku
				Create the Cedar stack
					C:\Users\Initia7_B\Documents\HPU\CSCI 3771\djangoSite>heroku create --stack cedar
					Creating high-light-6071... done, stack is cedar
					http://high-light-6071.herokuapp.com/ | git@heroku.com:high-light-6071.git
					Git remote heroku added
				Deploy the code
					C:\Users\Initia7_B\Documents\HPU\CSCI 3771\djangoSite>git push heroku master
					The authenticity of host 'heroku.com (50.19.85.132)' can't be established.
					RSA key fingerprint is 8b:48:5e:67:0e:c9:16:47:32:f2:87:0c:1f:c8:60:ad.
					Are you sure you want to continue connecting (yes/no)? yes
					Warning: Permanently added 'heroku.com,50.19.85.132' (RSA) to the list of known hosts.
					Enter passphrase for key '/c/Users/Initia7_B/.ssh/id_rsa':
					Counting objects: 96, done.
					Delta compression using up to 4 threads.
					Compressing objects: 100% (89/89), done.
					Writing objects: 100% (96/96), 43.87 KiB, done.
					Total 96 (delta 25), reused 0 (delta 0)

					-----> Heroku receiving push
					-----> Python app detected
					-----> Preparing Python interpreter (2.7.2)
					-----> Creating Virtualenv version 1.7
						   New python executable in .heroku/venv/bin/python2.7
						   Also creating executable in .heroku/venv/bin/python
						   Installing distribute........................................................................
					....................................................................................................
					.................done.
						   Installing pip...............done.
						   Running virtualenv with interpreter /usr/local/bin/python2.7
					-----> Activating virtualenv
					-----> Installing dependencies using Pip version 1.0.2
						   Downloading/unpacking Flask==0.8 (from -r requirements.txt (line 1))
						   Creating supposed download cache at /app/tmp/repo.git/.cache/pip_downloads
							 Storing download in cache at /app/tmp/repo.git/.cache/pip_downloads/http%3A%2F%2Fpypi.pytho
					n.org%2Fpackages%2Fsource%2FF%2FFlask%2FFlask-0.8.tar.gz
							 Running setup.py egg_info for package Flask

							   warning: no files found matching '*' under directory 'tests'
							   warning: no previously-included files matching '*.pyc' found under directory 'docs'
							   warning: no previously-included files matching '*.pyo' found under directory 'docs'
							   warning: no previously-included files matching '*.pyc' found under directory 'tests'
							   warning: no previously-included files matching '*.pyo' found under directory 'tests'
							   warning: no previously-included files matching '*.pyc' found under directory 'examples'
							   warning: no previously-included files matching '*.pyo' found under directory 'examples'
							   no previously-included directories found matching 'docs/_build'
							   no previously-included directories found matching 'docs/_themes/.git'
						   Downloading/unpacking Jinja2==2.6 (from -r requirements.txt (line 2))
							 Storing download in cache at /app/tmp/repo.git/.cache/pip_downloads/http%3A%2F%2Fpypi.pytho
					n.org%2Fpackages%2Fsource%2FJ%2FJinja2%2FJinja2-2.6.tar.gz
							 Running setup.py egg_info for package Jinja2

							   warning: no previously-included files matching '*' found under directory 'docs/_build'
							   warning: no previously-included files matching '*.pyc' found under directory 'jinja2'
							   warning: no previously-included files matching '*.pyc' found under directory 'docs'
							   warning: no previously-included files matching '*.pyo' found under directory 'jinja2'
							   warning: no previously-included files matching '*.pyo' found under directory 'docs'
						   Downloading/unpacking Werkzeug==0.8.3 (from -r requirements.txt (line 3))
							 Storing download in cache at /app/tmp/repo.git/.cache/pip_downloads/http%3A%2F%2Fpypi.pytho
					n.org%2Fpackages%2Fsource%2FW%2FWerkzeug%2FWerkzeug-0.8.3.tar.gz
							 Running setup.py egg_info for package Werkzeug

							   warning: no files found matching '*' under directory 'werkzeug/debug/templates'
							   warning: no files found matching '*' under directory 'tests'
							   warning: no previously-included files matching '*.pyc' found under directory 'docs'
							   warning: no previously-included files matching '*.pyo' found under directory 'docs'
							   warning: no previously-included files matching '*.pyc' found under directory 'tests'
							   warning: no previously-included files matching '*.pyo' found under directory 'tests'
							   warning: no previously-included files matching '*.pyc' found under directory 'examples'
							   warning: no previously-included files matching '*.pyo' found under directory 'examples'
							   no previously-included directories found matching 'docs/_build'
						   Requirement already satisfied (use --upgrade to upgrade): distribute==0.6.24 in ./.heroku/ven
					v/lib/python2.7/site-packages/distribute-0.6.24-py2.7.egg (from -r requirements.txt (line 4))
						   Installing collected packages: Flask, Jinja2, Werkzeug
							 Running setup.py install for Flask

							   warning: no files found matching '*' under directory 'tests'
							   warning: no previously-included files matching '*.pyc' found under directory 'docs'
							   warning: no previously-included files matching '*.pyo' found under directory 'docs'
							   warning: no previously-included files matching '*.pyc' found under directory 'tests'
							   warning: no previously-included files matching '*.pyo' found under directory 'tests'
							   warning: no previously-included files matching '*.pyc' found under directory 'examples'
							   warning: no previously-included files matching '*.pyo' found under directory 'examples'
							   no previously-included directories found matching 'docs/_build'
							   no previously-included directories found matching 'docs/_themes/.git'
							 Running setup.py install for Jinja2

							   warning: no previously-included files matching '*' found under directory 'docs/_build'
							   warning: no previously-included files matching '*.pyc' found under directory 'jinja2'
							   warning: no previously-included files matching '*.pyc' found under directory 'docs'
							   warning: no previously-included files matching '*.pyo' found under directory 'jinja2'
							   warning: no previously-included files matching '*.pyo' found under directory 'docs'
							 Running setup.py install for Werkzeug

							   warning: no files found matching '*' under directory 'werkzeug/debug/templates'
							   warning: no files found matching '*' under directory 'tests'
							   warning: no previously-included files matching '*.pyc' found under directory 'docs'
							   warning: no previously-included files matching '*.pyo' found under directory 'docs'
							   warning: no previously-included files matching '*.pyc' found under directory 'tests'
							   warning: no previously-included files matching '*.pyo' found under directory 'tests'
							   warning: no previously-included files matching '*.pyc' found under directory 'examples'
							   warning: no previously-included files matching '*.pyo' found under directory 'examples'
							   no previously-included directories found matching 'docs/_build'
						   Successfully installed Flask Jinja2 Werkzeug
						   Cleaning up...
					-----> Discovering process types
						   Procfile declares types -> web
					-----> Compiled slug size is 3.8MB
					-----> Launching... done, v3
						   http://high-light-6071.herokuapp.com deployed to Heroku

					To git@heroku.com:high-light-6071.git
					 * [new branch]      master -> master	
				Scale the app on the web
					C:\Users\Initia7_B\Documents\HPU\CSCI 3771\djangoSite>heroku ps:scale web=1
					Scaling web processes... done, now running 1
				Check app's processes
					C:\Users\Initia7_B\Documents\HPU\CSCI 3771\djangoSite>heroku ps
					Process  State      Command
					-------  ---------  -------------
					web.1    up for 2m  python app.py
				Check the logs
					C:\Users\Initia7_B\Documents\HPU\CSCI 3771\djangoSite>heroku logs
					2012-04-30T00:59:29+00:00 heroku[slugc]: Slug compilation started
					2012-04-30T00:59:55+00:00 heroku[api]: Config add PYTHONUNBUFFERED, PYTHONPATH, PATH, LD_LIBRARY_PAT
					H, LANG, PYTHONHOME, LIBRARY_PATH, PYTHONHASHSEED by bryan@wolfford.com
					2012-04-30T00:59:55+00:00 heroku[api]: Release v2 created by bryan@wolfford.com
					2012-04-30T00:59:55+00:00 heroku[api]: Release v3 created by bryan@wolfford.com
					2012-04-30T00:59:55+00:00 heroku[api]: Deploy 680a9a2 by bryan@wolfford.com
					2012-04-30T00:59:55+00:00 heroku[web.1]: State changed from created to starting
					2012-04-30T00:59:56+00:00 heroku[slugc]: Slug compilation finished
					2012-04-30T00:59:57+00:00 heroku[web.1]: Starting process with command `python app.py`
					2012-04-30T00:59:58+00:00 app[web.1]:  * Running on http://0.0.0.0:48411/
					2012-04-30T00:59:59+00:00 heroku[web.1]: State changed from starting to up
					2012-04-30T01:01:34+00:00 heroku[api]: Scale to web=1 by bryan@wolfford.com
				Visit the app
					C:\Users\Initia7_B\Documents\HPU\CSCI 3771\djangoSite>heroku open
					Opening http://high-light-6071.herokuapp.com/
					*opens in default browser*
					CELEBRATE!
			Try Shell access
				C:\Users\Initia7_B\Documents\HPU\CSCI 3771\djangoSite>heroku run python
				Running python attached to terminal... up, run.1
				Python 2.7.2 (default, Oct 31 2011, 16:22:04)
				[GCC 4.4.3] on linux2
				Type "help", "copyright", "credits" or "license" for more information.
				>>>
				Import a module
					>>> import polls
					import polls
					>>>
			Use a different WSGI Server
				add 'gunicorn==0.13.4' to requirements.txt
				change Procfile to 'web: gunicorn app:app -b 0.0.0.0:$PORT -w 3'