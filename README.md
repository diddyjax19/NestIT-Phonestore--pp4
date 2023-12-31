# NestIt Store - An Online store App!

## [](https://github.com/diddyjax19/NestIT-Phonestore--pp4#)[![](readmeDocumentation/screenshots/responsive.png)](readmeDocumentation/screenshots/responsive.png)

The NestIt Phone Store is  regular store where people can go to browse and order from a variety of phone and accesories.The store is open 24 hrs with staffs processing order to meet the clients need, it also as a place where customers can register and be part of the community to receive deals and promotions.Through the The NestIt store, users can check thier orders and the status of the delivery,they are also aware of where the good are coming from it.

A simple online market place built with the Django Framework using HTML, CSS and Javascript

This fictional site was created for Portfolio Project #4 (Full-Stack Toolkit) - Diploma in Full Stack Software Development Diploma at the [Code Institute](https://www.codeinstitute.net).

[View live website here](http://diddy.pythonanywhere.com/)

## [](https://github.com/diddyjax19/NestIT-Phonestore#toc)Table of Contents

# Table of contents

  * [Project goals](#project-goals "Project goals")
  * [UX](#ux "UX")
     * [User stories](#user-stories "User Stories")
     * [Database](#database "Database")
     
     
  * [Features ](#feature "Features")
      * [Navigation](#navigation "Navigation")
      * [Home page](#home-page "Home Page")
      * [Registration page](#registration-page "Registration page")
      * [Categories](#categories "Categories")
      * [About Us Page](#about-Us-Page "About Us Page") 
      * [Contact Page](#Contact-Page "Contact Page")
      * [Cart Page](#Cart-Page "Cart Page")
      * [My Account](#My-Account "My Account")
      * [Orders](#orders "Orders")
      * [Cart](#Cart "Cart")
      * [Change Password](https://github.com/diddyjax19/NestIT-Phonestore#change-password)
    

  * [Design](#design "Design")
      * [Colours](#colours "Colours")
      * [Typography](#Typography "Typography")
      * [Images](#images "Images")
      * [Wireframes](#Wireframes "Wireframes")
  * [Libraries And Installed Packages](#Libraries-And-Installed-Packages "Libraries And Installed Packages")
  * [Testing](#Testing "Testing")

  * [Deployment](#Deployment "Deployment") 
  * [Technologies Used](#Technologies-Used "Technologies Used")
  * [Security Features](#Security-Features "Security Features")
  * [Credit](#Credit "Credit")
  * [Acknowledgements](#Acknowledgements "Acknowledgements")


# Project Goals
***
The NestIt Phone Store is  regular store where people can go to browse and order from a variety of phone and accesories.The store is open 24 hrs with staffs processing order to meet the clients need, it also as a place where customers can register and be part of the community to receive deals and promotions. Through the The NestIt store, users can check thier orders and the status of the delivery,they are also aware of where the good are coming from.

# UX
***
 ## User Stories 
 ***

My Project was developed with agile planning. I had three columns: To Do, In Progress, and Done. This helps me to manage my project and helps me to be more flexible and adaptable to changes.
Below are the User stories that were used in creating this project. I add 8 EPIC with labels MUST, SHOULD-HAVE.

I have included links to the [GitHub Issues](https://github.com/diddyjax19/NestIT-Phonestore--pp4/issues) for this project, as well as the [KANBAN board](https://github.com/users/diddyjax19/projects/7).


## Database:
![SQL Database model](readmeDocumentation/screenshots/database_model.png)


<details>
<summary>Click to see more</summary>

1 EPIC - Home Page and Navigation Bar

    * As a Site User I can easily navigate around the site so that I can view different pages. As a Site User, I want to see a home page with basic information about the app.
2 EPIC - Account registration 

    * As a Site User I want to be able to create an account and log in into my app with my username and password.

3 EPIC - Add CRUD functionality

    * As a Site User I want to browse the website. .
    * As a Site User I want to browse my categories.
    * As a Site User I want to update my cart.
    * As a Site User I want to delete cart from my cart page. 

4 EPIC - Categories Page 

   * As a Site User I want to be able to navigate the categories page,This page has an sub-section that houses all the categories and products that are on the website.

5 EPIC - About page
    
   * As a Site User I want to have a page where the user can read about the website and it founder.

6 EPIC - Contact Page

   * As a Site User I want to contact the website owner directly. In this Section the User can fil a form and leave a request.

7 EPIC - Cart Page 
   
   * As a Site User I want to be able view the products added to the cart,increase the quantity of the product,delete the product in the cart,view the shipping address before checkout and the various payment options available.

8 EPIC - Profile Page 
   
   * As a Site User I want to be able login to the website and be able to add new shipping address,view the address on file and view the orders on the website.

9 EPIC - Orders Page 
   
   * As a Site User I want to be able view all the orders placed on my account and thier respective status.

10 EPIC - Change Password Page 
   
   * As a Site User I want to be able to change my password.

11 EPIC - Create Account Page 
   
   * As a Site User I want to be able to create an account,with all the neccessary inofrmations.

12 EPIC - Log-in Page 
   
   * As a Site User I want to be able login to the website,with the right credentials .  



</details>

# Features  
  ***
<details>
<summary>Click to see more</summary>

 ## Navigation Bar

 ![](readmeDocumentation/screenshots/navigation-menu-web-not-login.png)

 * The navigation menu consists of Logo-text,Categories,About,contact, Log In and Create Account. By clicking on the Logo, the user can always return to the Home page. 
 If the User is new, he will have to register, and if the User already exists, he can easily Log In to his Nestit webpage. When the User login, some links on the navigation bar will change, and the user will be able to see the cart and My Account.

 ![](readmeDocumentation/screenshots/navigation-menu-web-loggedin.png)

 * Also on the small screen the navigation menu will be changed to the burger menu which shows all the navigation links.

 ![](./readmeDocumentation/screenshots/navigation-menu-mobile-loggedin.png)


 ## Home Page
 ![](readmeDocumentation/screenshots/homepage.png)

 * The home page has a welcome message and a short description of the application. At the bottom are three bright images of a recipe with the small guide on what users can do with this app.

 ## Registration page
  
 * Django allauth was installed and used to create the Sign-Up, Login, and Log Out functionality and pages

   * Sign UP

 * The user has to fill up the fields in the registration form: username, email, and password. If the User already exists they can click on the top page Sign In button, and will be transferred to the log-in form.
 ![](readmeDocumentation/screenshots/create-account.png)
   
   * Log In

 * Log in form is similar to Sign up, only has a few fields username and a password. If the User forgotten to register as a new user,on the top of the Sign Up page there is a Sign Up link were the user can Sign Up. 
 ![](readmeDocumentation/screenshots/signup.png)

   * Success/unsuccess messages 

 * Success messages inform the user if they already have an account, enter the wrong password or username or enter the short password by creating a new account user.
 ![](readmeDocumentation/screenshots/user-existalready.png)
 ![](readmeDocumentation/screenshots/incorrect-password.png)
 ![](readmeDocumentation/screenshots/password-2short.png)

 ## Categories 

 * This is the main page where all created categories are saved. Under each category is the title of the manufacturer of the phone.

 ![](readmeDocumentation/screenshots/catergories.png)


 * By clicking on the image of the category, the user will be see all the phones avaliable from that manufacturer.

 ![](readmeDocumentation/screenshots/catergories-2.png)

 * At selecting the phone he is then redirected to the product description.In this section the user can view all the specification and the price.In this section the user is able to get see a  complete detail of the product and also see similar products.

 ![](readmeDocumentation/screenshots/Product-detail.png)

 ![](readmeDocumentation/screenshots/Product-detail2.png)

 ![](readmeDocumentation/screenshots/Product-detail2.png)

   ## About Us Page

 * This section tell the user a brief description of the website and a hiistory of the website.

 ![](readmeDocumentation/screenshots/about-us.png)

   ## Contact Page

 * In this section,the user has the opportunity to contact us directly or reach out to make enquiry.

 ![](readmeDocumentation/screenshots/contact.png)

   ## Cart Page

 * Under this Section you can see the products added to the cart,you can see the shippping address that are on your profile,you can also see a button that redirect you to continue shopping and also all the payment option available.
   
 ![](readmeDocumentation/screenshots/cart.png)
 ![](readmeDocumentation/screenshots/checkout.png)
    
 ## My Account

 ![](readmeDocumentation/html-validator/css.png)

 ## Profile

 * Under this page you will find the shipping address and all the items and their status.It also gives the user the ability to add address.

 ![](readmeDocumentation/screenshots/profile.png)

 ## Cart

 * Under this Section you can see the products added to the cart,you can see the shippping address that are on your profile,you can also see a button that redirect you to continue shopping and also all the payment option available.
   
 ![](readmeDocumentation/screenshots/cart.png)
 ![](readmeDocumentation/screenshots/checkout.png)


## Orders

 * In this section,the user can see all the orders they have placed under their account,it shows the product name,the picture of the product,the quantity of product placed,the date the order was placed, and the current status of the order {completed,accepted,cancelled,delivered and pending}.

 ![](./readmeDocumentation/screenshot/addRecipeForm.png)

 ## Change Password 

 * In this section,the user can reset his password.

 ![](readmeDocumentation/screenshots/change-password.png)


</details>

 # Design 
  ***
## Colours

  * The colour scheme was chosen by the background image of the project. I used black for the footer and white for the background.

## Typography

* The font chosen for the website is a font called "Libre Franklin", sans-serif. I used this font because Merriweather font is ideal for text-dense design: the letterforms have a tall x-height but remain relatively small, making for excellent readability across screen sizes while not occupying extra horizontal space. The font was found on [Google Font](https://fonts.google.com/) and imported to the website through a CSS import.

## Images

* All images were all taken from numerous website and compressed to the specificity of the products. 


## Wireframes

<details>
<summary>Click to see more</summary>

### Home Page - Mobile: 

![Home Page](readmeDocumentation/wireframe/home-page.jpg)

### Category page - Mobile: 

![Category Page Mobile](readmeDocumentation/wireframe/category-page.jpg)

##### About US - Mobile: 

![About US -Mobile](readmeDocumentation/wireframe/aboutus-page.jpg)

##### Cart page - Mobile: 

![Desktop Mobile](readmeDocumentation/wireframe/cart-page1.jpg)
![Desktop Mobile](readmeDocumentation/wireframe/cart-page2.jpg)


##### Profile Page - Mobile: 

![Profile Page - Mobile](readmeDocumentation/wireframe/profile-page.jpg)

##### Order Page - Mobile: 

![Order Page - Mobile](readmeDocumentation/wireframe/order-page.jpg)

##### Change Password Page - Mobile: 

![Change Password](readmeDocumentation/wireframe/change-password.jpg)

##### Signup Page - Mobile: 

![Signup Page](readmeDocumentation/wireframe/create-account.jpg)

##### Login Page - Mobile:

![Login Page](readmeDocumentation/wireframe/login-page.jpg)

##### Site Navigation - Mobile:(logged-In)

![Mobile:(logged-In)](readmeDocumentation/wireframe/navigation-login.jpg)

##### Site Navigation - Mobile:(Logged-Out)

![ Mobile:(Logged-Out)](readmeDocumentation/wireframe/navigation-sigin.jpg)

</details>

# Testing 
***

Details of all testing done can be viewed in depth in the 

[Link to TESTING.md](https://github.com/diddyjax19/NestIT-Phonestore--pp4/blob/main/TESTING.md) document.

 ## [](https://github.com/diddyjax19/NestIT-Phonestore--pp4#deployment)Deployment

### [](https://github.com/diddyjax19/NestIT-Phonestore--pp4#forking-the-github-repository)Forking the GitHub Repository

1.  Go to [the project repository](https://github.com/diddyjax19/Taskit-FrontEnd)
2.  In the right most top menu, click the "Fork" button.
3.  There will now be a copy of the repository in your own GitHub account.

### [](https://github.com/diddyjax19/NestIT-Phonestore--pp4#running-the-project-locally)Running the project locally

1.  Go to [the project repository](https://github.com/diddyjax19/Taskit-FrontEnd)
2.  Click on the "Code" button.
3.  Choose one of the three options (HTTPS, SSH or GitHub CLI) and then click copy.
4.  Open the terminal in you IDE program.
5.  Type `git clone` and paste the URL that was copied in step 3.
6.  Press Enter and the local clone will be created.

### [](https://github.com/diddyjax19/NestIT-Phonestore--pp4#alternatively-by-using-gitpod)Alternatively by using Gitpod:

1.  Go to [the project repository](https://github.com/diddyjax19/Taskit-FrontEnd)
2.  Click the green button that says "Gitpod" and the project will now open up in Gitpod.

### Manual Deplyoment In Python Anywhere:

# Deployment
The site was deployed to Heroku. The following steps were taken:
- Install Django & Gunicorn:
```pip install 'django<4' gunicorn```
- Install Django database & psycopg:
```pip install dj_database_url psycopg2```
- Creating the requirements.txt file with the following command:
```pip freeze --local > requirements.txt```
- Django project created using:``
```django-admin startproject phonestore```
- Django project created using:``
```django-admin startapp store```
- the changes were then migrated using:
```python3 manage.py makemigrations```
- the changes were then migrated using:
```python3 manage.py migrate```
- navigated to [Heroku](www.heroku.com) & created a new app called nestit.
- added the Heroku Postgres database to the Resources tab.
- navigated to the Settings Tab, to add the following key/value pairs to the configvars:
1. key: SECRET_KEY | value: randomkey
2. key: PORT | value: 8000
3. key: CLOUDINARY_URL | value: API environment variable
4. key: DATABASE_URL | value: value supplied by Heroku
- added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the env.py file
- added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the settings.py file
- add an import os statement for the env.py file.
- added Heroku to the ALLOWED_HOSTS in settings.py
- created the Procfile
- pushed the project to Github
- connected my github account to Heroku through the Deploy tab
- connected my github project repository, and then clicked on the "Deploy" button

## Final Deployment

### Gitpod
- Ensure 'DEBUG = FALSE' in settings.py
- Add "X_FRAME_OPTIONS= 'SAME ORIGIN'" to settings.py, to ensure that summernote editor works in deployed project.
- Add, commit and push deployment commit to GitHub.

### Heroku
- Go to 'Settings' tab and reveal config vars. Remove COLLECT_STATIC environment variable.
- Go to 'Deploy' tab and scroll down to 'Deploy Branch' (ensure github repo is connected). Run deployment.
- Wait for confirmation that application has deployed.

# How to set up environment variables in Django for security
It is important to keep sensitive bits of code like API keys and passwords away from the public.

1. Install Django Environ
In your terminal, inside the project directory, type:

`$ pip install django-environ`

2. Import environ in settings.py
`import environ`

3. Initialise environ
Below your import in settings.py:

```
    #Initialise environment variables
    env = environ.Env()
    environ.Env.read_env()
```

4. Create your .env file
In the same directory as settings.py, create a file called `.env`

5. Declare your environment variables in .env
Make sure to use quotations around strings.

    SECRET_KEY = "*******"
    DEBUG = "********"
    DATABASE_URL = "********"
    CLOUDINARY_URL = "*************"

6. IMPORTANT: Add your .env file to .gitignore
If you don’t have a .gitignore file already, create one at the project root. Make sure the name of your .env file is included.

7. Replace all references to your environment variables in settings.py, like so

## Technologies Used

* [GitHub](https://github.com/diddyjax19/NestIT-Phonestore--pp4) - is Used in conjunction with Gitpod as the code editor, to store the project and utilise git version control.
* [Python Anywhere](https://www.pythonanywhere.com/user/Diddy/) -  Used to deploy and host the finished product.
* [W3C](https://validator.w3.org/) - HTML Used to validate all HTML code.
* [W3C](https://jigsaw.w3.org/css-validator/) - CSS Used to validate all CSS code.
* [CI PEP8](https://pep8ci.herokuapp.com/) -  Testing Used to validate all Python code.
* [Google Fonts](https://fonts.google.com/) - Used to provide the fonts used in application styling.
* [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Used to aid the implementation of styling and responsiveness.
* [Fontawesome](https://fontawesome.com/) - is Used to implement effective icons.
* Google Chrome Dev Tools -  Used during the development to debug and test responsiveness.
* [Ax Dev Tools](https://chrome.google.com/webstore/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd) - Find and fix more accessibility issues during website development with axe DevTools. 

# Modules Used
- asgiref==3.3.4
- bcrypt==4.0.1
- certifi==2023.7.22
- cffi==1.15.1
- charset-normalizer==3.2.0
- cloudinary==1.34.0
- cryptography==41.0.1
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==3.2.3
- django-environ==0.10.0
- django-heroku==0.3.1
- gunicorn==21.2.0
- idna==3.4
- mysqlclient==2.1.1
- packaging==23.1
- paramiko==3.2.0
- Pillow==9.5.0
- psycopg2==2.9.7
- psycopg2-binary==2.9.7
- pycparser==2.21
- PyNaCl==1.5.0
- python-dotenv==1.0.0
- pytz==2021.1
- requests==2.31.0
- six==1.16.0
- sqlparse==0.4.1
- typing_extensions==4.7.1
- urllib3==1.26.15
- whitenoise==6.5.0 

# Brief Writeup on few of the libaries Used
***
  * Django -crispy-forms - Used to render forms throughout the project.
  * Django - allauth - Allows authentication, registration and account management in Django.
  * django-environ - is the Python package that allows you to use Twelve-factor methodology to configure your Django application with environment variables.
  * mySqlclient - Python interface to MySQL.
  * sqlparse - sqlparse is a non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements. 
  * pytz - This library allows accurate and cross platform timezone calculations using Python 2.4 or higher.
  * PyNaCl -PyNaCl is a Python binding to libsodium, which is a fork of the Networking and Cryptography library. 
  * pycparser- pycparser is a complete parser of the C language, written in pure Python using the PLY parsing library. It parses C code into an AST and can serve as a front-end for C compilers or analysis tools.
  * Pillow -The Python Imaging Library adds image processing capabilities to your Python interpreter.
  * Paramiko -Paramiko is a pure-Python 1 (3.6+) implementation of the SSHv2 protocol 2, providing both client and server functionality. It provides the foundation for the high-level SSH library Fabric, which is what we recommend you use for common client use-cases such as running remote shell commands or transferring files.
  * bcrypt - Acceptable password hashing for your software and your servers
  * Asgiref - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI.
  * Cryptography - A set of primitives for easily encrypting data in Django, wrapping the Python Cryptography library
  * cffi - C Foreign Function Interface for Python. Interact with almost any C code from Python, based on C-like declarations that you can often copy-paste from header files or documentation. 


# Security Features

* Users can not add to cart with first Signing in or Signing up..

* Error messages for not adding a shipping address to file. 

* Error messages for incorrect inputs on sign in/sign up form


# Credits    
* [Stack Overflow](https://try.stackoverflow.co/explore-teams/?utm_source=adwords&utm_medium=ppc&utm_campaign=kb_teams_search_brand_emea-dach&_bt=657236278309&_bk=stack+overflow&_bm=p&_bn=g&gclid=CjwKCAjwhdWkBhBZEiwA1ibLmF2ghGSQXiKfjiQcnpRL_87pacwew2yt-jYDV9_z56sxtUF-BMthsRoCB7oQAvD_BwE)
* [Codemy.com](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) 
* [Django documentation](https://docs.djangoproject.com/en/4.2/)
* [LinkedIn Learning](https://www.linkedin.com/learning/paths/become-a-django-developer)
* [E-commerce website with django](https://www.youtube.com/watch?v=YZvRrldjf1Y)
* [Codecademy](https://www.codecademy.com/?g_network=g&g_productchannel=&g_adid=528849219280&g_locinterest=&g_keyword=codecademy&g_acctid=243-039-7011&g_adtype=&g_keywordid=kwd-41065460761&g_ifcreative=&g_campaign=account&g_locphysical=1007835&g_adgroupid=70492864474&g_productid=&g_source={sourceid}&g_merchantid=&g_placement=&g_partition=&g_campaignid=1726903838&g_ifproduct=&utm_id=t_kwd-41065460761:ag_70492864474:cp_1726903838:n_g:d_c&utm_source=google&utm_medium=paid-search&utm_term=codecademy&utm_campaign=INTL_Brand_Exact&utm_content=528849219280&g_adtype=search&g_acctid=243-039-7011&)

# Acknowledgements

Martina Terlevic: For help and support throughout a tough year.

