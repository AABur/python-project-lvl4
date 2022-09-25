[![Maintainability](https://api.codeclimate.com/v1/badges/4a835accb4f3ea3647a3/maintainability)](https://codeclimate.com/github/AABur/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/4a835accb4f3ea3647a3/test_coverage)](https://codeclimate.com/github/AABur/python-project-lvl4/test_coverage)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

### Hexlet tests and linter status [![Actions Status](https://github.com/AABur/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/AABur/python-project-lvl4/actions)

**Task Manager** is a task management system similar to http://www.redmine.org/. It allows you to create tasks, assign executors, set task statuses and labels. Registration and Authentication are required to use the system.

## Example of a working project

<https://powerful-bastion-61895.herokuapp.com/>




## Local deplotment

Clone repo:

```bash
git clone git@github.com:AABur/python-project-lvl4.git
```

Create .env file in project root dir: 

```
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
