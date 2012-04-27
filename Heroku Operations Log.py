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
				C:\Users\Initia7_B\Documents\HPU\CSCI 3771\djangoSite>virtual venv --distribute
				'virtual' is not recognized as an internal or external command,
				operable program or batch file.

				C:\Users\Initia7_B\Documents\HPU\CSCI 3771\djangoSite>virtualenv venv --distribute
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
				(venv) C:\Users\Initia7_B\Documents\HPU\CSCI 3771\djangoSite>pip freeze > requirements.txt
				(venv) C:\Users\Initia7_B\Documents\HPU\CSCI 3771\djangoSite>cat requirements.txt
				Flask==0.8
				Jinja2==2.6
				Werkzeug==0.8.3
				distribute==0.6.24
			Declare process Types with Foreman/Procfile
				Create Procfile
				Add web: python app.py to Procfile
				(venv) C:\djangoSite>foreman start
				*Allow access through firewall*
				Test at localhost:5000 = "HelloWorld!" 
				Celebrate!
			Store App with Git
				create .gitignore containing venv and *.pyc
				
