import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/Aman-Husain-123/mlops-mini-project.mlflow')
dagshub.init(repo_owner='Aman-Husain-123', repo_name='mlops-mini-project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)