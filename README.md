# **Zendesk Co-Op Challenge**

## To view the project - https://yash-zendesk-test.netlify.app/

### **Before you get started, install:**

```
pip install pytest
pip install pytest-mock
npm i -g serverless
```

# Backend architecure:

* 2 AWS Lambda Functions:
  *  Wrapper for the /get_tickets Zendesk API call to get all of the tickets on a page.
  *  Wrapper for the /get_ticket_by_id Zendesk API call to get single ticket details.

- Deployed to the AWS API Gateway
- All logs get displayed in CloudWatch
- No persistance

### To run the tests run:
```
pytest <test_file.py>
```

### To deploy the backend (You will need AWS configured), run:
```
serverless deploy
```

# Frontend architecture:

- React app
  - Deployed with Netlify

### To run the frontend locally, run:
```
npm start
```



