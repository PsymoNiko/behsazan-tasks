import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for the request
url = "https://tryit.w3schools.com/trysql_view.asp?x=0.29899936982264197"

# Customer IDs of the top 5 customers
top_customer_ids = [20, 63, 71, 65, 37]  # Replace these with the actual CustomerIDs you retrieved from the initial query

# Headers for the HTTP request
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.w3schools.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.w3schools.com/',
    'Cookie': '<YOUR_COOKIE_HERE>',  # Replace with the actual cookie value
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Priority': 'u=4'
}

# Initialize an empty DataFrame to collect data for all customers
all_customers_data = pd.DataFrame(columns=['customer', 'employee_list'])

# Loop over each CustomerID and perform the request
for customer_id in top_customer_ids:
    # Update the payload with the current CustomerID
    payload = f'code=SELECT+Customers.CustomerID%2C+Customers.CustomerName%2C+Employees.EmployeeID%2C+Employees.LastName%2C+Employees.FirstName+FROM+%28Customers+INNER+JOIN+Orders+ON+Customers.CustomerID+%3D+Orders.CustomerID%29+INNER+JOIN+Employees+ON+Orders.EmployeeID+%3D+Employees.EmployeeID+WHERE+Customers.CustomerID+%3D+{customer_id}%3B&bt=1'
    
    # Send the request
    response = requests.post(url, headers=headers, data=payload)
    
    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')  # Find the first table in the HTML response

    # Check if table exists in the response
    if table:
        # Extract table headers
        table_headers = [th.text.strip() for th in table.find_all('th')]
        
        # Extract table data rows
        rows = []
        for tr in table.find_all('tr')[1:]:  # Skip header row
            cells = [td.text.strip() for td in tr.find_all('td')]
            rows.append(cells)
        
        # Create DataFrame from the parsed data
        df = pd.DataFrame(rows, columns=table_headers)

        # Group employees by customer and create a list of employee names for each customer
        df['EmployeeName'] = df['FirstName'] + " " + df['LastName']
        customer_employee_df = df.groupby(['CustomerName'])['EmployeeName'].apply(lambda x: ', '.join(x)).reset_index()
        
        # Rename columns to match the required format
        customer_employee_df.columns = ['customer', 'employee_list']
        
        # Append to the master DataFrame
        all_customers_data = pd.concat([all_customers_data, customer_employee_df], ignore_index=True)
    else:
        print(f"No data found for CustomerID: {customer_id}")

# Save the final DataFrame to Excel
all_customers_data.to_excel("customer_employee_list234.xlsx", index=False)
print("Excel file 'customer_employee_list.xlsx' created successfully!")


