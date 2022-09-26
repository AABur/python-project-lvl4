# Task Manager

[![Maintainability](https://api.codeclimate.com/v1/badges/4a835accb4f3ea3647a3/maintainability)](https://codeclimate.com/github/AABur/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/4a835accb4f3ea3647a3/test_coverage)](https://codeclimate.com/github/AABur/python-project-lvl4/test_coverage)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Hexlet tests and linter status [![Actions Status](https://github.com/AABur/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/AABur/python-project-lvl4/actions)

**Task Manager** is a task management system similar to <http://www.redmine.org/>. It allows you to create tasks, assign executors, set task statuses and labels. Registration and Authentication are required to use the system.

## System features

* Registration of users
* Only the user himself can edit and update himself
* Only the logged in users can add, edit and view tasks, statuses and labels.
* A task consists of a name and a description. Each task can have a person to whom it is assigned.  Also each task has a mandatory fields - author (set automatically when creating the task) and status.
* If a user is assigned to a task, it cannot be deleted.
* Only the task author can delete tasks
* If a status is associated with at least one task it cannot be deleted
* Labels are a flexible alternative to categories. Allows grouping tags by different attributes, e.g. bugs, features etc.
* If a label is associated with a task, it cannot be deleted.
* A task filter allows to filter tasks by status, artist, label and display tasks authored by the current user.
* [Rollbar](https://rollbar.com/) is used for error handling.
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
