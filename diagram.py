from diagrams import Diagram, Cluster
from diagrams.aws.compute import EKS
from diagrams.onprem.client import User
from diagrams.aws.network import ELB
from diagrams.aws.database import ElasticacheForRedis as Redis
from diagrams.programming.language import Go as Golang, Typescript

with Diagram("EKS Architecture", show=False):

    with Cluster("Backend API service"):
        api_gateway = Typescript("API Gateway")
        golang_services = [
            Golang("Service 1"),
            Golang("Service 2"),
            Golang("Service 3")
        ]

    typescript_app = Typescript("Frontend App")

    User("End User") >> ELB("Load Balancer") >> typescript_app >> api_gateway >> golang_services 

