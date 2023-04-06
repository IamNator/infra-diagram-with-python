from diagrams import Diagram, Cluster
from diagrams.aws.compute import EKS
from diagrams.onprem.client import User
from diagrams.aws.network import ELB
from diagrams.k8s.network import Ing as IngressController
from diagrams.programming.language import Go as Golang, Typescript

with Diagram("EKS Architecture", show=False):

    with Cluster("Backend API service"):

        ingress_controller = IngressController("Ingress Controller")

        api_gateway = Typescript("API Gateway")

        golang_services = [
            Golang("Auth Service"),
            Golang("Company Service"),
            Golang("Notification Service")
        ]
        

    typescript_app = Typescript("Frontend App")

    User("End User") >> ELB("Load Balancer") >> typescript_app >> api_gateway >> golang_services 

