from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.onprem.client import User
from diagrams.aws.network import ELB
from diagrams.aws.database import ElasticacheForRedis as Redis
# from diagrams.programming.language import Go

with Diagram("X Architecture", show=False):

    with Cluster("Backend API service"):
        api_srv = [
            EC2("Instance 1"),
            EC2("Instance 2"),
            EC2("Instance 3")
        ]

    notification_srv = EC2("Notification Service")

    queue = Redis("Redis Server")



    User("Front End") >> ELB("load balancer") >> api_srv >> queue >> notification_srv
