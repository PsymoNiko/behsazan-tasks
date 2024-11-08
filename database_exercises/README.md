# Database Exercise

![alt text](database_exercises.png)
## Overview

This exercise involves querying a database to answer specific questions based on existing tables. The goal is to extract meaningful information regarding customers and their requests.

## Tables
- **Customers**: Contains information about customers.
- **Requests**: Contains details about requests made by customers.

## Objectives
1. Identify the customer with the highest number of requests.
2. Retrieve the details of the requests made by this customer.

## Instructions
1. **Identify the Customer**:
   - Write a SQL query to find the customer who has made the most requests.
   - Ensure to count the number of requests associated with each customer.

2. **Retrieve Requests**:
   - Once the customer is identified, write another SQL query to fetch all requests made by this customer.
   - Format the output in a clear and organized manner.

## Example SQL Queries

### Step 1: Identify the Customer with the Most Requests
```sql
SELECT customer_id, COUNT(request_id) AS request_count
FROM Requests
GROUP BY customer_id
ORDER BY request_count DESC
LIMIT 1;
```

### Step 2: Retrieve Requests for the Identified Customer
Assuming the customer ID obtained from the first query is `X`:
```sql
SELECT *
FROM Requests
WHERE customer_id = X;
```

## Output Format
- The output should be presented in a structured format, showing all relevant details of the requests made by the identified customer.

## Conclusion
By following the above steps, you will be able to extract the necessary information from the database regarding the customer with the highest number of requests and their corresponding details.