# **Zendesk Co-Op Challenge**

## Install this before you get started

```
pip install pytest
pip install pytest-mock
npm i -g serverless
```

## To run the tests run:
```
pytest <test_file.py>
```


## To deploy the backend, run:
```
serverless deploy
```
## To run the frontend locally, run:
```
npm start
```
# Frontend architecture:

- React app
  - Deployed with Netlify

# Backend architecure:

* ## 2 AWS Lambda Functions:
  * ### Wrapper for the /get_tickets Zendesk API call.
  * ### Wrapper for the /get_ticket_by_id Zendesk API call.

### Deployed to the AWS API Gateway
### All logs get diaplyed in CloudWatch
### No persistance