# quotes-app
A Django web app with a login system, authorization, and permission access

# Project Description
The quotes app was designed with readers in mind. It allows the user to write down the quote, 
along with relevant information such as the author (of course), the book or original source, the page number, and the year of publication.
The app also allows the user to create collections of quotes, similar to how playlists of individual songs can be created on a music streaming service.

# Tech Used
The project was built using Django. Before starting the project, I knew very little about the differences of the various possible frameworks.
However, from reading various articles and forums, I knew that Django was a "batteries-included" framework and had a template system 
for creating basic front-end UI that was paired with Bootstrap. I wanted to mainly explore various concepts of web-development that I have yet to learn in school such as creating software that
utilizes CRUD operations with a database, how login-systems are implemented in an application, and how we personalize the application for each user.
Thus, Django was a perfect match that allowed me to jump straight away into exploring these topics.

# Features

Each user can add quotes and fill in as many details as they would like. Depending on the information, it will be displayed alongside the quote in the quote list page.
<img width="1323" alt="Screen Shot 2023-01-01 at 4 30 52 PM" src="https://user-images.githubusercontent.com/104177348/210185995-38192d0e-5782-43bf-8bf6-9951532d2531.png">
<img width="1325" alt="Screen Shot 2023-01-01 at 5 03 54 PM" src="https://user-images.githubusercontent.com/104177348/210186014-f62ef4f1-27a7-48aa-9346-fcf91d184a3d.png">

User can also create collections of quotes. When a user signs up, the collection "All Quotes" is automatically created and cannot be modified. However, you can create as many quotes as you like and modify it as you like!
<img width="1314" alt="Screen Shot 2023-01-01 at 5 05 08 PM" src="https://user-images.githubusercontent.com/104177348/210186045-7e8f01a5-c222-44b5-a26b-61bce4ee667c.png">

I've coded the website to only show quotes that are created by the logged in user. This way, you are only able to access the quotations that you've made and you are not exposed to the quotations and collections that other users have made.
