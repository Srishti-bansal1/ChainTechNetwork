# ChainTech Network
`http://127.0.0.1:8003/ChainTEMP`  clicked on it to go my project interface.

swagger link - `http://127.0.0.1:8003/swagger/`

# Introduction <br>

This is a User Login project . In this project I used python language (version 3.9 ) & Django Rest framework (version 4.2.9) for backend and HTML & JavaScript for frondend development. This project used to enrolled the user, read the user information.

In this project, I created 3 HTML pages. 1st is ChainTemp where I'm rendering the current Date-Time, weather information and random quotes. `http://127.0.0.1:8003/ChainTEMP` 
2nd is UserDataForm, this page is navigating to 1st page where user enter our details  
`http://127.0.0.1:8003/ChainForm` and this page is also connected with 3rd page which is dataTable where we will get user details `http://127.0.0.1:8003/ChainTable`  and we can also navigate 1st page to 3rd page . <br>

In this project , I Designed a model and their fields are name , email. Migrated the model to create a Table. Connected with MYSQL database. Created APIs for Create and Read operation. 
 <br>
`CHAIN/chain/show` use for read <br> `CHAIN/chain/add_create` use for create <br>
To rendered the current Date-Time , weather information and random quotes ` CHAIN/dynamic/dynamic`.
<br>
Exercise 1: Setting Up a Simple Web Page 
<br>
Exercise 2: Creating a Python Web Server  http://127.0.0.1:8003/ChainTEMP
<br>
Exercise 3: Adding Dynamic Content  http://127.0.0.1:8003/CHAIN/dynamic/dynamic
<br>
Exercise 4: Form Handling   http://127.0.0.1:8003/ChainForm
<br>
Exercise 5: Data Persistence  http://127.0.0.1:8003/ChainTable


<br>
# SetUp for Linux or MAC <br>
step 1 : open terminal and clone the code by executing  * git clone https://github.com/Srishti-bansal1/ChainTechNetwork.git *
<br>
step 2 : Install virtual environment  with command :  pip install virtualenv
<br>
step 3 : Create virtual environment  with command : ` virtualenv .venv`
<br>
step 4 : Activate the virtual environment with command :`source  .venv/bin/activate`
<br>
step 5 : Move in projct file with command :`cd ChainPro`
<br>
step 6 : Execute migration command to create table in database using command : python mange.py migrate
<br>
step 7 : Run the server with command : python manage.py runserver 8003
<br> 

# API Documentation -<br>
        1. Create :- End point -  http://127.0.0.1:8003/CHAIN/chain/add_create

                    request body - {	
                                        "name"   : <str> ,
                                        "email"  : <str>,
                                    }	
                    response body - {	
                                        "id "    : <int>,
                                        "name"   : <str> ,
                                        "email"  : <str>,
                                    }

        2. Read :- End point - http://127.0.0.1:8003/CHAIN/chain/show
        
                    response body - {	
                                        "id "    : <int>,
                                        "name"   : <str>,
                                        "email"  : <str>,
                                    }

# HTML Documentation - <br>
        1. Front page :-   End point - http://127.0.0.1:8003/ChainTEMP

                        response body - <HTML page>       

        2. Create user :-  End point - http://127.0.0.1:8003/ChainForm

                        response body - <HTML page>

        3. User table :-   End point - http://127.0.0.1:8003/ChainTable

                        response body - <HTML page>
                           	
