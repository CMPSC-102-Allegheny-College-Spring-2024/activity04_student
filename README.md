## Survey

Prime finder

## Assigned

Friday, 9 Feb, 2024

## Due

Friday, 9 Feb 2024, 11:00am

## Project Goals

This activity invites you to edit and complete a poetry project. Much of the code already exists to count between  a `start` value to an `end` value. As the program is counting, the primality of each index value is shown using boolean logic. At the end of the counting, the average value between the `start` and `end` values is calculated and returned to the user.

Your goal is to complete this given code to function within a Poetry project. The code is to be run with command-line arguments for the `start` and the `end` values.

This project offers you the opportunity to ensure that you understand how to (i) run and understand basic python code and, (ii) how to complete a poetry project using given code to include command line parameters

## Installations

If you have not yet installed Python, Poetry and GatorGrade, you may find instructions below about how to install this software.

- Install Python. Please see:
  - [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
  - [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
  - [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)
- Install `gatorgrade`
  - First, [install `pipx`](https://pypa.github.io/pipx/installation/)
  - Then, install `gatorgrade` with `pipx install gatorgrade`
- [Install `poetry`](https://python-poetry.org/docs/)
- Install `VSCode` or another editor. See [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

## Initial Steps

- Locate and access the directory `poetryProject/` of your project. You will be working in this directory.

- Change into the directory: `cd poetryProject`.

- The "boiler plate" code for the project has already been created using the command: `poetry new primefinder`

- The source code to edit has already been placed into the project directory: `poetryProject/primefinder/primefinder/`

- Initialize Poetry: `poetry install` (Note: check that you are in the same directory as the file, `pyproject.toml`)

### Executing the Poetry Project

- Determine the online help capability of code: `poetry run primefinder --help`. If this command does not work properly then there is a problem with your code.

- Here you will notice that the code "runs" with errors, and you are unable to adjust the inputs from the command line. Your task is to complete the code so that these command line inputs may be adjusted.

- Review your notes and slides to determine the rest of the steps for the project!

- Once the code has been completed, the command to execute the code is similar to following: `poetry run primefinder --start 1 --end 10` which gives the below output.

``` bash
Starting value : 1
 Ending value : 10

 1 is prime: False
 2 is prime: True
 3 is prime: True
 4 is prime: False
 5 is prime: True
 6 is prime: False
 7 is prime: True
 8 is prime: False
 9 is prime: False

 The average of the values between 1 and 10 is: 5.0
```

## GatorGrade Checking

You can also use `gatorgrade` to check the baseline requirements of this assignment by running the following command in your terminal:

`gatorgrade --config config/gatorgrade.yml`

If `gatorgrade` shows that all checks pass, you will know that you have met baseline requirements of this project.


## Submission

As you are working, you are to commit and push regularly. The commands are the following.

```bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

This is a check mark grade.
