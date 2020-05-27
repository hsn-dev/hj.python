# PIPENV ~ Virtual Environment

###### How to install
```batch
pip install pipenv
```

###### Create venv in new project
###### Install from Pipfile, if there is one
###### To update pipfile, if any changes were made manually
```batch
pipenv install
```

###### Or, add a package to your new project:
```batch
pipenv install <package>
```
This will create a Pipfile if one doesn’t exist. If one does exist, it will automatically be edited with the new package you provided.

###### Activate the Pipenv shell:
```batch
pipenv shell
```
This will spawn a new shell subprocess, which can be deactivated by using exit.

###### Check python executable:
```python
import sys
sys.executable
```

###### To run commands or scripts in venv without activating:
```batch
pipenv run <command>
pipenv run python <script> 
```

###### Install from requirements.txt file:
```batch
pipenv install -r "path/to/requirements.txt"
```

###### Create requirements file similar output from pipenv:
```batch
pipenv lock -r
```

###### Install package in dev environment:
```batch
pipenv install <package> --dev
```

###### Uninstall package:
```batch
pipenv uninstall <package>
```

###### Check for updates and security fixes in our packages
```batch
pipenv check
```

###### Dependencies Graph for Packages
```batch
pipenv graph
```

###### Update the lock file for use in production
```batch
pipenv lock
```

###### Run this command in production to install from pipfile.lock
```batch
pipenv install --ignore-pipfile
```

###### Create environment variables for specific virtual environments

Create a ```.env file``` within the project directory and set multiple environment variables within that file.
Don't commit .env file to git for security purposes.
```python
import os 
os.environ['<env-variable>']
```

###### Changing version of python of current virtual environment:
Manually change python version in pipfile and then run `pipenv --python <version>`
OR
Remove virtual environment `pipenv --rm` it will only remove venv not pipfiles.
After that recreate the environment using `pipenv install` it will install everything + your specific python version 


###### PIPFILE - (editable)
It uses a format called Toml which is similar to key-value pairs.
1. `[[source]]` tells from where we are installing the packages.
2. `[[packages]]` tells what packages are required and which version to install if * is given then it automatically installs updated version at that time. Otherwise we can manually specify a specific version to install.
3. `[[requires]]` tells which python version to install
4. `[[dev-packages]]` tells these packages should not be installed in production but if some other user want to get our project then that user can also install packages needed for development by just specifying --dev command.

###### PIPFILE.LOCK - (not editable)
It also contains information about dependencies. We can see the version of the packages installed.
1. It will always give you same deteministic builds.
2. that means pip file sees for new update and updated that packages after that if your project works fine in development then you can simply update your lock file and push your files to production.

