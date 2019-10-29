ShopKeepr:

An automated requirements manager for python projects.



Ever felt that updating the requirements.xt file is a bit too tedious? or too bloated with a lot of dependencies? Same. A lot of times it happens that after uninstalling a package from your project, there are dangling dependencies still left.

ShopKeepr takes care of it all for you by maintaining a state of all packages and dependencies installed for the project you're working on, removing all unused dependencies when you uninstall a package and update the requirements.txt file automatically whenever you make a change to the state of installed packages for your projects in your virtual environment.



Installation Instructions:

```
pip3 install shopkeepr
```



Usage Instructions:

```
keepr <command> <package list>
```



Commands:

* install - Install Packages
* uninstall - Uninstall Packages and dependencies
* update - Update an existing package
* help - Display Help information
* credits - List author credits



Example:

```
keepr install django==2.2 pymongo==1.2
```



**Note:** 
 
* The application currently supports 'venv' to manage the virtual environment for the project you're working on.     

* The application makes use of a sqlite database named 'packages.db' under each project. You'd need to add that to your .gitignore file to avoid pushing it to your repo.
