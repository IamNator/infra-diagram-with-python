from diagrams import Diagram, Cluster
from diagrams.aws.compute import EKS
from diagrams.onprem.client import User
from diagrams.aws.network import ELB
from diagrams.k8s.network import Ing as IngressController
from diagrams.programming.language import Go as Golang, Typescript

with Diagram("EKS Architecture", show=False):

    with Cluster("Backend API service"):

        ingress_controller = IngressController("Ingress Controller")

        frontend_service = Typescript("Frontend App")

        api_gateway = Typescript("API Gateway")

        golang_services = [
            Golang("Auth Service"),
            Golang("Company Service"),
            Golang("Notification Service")
        ]

        
    User("End User") >> ELB("Load Balancer") >> ingress_controller
    
    ingress_controller >>  frontend_service >> api_gateway >> golang_services 

