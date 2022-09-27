# Task Manager

[![build](https://github.com/AABur/python-project-lvl4/workflows/Python_CI/badge.svg)](https://github.com/AABur/python-project-lvl4/actions/workflows/python-ci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/4a835accb4f3ea3647a3/maintainability)](https://codeclimate.com/github/AABur/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/4a835accb4f3ea3647a3/test_coverage)](https://codeclimate.com/github/AABur/python-project-lvl4/test_coverage)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Hexlet tests and linter status [![Actions Status](https://github.com/AABur/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/AABur/python-project-lvl4/actions)

**Task Manager** is a task management system similar to <http://www.redmine.org/>. It allows you to create tasks, assign executors, set task statuses and labels.

## System features

### Users

* Create, edit and delete users
* Authentication of users
* Only user can edit and update himself

### Statuses
* View, create, update, delete statuses only for logged in users
* If a status is related to a task - you can't delete it

### Tasks
* View, create, update tasks only by logged-in users
* Only the creator can delete tasks
* Tasks can be filtered according to their status, artist or label; it is also possible to display the tasks created by the current user
* If the user is associated with a task - it cannot be deleted

### Tags

* Only logged-in users can view, create, update and delete labels
* If a label is associated with a task - it cannot be deleted

### Used services

* Application works equally well with SQLite and PostgreSQL
* [Rollbar](https://rollbar.com/) is used for bugs handling.
* Project designed for deployment on [Heroku](https://www.heroku.com)

## Illustration of a working project

<https://powerful-bastion-61895.herokuapp.com/>

## Local deployment

Install [poetry](https://python-poetry.org/)

Clone repo:

```bash
git clone git@github.com:AABur/python-project-lvl4.git
```

Create .env file in project root dir:

```bash
SECRET_KEY=<django secret key>
ROLLBAR_ACCESS_TOKEN=<Rollbar access token>
```

Install project:

```bash
make setup
```

Launch server:

```bash
make run
```

Open **Task Manager**

```bash
make open
```

## Contributing

This is a learning project and the contribution is not accepted.

## License

[MIT License](https://github.com/AABur/python-project-lvl4/blob/main/LICENSE)
