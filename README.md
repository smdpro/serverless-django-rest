# serverless-django-rest

# Django Restful API Challenge

Implement a simple Restful API on Django using the following tech stack: Python, Django Rest Framework, AWS DynamoDB


# How to run this project

### 1. Clone repository:
```bash
git clone https://github.com/smdpro/serverless-django-rest.git
cd serverless-django-rest
```

### 2. install requerments.txt
 
- install python 3.11 from [here](https://www.python.org/downloads/release/python-3103/)

On Linux
```bash
python -m venv .venv 
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

### 3. AWS Cli Configuration
- Download AWS Cli from [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and install it.

- on aws cli terminal:

```bash
aws configure
```

- Enter your IAM informations:

```bash
$ AWS Access Key ID [None]: ENTER YOUR ACCESSKEY
$ AWS Secret Access Key [None]: ENTER YOUR SECRETKEY
$ Default region name [None]: ENTER YOUR REGION
$ Default output format [None]: json
```

### 4. Aws DynamoDB

**You can Skip this section if the table already exists in dynmaoDB**

run docker container for dynamodb
```bash 
docker run -d -p 7000:8000 amazon/dynamodb-local
```

After entering the AWS Secret variables, we can use dynamodb migrator to create our nosql database.

```bash 
python local_maigration.py
```

After this, updating .env file.
```bash
IS_OFFLINE=True
REGIN_NAME=localhost
ENDPOINT_URL=http://localhost:7000
```

### 6. Run server locally :)
```bash
 python manage.py runserver
```



### 7. Deploy on AWS lambda


* install serverless:
```bash
npm install -g serverless

```

* install serverless packages from package.json
```bash
npm install
```

* deploy your Django project to AWS Lambda using Serverless
```bash
serverless deploy 
```




