## Deliverable 1

### Introduction

+ Topic: Library
+ Entities: Book - Book Instance - Genre - Author - Language - Libraries

This project will consist to create a web application with framework Django, in this project will create the webpage of a library. On the application we could see the books that the library will have and where are the nearest libraries in our location.

That will show which books are available and which Libraries have them. Also the books will be related with the author that wrote them and the gender. 

The Book Instance will contain the state about the books: availability ( the lending period, the owner ) and the user that take in lending the book.

![UML_Library](https://github.com/elskater98/ProjecteWeb_Pre-Assignment/blob/master/UML_llibreria.png)

### 1. Number and function of servers

We have three servers in our application. The first one is the __BD Server__ which is the responsible to give an answer to all 
the requirements from the application that needs to access his information. The second one is the __Server Application__ which 
is the responsible for attend petitions of clients and guaranty their access. Also, manages everything related with the DB. 
Finally, the __Web Server__ is the responsible to answer HTTP petitions of the clients answering with an HTML document (template).

### 2. Connections and dependences

In order to make the app works correctly, the Server Application have to be able to get response by the BD Server and the 
Web Server.

To get the request and the response of the HTTP, it needs the interaction with the Server Application and the BD Server. 
This interaction is necessary, because without the information and the management between different servers, it couldn’t 
make the necessary operations for the initial request.

### 3. States

The states in our application are all these where the client is situated every moment and are necessary for the correct 
working of the application in order to make a response every moment the client make a request.

+ __Required states__: login, logout, session started
+ __Optional states__: add content, edit the content, delete elements, register users

### Additional comments

In the Heroku part, we followed the professor [tutorial](https://github.com/carlesm/minidjangoapp/blob/master/deploymentfiles/heroku.md)
but we have some troubles with the _git push_ to heroku. All the things related with the deployment on Heroku are located on the 
[heroku](https://github.com/projecteweb-fjmm/LlibreriaWeb/tree/heroku) branch.
