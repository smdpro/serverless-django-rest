# serverless-django-rest

Implement a simple Restful API on Django using the following tech stack: Python, Django Rest Framework, AWS DynamoDB


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

### 3. Run Locally

run docker container for dynamodb
```bash 
docker run -d -p 7000:8000 amazon/dynamodb-local
```

run local migration for creating the table

```bash 
python local_maigration.py
```

After this, updating .env file.
```bash
IS_OFFLINE=True
REGIN_NAME=localhost
ENDPOINT_URL=http://localhost:7000
```
Run server
```bash
 python manage.py runserver
```

### 4. AWS Cli Configuration
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

### 5. Deploy on AWS lambda


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




