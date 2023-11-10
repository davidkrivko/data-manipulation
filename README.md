# Data Management Service

This service is designed to work with a dataset provided in a .csv format, which includes the following fields: category, firstname, lastname, email, gender, birthDate. It allows reading the CSV file, writing the data to a database, and displaying the data with filters and pagination.

## Getting Started

### Prerequisites

- Docker
- GitHub account
- Python 3+

## Installation

1. Clone the repository to your local machine using GitLab's repository URL:

```
git clone https://github.com/davidkrivko/data-manipulation.git
```

2. Navigate to the cloned directory:

```
cd <repository-path>
```

3. Create ENV file as .env.example

```
cp .env.example .env
```

4. Running the Service

To run the service in a Docker container, execute the following command:

```
docker-compose up --build
```

This command will build the Docker image and start the service.

5. Run migrations

```
python manage.py migrate
```

6. Import data from file

```
python manage.py import_data
```

## Usage

Once the service is up and running, you can access the data management interface through your web browser.

- To view data with pagination:
```
http://localhost:8000/api/users/
```

- To apply filters, use query parameters like so:
```
category=<category>
gender=<gender>
birthDate=<YYYY-MM-DD>
age=<age>
ageRange=<startAge>-<endAge>
```

- To export filtered data as a CSV file manually:
```
http://localhost:8000/api/export_csv/?<params>
```

- To export filtered data as a CSV file on email via Celery:
```
http://localhost:8000/api/export_csv/email/?<params>
```


- Also you can manage favorite users categories
```
http://localhost:8000/api/categories/
```


## Thank you)
