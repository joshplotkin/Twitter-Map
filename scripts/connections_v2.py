import pymysql
import boto.sqs
import boto.sns

aws_region = "xxxx"
aws_access_key = 'xxxx'
aws_secret_key = 'xxxx'

def connect_to_sqs(queue_name):
	# Credentials for creating SQS Queue
	# sqs queue is changed to Divyansh's Queue credentials.
	conn_sqs = boto.sqs.connect_to_region( aws_region,
			aws_access_key_id=aws_access_key,
			aws_secret_access_key=aws_secret_key);
	#	aws_access_key_id=aws_access_key,
	#	aws_secret_access_key=aws_secret_key);

	#Connect to SQS Queue 
	sqs_queue = conn_sqs.get_queue(queue_name)
	sqs_queue = conn_sqs.create_queue('TwitterMap_gp_1')
	return sqs_queue


def connect_to_mysql():
	#database credentials
	host_name='xxxx'
	port_num=3306
	user_name='xxxx'
	password='xxxx' 
	database='tweets'
	charset = 'utf8'

	conn = pymysql.connect(host=host_name,
	                       port=port_num, user=user_name,
	                       passwd=password, 
	                       db=database,
	                       charset = charset);
	cur = conn.cursor();
	return conn,cur

def connect_to_sns():
	conn_sns = boto.sns.connect_to_region( aws_region, aws_access_key_id=aws_access_key, \
				aws_secret_access_key=aws_secret_key);

	#create a sns topic
	topic_name = 'test_topic1'
#	sns_topic = conn_sns.create_topic(topic_name)

	topic_arn = 'arn:aws:sns:us-east-1:900440526214:test_topic1'
	endpoint = 'http://ec2-54-174-83-22.compute-1.amazonaws.com:3000/sns'
	protocol = 'http'
#	conn_sns.subscribe(topic_arn,protocol,endpoint)
#	msg = 'sns publish message test 2'
#	conn_sns.publish(topic=topic_arn, message=msg)
	return conn_sns,topic_arn
