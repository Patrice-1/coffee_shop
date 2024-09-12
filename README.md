# Coffee Shop Application

A python application that for a Coffee shop using OOP.

## Setup

1. Create a repository on github and copy its `SSH_link`.
2. On your terminal, navigate to the directory you want to set up your work and clone it by running `git clone <SSH_link>`.
3. Install the required environment(myenv) by running `python -m venv myenv`.
4. Activate virtual environment by running `source myenv/bin/activate`.

## Running the Application

Run `python -m <module_name>` to run the application i.e `python -m customer` or `python <script_name>` i.e `python customer.py`.
Run `deactivate` to exit virtual environment.

## Saving your work

Run `git add .` to stage all changes for commit.
Run `git commit -m "<commit_message>"` to commit changes.
Finally run `git push` to push the changes to the main repository on github.
**NB**: Run the above commands everytime you make changes to your work to save the progress. 
## Domain Model

The domain model consists of three models: `Customer`, `Coffee`, and `Order`. A `Coffee` has many `Orders`, a `Customer` has many `Orders`, and an `Order` belongs to a `Customer` and a `Coffee`.