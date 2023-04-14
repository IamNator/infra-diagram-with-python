from os import environ
from diagrams import Diagram, Cluster, Edge
from diagrams.saas.cdn import Cloudflare
from diagrams.onprem.client import User
from diagrams.aws.network import ELB
from diagrams.onprem.network import Nginx
from diagrams.onprem.aggregator import Fluentd
from diagrams.elastic.elasticsearch import Elasticsearch
from diagrams.programming.framework import React
from diagrams.onprem.database import Mongodb
from diagrams.aws.storage import SimpleStorageServiceS3BucketWithObjects
from diagrams.programming.language import Go as Golang, Javascript, Typescript


def create_cloud_infrastructure_diagram(company_name = ""):
    """
    Creates a diagram of the cloud infrastructure for the web application.
    """

    with Diagram(company_name + " Cloud Infrastructure",
                filename="infrastructure_diagram",
                show=False,
                direction="LR",
                outformat="png"
                ):

        with Cluster("EKS Cluster", graph_attr={
            # "pad": "6.0",
            "center": "true"
        }):
            
            with Cluster("Controller",graph_attr = {
                "bgcolor": "transparent",
            }):
                ingress_controller = Nginx("Ingress \nController")

            with Cluster("Frontend App",graph_attr = {
                "bgcolor": "transparent",
                "fontcolor": "bold",
            }):
                frontend_service = React("Frontend App")
        
            with Cluster("Backend \nAPI Services",graph_attr = {
                "bgcolor": "transparent",
                "fontcolor": "bold", 
            }):
                api_gateway = Typescript("API \nGateway") 

            
                with Cluster(label="Microservices", graph_attr = {
                    "bgcolor": "transparent",
                    "style": "invis",
                }):
                    microservices = [
                        Typescript("Auth API\nService"),
                        Golang("Company API\nService"),
                        Javascript("Notification API\nService")
                    ]


            with Cluster(label="Metrics \nCollection", graph_attr = {
                "bgcolor": "transparent",
                "fontcolor": "bold",
                "comment": "Responsible for logging collection and parsing"
            }):
                aggregator = Fluentd("Fluentd\n(Logging)")
                
        with Cluster("External", graph_attr = {
                "bgcolor": "transparent",
                "fontcolor": "invis",
            }):
            
            with Cluster("Database", graph_attr = {
                "bgcolor": "transparent",
            }):
                mongo_db = Mongodb("MongoDB")
            
            elasticsearch = Elasticsearch("Elasticsearch")
            s3_bucket = SimpleStorageServiceS3BucketWithObjects("S3 Bucket")
        

        # CONNECTIONS
            
        __ingres_color__ = "darkgreen"
        __api_gate_conn__ = "darkblue"
        __metrics__ = "darkorange"
        __database__ = "darkblue"
                    
        load_balancer = ELB("Load Balancer")

        User("End User") >> Cloudflare("Cloudflare") >> load_balancer

        load_balancer \
            >> Edge(color=__ingres_color__, style="bold") \
            >>  ingress_controller

        ingress_controller \
            >> Edge(color=__ingres_color__, style="bold") \
            >> frontend_service
        
        frontend_service \
            >> Edge(color=__metrics__,style="dashed") \
            >> aggregator
        
        ingress_controller \
            >> Edge(color=__ingres_color__, style="bold") \
            >> api_gateway
        
        api_gateway \
            >> Edge(color=__metrics__,style="dashed") \
            >> aggregator

        api_gateway \
            >> Edge(color=__api_gate_conn__, label="REST") \
            >> microservices
        
        microservices \
            >> Edge(color=__metrics__,style="dashed") \
            >> aggregator
        
        microservices \
            >> Edge(color=__database__, style="dashed") \
            >> mongo_db

        aggregator \
            >> elasticsearch

        aggregator \
            >> s3_bucket

        
company_name = environ.get("COMPANY_NAME")
create_cloud_infrastructure_diagram(company_name=company_name)