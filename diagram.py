from diagrams import Diagram, Cluster
from diagrams.aws.compute import EKS
from diagrams.onprem.client import User
from diagrams.aws.network import ELB
from diagrams.k8s.network import Ing as IngressController
from diagrams.programming.language import Go as Golang, Typescript

with Diagram("EKS Architecture", show=False):

    with Cluster("Backend API service"):
        api_gateway = Typescript("API Gateway")
        golang_services = [
            Golang("Auth Service"),
            Golang("Company Service"),
            Golang("Notification Service")
        ]
        
        ingress_controller = IngressController("Ingress Controller")

    typescript_app = Typescript("Frontend App")

    User("End User") >> ELB("Load Balancer") >> ingress_controller >> api_gateway >> golang_services 
    typescript_app >> api_gateway
