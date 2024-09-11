# Coffee Shop Application

A python application that for a Coffee shop using OOP.

## Setup

1. Create a repository on github and copy its `SSH_link`.
2. On your terminal, navigate to the directory you want to set up your work and clone it by running `git clone <SSH_link>`.
3. Install the required environment(myenv) by running `python -m venv myenv`.
4. Activate virtual environment by running `source myenv/bin/activate`.

## Running the Application

Run `python <module_name>` to run the application i.e `python3 -m coffee`
## Domain Model

The domain model consists of three models: `Customer`, `Coffee`, and `Order`. A `Coffee` has many `Orders`, a `Customer` has many `Orders`, and an `Order` belongs to a `Customer` and a `Coffee`.