# Django Music Collection

Create an application to keep track of all the music albums you own. You can choose what fields each album should have, but it should have at least these three:

- title
- artist
- year released

Your Django app should allow you to do the following:

- See a list of all albums (this should be your homepage)
- Create a new album
- See a detail page for one existing album
- Edit an existing album
- Delete an existing album

Your app should have at least minimal styling using a CSS library like Tachyons, Material, or Semantic.

A good place to start is planning out your model and making sure you can make an Album object in the console. Make some simple wireframes to sketch out the different functions of the app on the list above, and the urls (and corresponding view functions) you will need to make each page show up. Start with the home page.

## Spicy options 🌶️🌶️🌶️

- Add an Artist model and create a foreign key on the Album model to associate the two.
  - Show the Artist and their other albums on the album detail page, with links to those album detail pages.
- Create an way to mark an album with a star rating.
- Add an option to sort all albums on the list page by title, year, or artist.

## Getting up and running

In your project directory, run the following to install the project dependencies, set up your virtual environment, and run the existing database migrations. After you do these steps you can run your server.

```
$ pipenv install
$ cp django_music/.env.sample django_music/.env
$ pipenv shell
$ python manage.py migrate
```
Alternative:
```
$ pip install -r requirements.txt
```

This app uses [Django Registration Redux](https://django-registration-redux.readthedocs.io/en/latest/quickstart.html?highlight=urls) to provide a process for users to register. You will see it added to settings and urls. Redux requires a template called `base.html`. To register for the first time, a user vists `accounts/register`, to login visit `accounts/login` and to logout visit `accounts/logout`.


To generate an app in your django_music project (so that you have something analogous to `contacts` in the Uptact assignment), you want to run the following (where <name_of_app> is a name you can choose) in your repo:

`django-admin startapp <name_of_app>`

If you ran `django-admin startapp albums`, your directory structure would look like:

```
.
├── README.md
├── albums
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── django_music
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── pyproject.toml
├── static
├── templates
└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
7 directories, 23 files
```

Once you have your app set up, be sure to add it to the `INSTALLED_APPS` list in `settings.py`.

### Turning it in

We are going to use a new way of turning this in. DO your work in a branch and then create a pull request with your work.

### Django Project Template

This project was generated from the Momentum Django project template. This template sets up some minimal changes:

- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) and [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) are both installed and set up.
- [django-environ](https://django-environ.readthedocs.io/en/latest/) is set up and the `DEBUG`, `SECRET_KEY`, and `DATABASES` settings are set by this package.
- There is a custom user model defined in `users.models.User`.
- There is a `templates/` and a `static/` directory at the top level, both of which are set up to be used.
- A `.gitignore` file is provided.
- [Pipenv](https://pypi.org/project/pipenv/) is used to manage dependencies.

