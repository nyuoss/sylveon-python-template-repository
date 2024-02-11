# Sylveon

[![CircleCI Status](https://dl.circleci.com/status-badge/img/circleci/3xWZeNMCu5Vj5AMLtYkBLD/3BbpjRhT2mTt2SAzHyziCj/tree/main.svg?style=svg&circle-token=a3755171dc7af90c9eed83c7eb96aa5f59faef63)](https://dl.circleci.com/status-badge/redirect/circleci/3xWZeNMCu5Vj5AMLtYkBLD/3BbpjRhT2mTt2SAzHyziCj/tree/main)

## Description

This is a template repository for Python designed to work out of the box for developing software projects. This repository provides the fundamental building blocks needed to design and develop projects including:

- Build Management
- Unit Testing
- Continuous Integration
- Static Analysis
- Code Formatting
- Component Specification

A template for issue and pull requests is also provided for collaborative development.

## Setup (PDM)

### Requirements

- [PDM](https://pdm-project.org/latest/)

### Instructions

1. Clone project repository to your local machine
2. Initialize repository using `pdm install`
3. Update dependencies using `pdm update`
4. Activate virtual environment using `pdm venv activate`
5. Run the project using `pdm run start`

### Scripts

View available scripts using `pdm run --list`

- `start` - Start the project
- `test` - Run tests
- `lint` - Run static analysis
- `format` - Format code
- `format-test` - Dry run for code formatting

## Component Specification

For the purposes of this project, and scope of this template, we are defining a component to be any group or individual module which performs a standalone functionality, utility, or otherwise.

In structuring these components, we use the `__main__.py` file as the entry point into this application. Other utilities ("components") may be imported, but are not intended to be accessed by users. These are marked as such with a single underscore in front of the file name (e.g. _accessory.py)

We have included two examples of components which are imported into the `__main__.py` file: one is "Hello World" which is not intended to be accessed by users, and the second is a component which finds the length of a string, which is meant to be accessed by users. 

The "Hello World" component is a basic module which provides a function to print the greeting message "Hello World!" 

The "String Length" component is designed to calculate the length of a given string. 

We have imported both modules into the `__main__.py` file, to showcase how components can be imported into different files within a Python project. As seen from the code structure below (which only includes files relevant to the components) our import strategy assumes that all components will be within the `src/sylveon` directory. 

```
src/sylveon/
|-- __init__.py
|-- __main__.py
|-- _hello/
|   |-- __init__.py
|   |-- _greeting.py
|-- string_length/
|   |-- __init__.py
|   |-- find_length.py

```

## Objectives

1. Programming Language: ```Python``` ✅
2. Toolchain/Runtime Environment: ```Python``` >= 3.12 ✅
3. Testing Framework: ```pytest``` ✅
4. Continuous Integration Solution: ```CircleGI``` ✅
5. Static Analysis Tool: ```mypy```✅
6. Code Formatting Solution: ```black``` ✅
7. Package Manager: ```pip/PDM``` ✅
8. Python Dependency Management ✅
9. Component Specification: ✅
10. Issue and Pull Request Templates ✅

## Authors

- Susmitha Kusuma
- Berry Liu
- Margaret Jagger
- Calvin Tian
- Kevin Zheng
