# Inventory Management System

A Django REST API for managing inventory items with PDF and Excel export capabilities.

## Features

- Complete CRUD operations for inventory items
- Filter items by quantity and price range
- Pagination support
- Export data to PDF and Excel formats
- RESTful API design

## Technologies Used

- Python 
- Django 
- Django REST Framework
- ReportLab (PDF generation)
- OpenPyXL (Excel generation)
- Django Filter
- SQLite (Database)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/nikhil-sutar/DataWeaver.git
cd core
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

## How to Run the Server
```bash
python manage.py runserver
```

## How to Test APIs

### Using Postman

1. Import the included `Inventory_APIs.postman_collection.json` file
2. Select an endpoint and click "Send"
3. View the response

## Filtering Examples

**Filter by Quantity Range:**
```
GET /api/items/?quantity__gte=5&quantity__lte=50
```

**Filter by Price Range:**
```
GET /api/items/?price__gte=100&price__lte=2000
```

**Combine Filters:**
```
GET /api/items/?quantity__gte=10&price__lte=1000
```

## How to Generate PDF and Excel

### PDF Export

**Using Browser:**
```
http://localhost:8000/api/items/export/pdf/
```
File will download automatically as `items_report.pdf`

**Using Postman:**
1. Send GET request to `/api/items/export/pdf/`
2. Click "Save respose to file"
3. Save the PDF file

### Excel Export

**Using Browser:**
```
http://localhost:8000/api/items/export/excel/
```
File will download automatically as `items_report.xlsx`

**Using Postman:**
1. Send GET request to `/api/items/export/excel/`
2. Click "Save respose to file"
3. Save the Excel file

### Export with Filters

You can apply filters to exports:
```
GET /api/items/export/pdf/?quantity__gte=10
GET /api/items/export/excel/?price__lte=1000
```