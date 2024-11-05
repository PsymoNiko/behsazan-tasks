# behsazan-tasks

# Python Developer Exercises

This repository contains a series of technical exercises designed for a Python developer role. Each exercise demonstrates different aspects of programming, database management, and API development. The tasks are divided into categories to maintain clarity and organization.

## Table of Contents
- [Python Exercises](#python-exercises)
- [Database Exercises](#database-exercises)
- [Service Setup with FastAPI](#service-setup-with-fastapi)
- [Airflow Task](#airflow-task)
- [Setup and Requirements](#setup-and-requirements)
- [How to Run](#how-to-run)

## Python Exercises
The `python_exercises/` folder contains solutions to Python programming tasks, focusing on data parsing, file handling, and dictionary manipulation.

### Task 1: JSON Parsing
- **Description**: A function that takes a JSON input, processes it, and returns a structured dictionary.
- **File**: `python_exercises/task1.py`
- **Usage**: Provides a sample JSON and outputs the structured data as specified.

## Database Exercises
The `database_exercises/` folder includes SQL tasks aimed at querying and organizing data from a sample customer database.

### Task 2: Customer and Employee Queries
- **Description**: SQL scripts that retrieve the highest-value customers and their assigned employees.
- **File**: `database_exercises/customer_queries.sql`
- **Usage**: Use an SQL editor or database tool to run these queries.

## Service Setup with FastAPI
The `service_setup/` folder contains a FastAPI application that demonstrates the basics of setting up API endpoints.

### Task 3: FastAPI Service
- **Description**: A basic FastAPI service that provides a greeting message and demonstrates different types of API services.
- **File**: `service_setup/main.py`
- **Usage**: Run with `uvicorn main:app --reload` to start the FastAPI server.

## Airflow Task
The `airflow/` folder contains documentation and scripts related to Airflow, including information on what Airflow is and its pros and cons.

### Task 4: Airflow Overview
- **Description**: A document detailing Airflow's use cases, benefits, drawbacks, and comparison with similar tools.
- **File**: `airflow/overview.md`

## Setup and Requirements
To set up the project, make sure you have Python 3.x and `pip` installed. If you are working with FastAPI, install the required packages with:
```bash
pip install -r requirements.txt
