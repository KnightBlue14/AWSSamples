This is a simple use of lambda to stop and start ec2 instances on a schedule. 

First, you will need to set up an IAM role, allowing lambda to interact with EC2 instances. You will also need to enable acces to Cloudwatch for logging purposes. The sample is in role.json

In the lambda console, set up two functions using the files in this folder. From there, navigate to the Scheduler console, enter your name and description, and select 'recurring schedule'. In case you are not familiar with cron format -

0/x means a regular interval of x length, starting from the beginning. For instance, if I type 0/15 in the minutes box, this will be read as triggering the schedule every 15 minutes, starting from the hour. Typing * in every other box (except for Day of the week, which will fill on it's own) will mean that only the minute box is counted.
However, if I then type 0/2 in the hours box, this will then trigger the schedule in 15 minute intervals, but only within every 2nd hour. If you're only interested in running your script between business hours, these options won't mean a lot, but it does allow a great deal of control over when it will be run.
