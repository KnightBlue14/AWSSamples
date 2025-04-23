A sample of files I have used in an airflow instance, hosted on an EC2 instance.

Startup and utilhealth are bash files that run automatically once the instanc eis turned on, startup activationg the airflow webserver and scheduler, while utilhealth and health_check.py were set up to solve a peculiar issue.

I found initially that while the scheduler would run a DAG once, it would then not run that file later on. I suspect that it was due to me using a smaller instance with fewer cores and memory, but upgrading to a larger one would incur a higher cost, so I opted to set up a script to restart it automatically. In the airflow config, you can set up a healthcheck api, which can in turn be monitored externally. health_check.py simply checks the status reported on the . If it is healthy, then nothing is done. Otherwise, it restarts the scheduler.

As for the DAGs, these are two different ways to load data from the OpenWeather API. csv_dag ouputs the data to a csv stored in an S3 bucket, while pull_dag stores it in an RDBS instance. I would personally recommend an S3 bucket, as it does not incur a cost and simple operations can still be run on the data, but it is still useful to have a working example of the latter.

More details of what the files do can be found in my earlier repo -
```
https://github.com/KnightBlue14/Weather_monitoring
```
These files are currently set to monitor Leeds, but they can easily be changed by moviing the code block into a for loop