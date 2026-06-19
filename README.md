# Job Market Analytics System

## Overview

The Job Market Analytics System is an end-to-end data analytics project built using Python, MySQL, SQL, Pandas, and Streamlit.

The application scrapes job listings from a website, stores the data in a MySQL database, performs analytical queries, and displays insights through an interactive dashboard.

---

## Features

* Scrape job listings using BeautifulSoup
* Store scraped data in MySQL
* Perform SQL analytics on job data
* Interactive Streamlit dashboard
* Company and location filters
* KPI cards for quick insights
* Hiring trend visualizations
* Data exploration through tables and charts

---

## Tech Stack

* Python
* BeautifulSoup
* Requests
* Pandas
* MySQL
* SQL
* Streamlit

---

## Project Workflow

Website

↓

Python Web Scraper

↓

CSV Storage

↓

MySQL Database

↓

SQL Analytics

↓

Streamlit Dashboard

---

## Database Schema

Table: job_listings

| Column   | Type         |
| -------- | ------------ |
| id       | INT          |
| title    | VARCHAR(255) |
| company  | VARCHAR(255) |
| location | VARCHAR(255) |

---

## Key SQL Queries Used

### Total Jobs

SELECT COUNT(*) FROM job_listings;

### Top Companies

SELECT company, COUNT(*)
FROM job_listings
GROUP BY company
ORDER BY COUNT(*) DESC;

### Top Locations

SELECT location, COUNT(*)
FROM job_listings
GROUP BY location
ORDER BY COUNT(*) DESC;

---

## Dashboard Features

* Total Jobs KPI
* Total Companies KPI
* Total Locations KPI
* Company Filter
* Location Filter
* Top Companies Chart
* Top Locations Chart
* Job Listings Table

---

## Skills Demonstrated

* Web Scraping
* Data Collection
* Database Design
* SQL Querying
* Data Analysis
* Dashboard Development
* Data Visualization
* Problem Solving
* Python Programming

---

## Future Improvements

* Real-time job scraping
* Salary analysis
* Skill demand analysis
* Automated daily updates
* Cloud deployment

---

## Author

Bhoomika Grandhi
