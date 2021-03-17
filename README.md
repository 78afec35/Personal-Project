# Personal-Project - Website and Blog

Author: Suner Syuleyman

## Packages Used (Runtime Requirements)

### Core Utililites
+ click 7.1.2
+ Flask 1.1.2
+ itsdangerous 1.1.0
+ Jinja2 2.11.3
+ MarkupSafe 1.1.1
+ Werkzeug 1.0.1

### Extra Utilities

+ astroid 2.5
+ attrs 20.3.0
+ dnspython 2.1.0
+ email-validator 1.1.2
+ Flask-CLI 0.4.0
+ Flask-MySQL 1.5.2
+ Flask-SQLAlchemy 2.4.4
+ Flask-WTF 0.14.3
+ idna 3.1
+ importlib-metadata 3.7.2
+ iniconfig 1.1.1
+ is-disposable-email 1.0.0
+ isort 5.7.0
+ lazy-object-proxy 1.5.2
+ mccabe 0.6.1
+ packaging 20.9
+ pkg-resources 0.0.0
+ pluggy 0.13.1
+ py 1.10.0
+ pylint 2.7.1
+ pylint-flask 0.6
+ pylint-flask-sqlalchemy 0.2.0
+ pylint-plugin-utils 0.6
+ PyMySQL 1.0.2
+ pyparsing 2.4.7
+ pytest 6.2.2
+ SQLAlchemy 1.3.23
+ toml 0.10.2
+ typed-ast 1.4.2
+ typing-extensions 3.7.4.3
+ wrapt 1.12.1
+ WTForms 2.3.3
+ wtforms-validators 1.0.0
+ zipp 3.4.1

##  Development Environment Set-Up

### **Bootstrap Bash Script**

Once you have selected an Ubuntu 18.10 server from GCP. This sets up most of the environment.

    #!/bin/bash 
    apt-get update
    sudo su -
    useradd ubuntu
    sudo apt-get install build-essential xrdp xfce4 xfce4-terminal xfce4-goodies xorg dbus-x11 x11-xserver-utils software-properties-common apt-transport-https wget -y
    #Setting up XRDP
    sudo sed -i.bak '/fi/a #xrdp multiple users configuration \n xfce-session \n' /etc/xrdp/startwm.shsudo ufw allow 3389/tcp
    sudo /etc/init.d/xrdp restart
    sudo systemctl restart xrdp
    sudo apt-get install build-essential libcurl4-gnutls-dev libxml2-dev libssl-dev firefox -y
    sudo ufw allow 3389
    # setting up VSCode
    sudo apt update
    sudo apt install software-properties-common apt-transport-https -y
    wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
    sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
    sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
    sudo apt update
    sudo apt install code -y

### **GCP Shell set up**

This snippet in the Google Cloud Shell allows RDP traffic through. 

    gcloud compute firewall-rules create allow-rdp --allow tcp:3389

### **User Configuration**

Final part is to create a user to allow the XRDP client to log in. This done via the in built SSH client in GCP. 

    sudo passwrd ubuntu 

Then you enter your password and log in via RDP:

![RDP Connection Screen](ReadmeAssets/RDP.png)
![Desktop Screenshot](ReadmeAssets/XRDP.png)

## Software Design

### **Project management**

Trello has been used as the primary source of project management.

<https://trello.com/b/lOwC8NkE/personal-project>

![trello screenshot](ReadmeAssets/trello.png)

### **Architecture**

plaseholder

### **SWOT Analysis**
+ Strengths
    + Quick and easy to deploy
    + Agile and modular design
    + Quick to edit and introduce new features
    + Responsive website and systems
+ Weakneses
    + Many packages are used and that can introduce dependencies on all these packages being supported
    + Basic framework which means more complicated features might need an advanced framework
    + Rigid 3 tier architecture
+ Opportunities
    + There are many features that I would like to add onto this website
    + It can be integrated with more features and packages
    + Can be expanded from an application package framework into an application factory, allowing for microservices deployment
+ Threats
    + In it's current state it is vulnerable to SQL injections and other threats such as having keys and passwords available inside the server.
    + Cannot scale easily in its present form.
    + No automatic measures to handle crashes/ errors and incidents.  

## Programming/Software Development

### **Version Control System**

#### **GitHub**

I have used git and github to manage and store different version with different branches created for different features.

Public Git Page <https://github.com/78afec35/Personal-Project>

Clone Link <https://github.com/78afec35/Personal-Project.git>

![tree diagram](ReadmeAssets/git.png)

### **Tools used**


+ Jenkins
+ VS Code
+ Trello
+ Google Chrome
+ Google Cloud Platform (GCP)
+ Ubuntu 18.10
+ Bootstrap 4

## Testing

placeholder

## Systems Integration and Build

placeholder

## References

1. Kevin Powell - CSS Navbar - <https://www.youtube.com/watch?v=8QKOaTYvYUA&ab_channel=KevinPowell>
2. Corey Schafer - Tutorials - <https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g>
3. Background image - Langtang National Park, Nepal - Sergey Pesterev - <https://unsplash.com/@sickle>
4. Flask Tutorial - <https://flask.palletsprojects.com/en/master/tutorial/>
