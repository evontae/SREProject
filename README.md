# Containerized System Monitoring Tool with Chaos Engineering

## Introduction
This project aims to develop a robust and scalable system monitoring tool designed with a strong SRE/DevOps emphasis. It leverages microservices architecture, containerization with Docker, orchestration with Kubernetes (and Helm), and potentially utilizes Azure cloud services for infrastructure provisioning, serverless functions, CI/CD pipelines, and observability.

The tool collects comprehensive system metrics (CPU, memory, disk, network) in real-time, providing insights into system health and performance. It is designed with reliability in mind, incorporating chaos engineering experiments to proactively identify and address vulnerabilities. Additionally, the project explores the potential of ML/AI for predictive analysis and anomaly detection to further enhance system reliability and security.

This project showcases a deep understanding of modern SRE/DevOps practices, including Infrastructure as Code (IaC) with Terraform, continuous integration and deployment (CI/CD) with Azure DevOps, and the effective use of cloud-native technologies like Kubernetes and Azure Functions. The end result is a powerful and customizable tool for monitoring and maintaining complex IT infrastructures.

## Key Improvements
- **Microservices Architecture:** Emphasizes modularity and scalability.
- **Helm:** Highlights the use of Helm for managing Kubernetes deployments.
- **Azure:** Clarifies the potential use of Azure cloud services for various aspects of the project.
- **Reliability and Chaos Engineering:** Focuses on building a reliable system and using chaos engineering techniques.
- **ML/AI:** Explores ML/AI for predictive analysis, demonstrating a forward-thinking approach.
- **SRE/DevOps Focus:** Reinforces the overall focus on SRE/DevOps principles and practices.

## Plan

1. **System Monitoring Microservices (Python):**
    - Develop independent Python microservices using `psutil` and `shutil` to collect:
        - CPU usage (overall and per core)
        - Memory utilization (total, available, used, swap)
        - Disk usage and partitions (total, used, free space, percentage utilization)
        - Network traffic (bytes sent/received, packets sent/received)
    - Expose metrics via RESTful APIs.
    - Implement structured logging in JSON format.

2. **Containerization and Orchestration (Docker & Kubernetes/Helm):**
    - Package each microservice into a Docker container.
    - Use Helm charts to define, install, and manage the microservices on Kubernetes.
    - Set up a local Kubernetes environment (Minikube or kind) for development and testing.

3. **CI/CD Pipeline (Azure DevOps):**
    - Create an Azure DevOps project and establish a CI/CD pipeline.
    - Automate building, testing, vulnerability scanning, and deploying Docker images to a container registry (e.g., Azure Container Registry).
    - Implement continuous deployment to a Kubernetes cluster (local or cloud-based).

4. **Cloud Infrastructure Provisioning (Terraform):**
    - Learn Terraform and create configuration files to provision the required Azure infrastructure:
        - Azure Kubernetes Service (AKS) cluster
        - Azure Container Registry
        - Azure Log Analytics Workspace (for centralized logging)
        - Networking components (Virtual Networks, Load Balancers)
        - Consider cost-effective options (e.g., Spot VMs, smaller node pools)

5. **Observability and Alerting (Azure Monitor & Prometheus/Grafana):**
    - Configure Azure Monitor for log aggregation and basic metrics collection.
    - Set up Prometheus to scrape metrics from microservices and Kubernetes.
    - Use Grafana to create custom dashboards visualizing metrics from Azure Monitor and Prometheus.
    - Implement alerts based on metric thresholds and anomaly detection (consider using ML-based models).

6. **Chaos Engineering (Azure Chaos Studio):**
    - Design and execute chaos experiments on the Azure infrastructure and microservices to test resilience.
    - Analyze results and iterate to improve system fault tolerance.

7. **(Optional) Predictive Analysis (ML/AI):**
    - Gather historical metric data.
    - Train ML models for anomaly detection or predictive scaling.
    - Integrate models into the monitoring tool.

## Technologies

- **Containerization:** Docker (for packaging and deployment)
- **Cloud Infrastructure Provisioning:** Terraform (for managing Azure resources)
- **Serverless Computing:** Azure Functions (for event-driven processing of metrics)
- **CI/CD Pipeline:** Azure DevOps (for automating build, test, and deployment)
- **System Monitoring:** Python with `psutil` (for collecting system metrics) and `shutil` (for disk usage)
- **Observability:** Azure Monitor (for collecting logs and metrics, dashboards, and alerting)
- **Chaos Engineering:** Azure Chaos Studio or similar tools (for resilience testing)
- **Web Dashboard:** Flask or Django (for creating the web interface)
- **Data Visualization:** Potentially libraries like `tabulate` (for tables), `plotly`, or `bokeh` (for interactive charts).
- **(Optional) Configuration Management:** Ansible (for automating configuration and deployment if needed)

## Project Roadmap

**Project Roadmap (Deliverable-Based):**

### Phase 1: Microservice Development and Local Deployment
- **Deliverable 1.1:** Refactored system monitoring Python script:
    - Break down `system_monitor.py` into independent microservices (CPU, memory, disk, network) with RESTful APIs.
    - Implement structured logging in JSON format within each microservice.
- **Deliverable 1.2:** Dockerized microservices:
    - Create optimized Dockerfiles for each microservice, minimizing image size.
    - Build and test Docker images locally.
- **Deliverable 1.3:** Comprehensive unit and integration tests:
    - Write and execute unit tests to verify individual microservice functionality.
    - Develop integration tests to ensure seamless interaction between microservices.
- **Deliverable 1.4:** Local Kubernetes deployment with Helm:
    - Set up a local Kubernetes environment (Minikube or kind).
    - Create Helm charts for each microservice.
    - Deploy microservices using Helm and test functionality within the local cluster.
    - Set up local log aggregation (e.g., Docker logging driver or sidecar container).
- **Deliverable 1.5:** Local monitoring with Prometheus and Grafana:
    - Install and configure Prometheus to scrape metrics from microservices.
    - Set up Grafana to visualize metrics and create custom dashboards.

### Phase 2: CI/CD Pipeline and Cloud Infrastructure
- **Deliverable 2.1:** Azure DevOps CI/CD pipeline:
    - Create a CI/CD pipeline to automate building, testing, and deployment.
    - Incorporate image vulnerability scanning.
- **Deliverable 2.2:** Terraform configuration for Azure infrastructure:
    - Define Azure resources (AKS, Container Registry, Log Analytics Workspace, etc.) using Terraform with cost optimization and security best practices.
- **Deliverable 2.3:** Automated deployment to Azure Kubernetes Service (AKS):
    - Use Terraform to provision the Azure infrastructure.
    - Configure the CI/CD pipeline to deploy Dockerized microservices to AKS.
    - Set up Azure Key Vault for secrets management.

### Phase 3: Azure Functions, Monitoring, and Alerting
- **Deliverable 3.1:** Azure Functions implementation:
    - Deploy each microservice as an Azure Function, optimizing performance and cost.
- **Deliverable 3.2:** Centralized Logging:
    - Configure Azure Log Analytics Workspace to collect and store logs from AKS cluster and Azure Functions.
- **Deliverable 3.3:** Observability with Azure Monitor and Prometheus/Grafana:
    - Collect metrics from Azure Functions and AKS cluster using Azure Monitor.
    - Integrate Prometheus with Azure Monitor for additional metrics collection.
    - Create custom dashboards in Grafana using data from both Azure Monitor and Prometheus.
- **Deliverable 3.4:** Alerting System:
    - Set up alerts in Azure Monitor based on metric thresholds and anomaly detection.

### Phase 4: Chaos Engineering and Reliability
- **Deliverable 4.1:** Chaos Experiment Design and Execution:
    - Design and execute chaos experiments using Azure Chaos Studio on Azure infrastructure and microservices.
- **Deliverable 4.2:** Resilience Analysis and Improvement:
    - Analyze experiment results, identify weaknesses, and implement improvements to enhance system resilience.

### Phase 5: Scaling, Optimization, and ML/AI (Optional)
- **Deliverable 5.1:** Scalability and Performance Assessment:
    - Conduct load testing on Azure infrastructure.
    - Implement horizontal pod autoscaling (HPA) in AKS.
    - Optimize microservices, Kubernetes configuration, and Azure infrastructure for performance and efficiency.
- **Deliverable 5.2 (Optional):** ML/AI Integration:
    - Train and integrate ML models for anomaly detection or predictive scaling.
    - Validate the effectiveness of the ML models in real-world scenarios.

## Contributing

Contributions are welcome! Feel free to open issues for bug reports or feature requests. If you'd like to contribute code, please fork the repository and submit a pull request.

- **Set Up Development Environment:** Instructions for setting up the environment.
- **Coding Standards:** Guidelines on code style and best practices.
- **Running Tests:** Instructions for running unit and integration tests.
