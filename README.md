This is my first Django project. It's a web app designed to help people track monthly subscription services.

In March 2017 I started learning Django. Here are tutorials I did (roughly) in order:

- [Obey The Testing Goat](http://www.obeythetestinggoat.com/)

- [Official Django Tutorial (Polling App)](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)

- [Idea Langing Page (by Justin M.)](https://www.youtube.com/playlist?list=PLEsfXFp6DpzTgDieSvwKL3CakR8XyKkBk)

- [Django Web Frame Work (by Max G.)](https://www.youtube.com/playlist?list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj)

- [Try Django 1.9](https://www.youtube.com/playlist?list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy)

There is a lot covered in these five tutorials and it provided a good foundation of learning the basic structure of a Django Project, adding apps, writing views, wiring up URL patterns, writing models, the Django ORM, the Django templating language, user authentication, the Django admin, forms and a little bit of the Django ReST Framework, as well as Bootstrap 3 and deploying to Heroku (or Amazon).

The commit history shows that I tried to use class-based views for a good portion of the CRUD functionality, but I later abandoned this in favor of function-based views. I wanted to get a stronger understanding of the basics, and I had some trouble with flexibility of the class-based views. There is lots of inheritance going on and I didn't fully understand how to override certain functions. I was able to see the simplicity and power of class-based views and I look forward to delving into them in more detail in the next project or in later stages of this project.

Here's a basic overview of what the app allows users to do:

* Create an account, verify email, setup a basic profile
* Reset password, recover forgotten password
* Add "subscriptions" to their profile that shows the service they are subscribed to, how much they are spending on it, the date they started using the service and the nickname of the credit card they are using to pay for it
* Add a service to their wish-list
* Edit their subscriptions
* Make individual subscriptions private so that they are visible only to the user
* List a new service
* Leave a comment on a service
* Comment on comments (using ContentType and generic foreign keys)
* Flag comments as inappropriate
* Delete their own comments
* Write articles for the blog portion of the site
* Tag blog articles with keywords (using [Django Taggit](https://github.com/alex/django-taggit))
* Associate one or more services with their article
* Comment on blog articles and other comments
* "Like" blog articles with an AJAX-powered like-button (using the Django ReST Framework)
* Follow users
* See follower list and list of users they are following on their profile
* Message other users
* View message inbox
* Search for services using a search bar
* Browse categories and tags
* Share their profile on social media
* Share other user's profile on social media

There are a few things I would still like to figure out how to do:

* Schedule custom emails to users each month (using Celery, perhaps?)
* Provide users with a survey where they can select their interests and generate subscription recommendations based on their interests and current subscriptions
* Restrict users from adding more than 5 or 6 subscriptions unless they have a premium account
* Integrate Stripe to accept payments for premium membership
* Show page-view count for users' profiles
* Let premium members see who viewed their profile
* Let premium members make their profile private
* Image hosting with Amazon S3
* Better UI (Angular?)
* "Similar" services displayed on each service page
* Django allauth for social authentication
* Do more with Django ReST Framework
* Notifications as implemented in [Try Bootcamp](trybootcamp.vitorfs.com/)

I have been able to successfully implement django allauth on a test-site, and I would eventually like to let users sign in with Facebook or Twitter, and let them connect with FB or Twitter friends who are already members. For now, the default email-based signup/login system is sufficient.
