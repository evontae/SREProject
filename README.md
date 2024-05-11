Containerized System Monitoring Tool with Chaos Engineering
-----------------------------------------------------------

This project builds a containerized monitoring tool for IT infrastructure with a focus on system health, reliability testing, and DevOps best practices. It leverages Python, Docker, and potentially Ansible to collect and display real-time system metrics, introduce controlled failures for resilience testing, and streamline deployment.

Plan
----

-   **System Monitoring Script Development (Python):**

    -   Develop a robust Python script utilizing `psutil` and `shutil` to gather comprehensive system metrics:
        -   CPU usage (overall and per core)
        -   Memory utilization (total, available, used, swap)
        -   Disk usage and partitions (total, used, free space, percentage utilization)
        -   Network traffic (bytes sent/received, packets sent/received)
-   **Containerization (Docker):**

    -   Package the monitoring script and its dependencies into a Docker container for portability and ease of deployment.
    -   Configure the container to log system metrics to a centralized location (e.g., Azure Storage Account).
-   **Cloud Infrastructure Provisioning (Terraform):**

    -   Utilize Terraform to define and provision the required Azure cloud infrastructure:
        -   Azure Virtual Machines (or Azure Container Instances) to run the monitoring containers.
        -   Azure Storage Account to store logs and metrics.
        -   Azure Container Registry to store the Docker images.
        -   Networking components (Virtual Networks, Network Security Groups) for secure communication.
-   **Serverless Implementation (Azure Functions):**

    -   Refactor the Python script into individual Azure Functions, each responsible for collecting and processing a specific set of metrics.
    -   Leverage Azure Functions' scalability and event-driven capabilities to optimize resource usage and cost-efficiency.
-   **CI/CD Pipeline (Azure DevOps):**

    -   Establish a CI/CD pipeline using Azure DevOps to automate the building, testing, and deployment of the monitoring application.
    -   Integrate Terraform into the pipeline to manage infrastructure updates and ensure consistency across environments.
-   **Observability and Alerting (Azure Monitor):**

    -   Configure Azure Monitor to collect logs and metrics from the monitoring application and the underlying Azure infrastructure.
    -   Set up custom dashboards and alerts in Azure Monitor to gain insights into system health, performance, and potential issues.
-   **Chaos Engineering and Reliability Testing:**

    -   Introduce chaos engineering practices to proactively test the resilience and fault tolerance of your monitoring system.
    -   Utilize Azure Chaos Studio or other tools to simulate real-world failures and measure the impact on your application.
    -   Use the findings to identify vulnerabilities and strengthen your infrastructure and application.
-   **Web Dashboard (Flask/Django):**

    -   Develop a web-based dashboard using Flask or Django to visualize real-time and historical system metrics.
    -   Integrate the dashboard with Azure Monitor to provide a comprehensive view of your system's health and performance.
-   **Advanced Features (Optional):**

    -   Explore additional functionalities like autoscaling, cost optimization, and integration with other monitoring and alerting tools.
    -   Consider expanding the monitoring scope to include application-specific metrics and logs.

Technologies
------------

-   **Containerization:** Docker (for packaging and deployment)
-   **Cloud Infrastructure Provisioning:** Terraform (for managing Azure resources)
-   **Serverless Computing:** Azure Functions (for event-driven processing of metrics)
-   **CI/CD Pipeline:** Azure DevOps (for automating build, test, and deployment)
-   **System Monitoring:** Python with `psutil` (for collecting system metrics) and `shutil` (for disk usage)
-   **Observability:** Azure Monitor (for collecting logs and metrics, dashboards, and alerting)
-   **Chaos Engineering:** Azure Chaos Studio or similar tools (for resilience testing)
-   **Web Dashboard:** Flask or Django (for creating the web interface)
-   **Data Visualization:** Potentially libraries like `tabulate` (for tables), `plotly`, or `bokeh` (for interactive charts).
-   **(Optional) Configuration Management:** Ansible (for automating configuration and deployment if needed)

Project Roadmap:
----------------

-   **Phase 1: Initial Script and Containerization:**

    -   **Deliverable:** A working Python script that gathers system metrics (CPU, memory, disk, network) and outputs data in a structured format (JSON).
    -   **Deliverable:** A Dockerfile and a built Docker image containing the Python script and its dependencies.
    -   **Deliverable:** A set of unit tests to verify the script's core functionality within the Docker container.

-   **Phase 2: Cloud Infrastructure Provisioning with Terraform:**

    -   **Deliverable:** Terraform configuration files (`.tf`) defining the Azure resources (Azure Virtual Machine, Azure Storage Account for logs, Azure Container Registry).
    -   **Deliverable:** A successfully provisioned Azure environment with the resources defined in the Terraform files.
    -   **Deliverable:** A Terraform module for the monitoring infrastructure to ensure reusability and maintainability.

-   **Phase 3: Serverless Integration with Azure Functions:**

    -   **Deliverable:** Azure Functions replacing the original Python script, each handling a specific monitoring task.
    -   **Deliverable:** Function triggers (timer-based, HTTP-triggered) set to execute functions at intervals or on-demand.
    -   **Deliverable:** Azure Storage Queues or Tables storing collected metrics, enabling historical analysis and visualization.
    
-   **Phase 4: CI/CD Pipeline Implementation with Azure DevOps:**

    -   **Deliverable:** An Azure DevOps project with a CI/CD pipeline to automate builds, tests, and deployments.
    -   **Deliverable:** Pipeline stages for linting, unit testing, and integration testing to ensure code quality and reliability.
    -   **Deliverable:** Automated deployment of the containerized application to Azure using Terraform and Azure DevOps integration.
-   **Phase 5: Observability and Alerting with Azure Monitor:**

    -   **Deliverable:** Azure Monitor configuration to collect logs, metrics from the app, and infrastructure.
    -   **Deliverable:** Custom Azure dashboards visualizing system health, performance, and historical trends.
    -   **Deliverable:** Alerts and notifications (email, SMS, etc.) based on custom thresholds or anomaly detection in Azure Monitor.
-   **Phase 6: Chaos Engineering and Reliability Testing:**

    -   **Deliverable:** Chaos engineering experiments using Azure Chaos Studio or similar tools to simulate failures and assess resilience.
    -   **Deliverable:** Detailed report analyzing the experiment results, including identified weaknesses and recommendations for improvement.
-   **Phase 7: Web Dashboard and Advanced Features:**

    -   **Deliverable:** Interactive web dashboard using a Python framework (e.g., Flask, Django) hosted on Azure App Service, displaying real-time metrics.
    -   **Deliverable:** Integration with Azure Monitor to pull metrics and logs into the web dashboard for visualization.
    -   **Deliverable:** Implementation of autoscaling features based on system load or specific metrics (e.g., CPU usage) using Azure Virtual Machine Scale Sets.

Design Process:
---------------

In designing this tool, I prioritized modularity and maintainability by creating separate functions for each resource type (CPU, memory, disk, network). This made the code easier to understand, test, and modify. I chose `psutil` for its comprehensive system information retrieval capabilities and cross-platform compatibility.

Robust error handling was crucial to ensure the script's reliability in diverse environments. I implemented `try-except` blocks in each function to catch potential errors such as permission issues or unexpected exceptions, allowing the script to recover gracefully and continue running.

For data storage, I chose dictionaries, as they provided a flexible and structured way to represent the collected metrics. Each resource type had its own dictionary, with keys representing specific metrics (e.g., "total," "used," "free") and their corresponding values.

Initially, I planned to have simple text output for the monitoring data. However, recognizing the potential value of visualizing this information in a more user-friendly way, I explored libraries like `tabulate` to format the data into tables. This is a stepping stone towards creating a web-based dashboard for real-time monitoring in the future.

Contributing
------------

Contributions are welcome! Feel free to open issues for bug reports or feature requests. If you'd like to contribute code, please fork the repository and submit a pull request.