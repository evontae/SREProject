Containerized System Monitoring Tool with Chaos Engineering
-----------------------------------------------------------

This project builds a containerized monitoring tool for IT infrastructure with a focus on system health, reliability testing, and DevOps best practices. It leverages Python, Docker, and potentially Ansible to collect and display real-time system metrics, introduce controlled failures for resilience testing, and streamline deployment.

Plan
----

-   **Containerization (Docker):** Package the monitoring script and its dependencies into a portable, easily deployable Docker container.
-   **Build a system monitoring tool (Python):**
    -   CPU Usage (overall and per-process)
    -   Memory Utilization (free, used, swap space)
    -   Disk Usage (available space, potential bottlenecks)
    -   Network Traffic (throughput, unusual spikes)
-   **Integrate Ansible:** Automate the setup and configuration of the monitoring application across multiple systems.
-   **Explore alerting:** Integrate a notification tool to alert on critical system conditions or anomalies.
-   **Introduce chaos engineering:**
    -   Stress test the system by simulating high loads and resource constraints.
    -   Induce false failures (disk full, unresponsive processes) to assess system robustness.
-   **Capture and redirect logs:** Collect comprehensive logs for analysis and debugging.
-   **(Optional) Move infrastructure to the cloud:** Evaluate and potentially migrate the monitoring solution to a cloud environment for scalability and reliability.

Technologies
------------

-   **Containerization:** Docker
-   **Configuration Management:** Ansible
-   **System Monitoring:** Python (`shutil`, `psutil`)
-   **Logging:** Python `logging` module
-   **Web Dashboard:** Python web framework (Flask, Django, or similar)
-   **Cloud Deployment:** Azure DevOps (Potential)
-   **Table Formatting Library:** Tabulate (or similar)

Project Roadmap:
----------------

-   **Phase 1: Initial Script and Containerization (Weeks 1-2):**
    -   Develop a Python script to collect basic system metrics (CPU, memory, disk, network).
    -   Create a Dockerfile to containerize the script and its dependencies.
    -   Test the containerized application on a local machine.
-   **Phase 2: Ansible Integration and Alerting (Weeks 3-4):**
    -   Write Ansible playbooks to automate the deployment and configuration of the monitoring container.
    -   Research and integrate a suitable alerting mechanism (e.g., email, Slack notifications) triggered by user-defined thresholds.
-   **Phase 3: Chaos Engineering and Reliability Testing (Weeks 5-6):**
    -   Develop scripts or tools to simulate various system failures and stressors.
    -   Conduct controlled chaos engineering experiments to assess system resilience.
    -   Refine the monitoring and alerting system based on findings from these experiments.
-   **Phase 4: Web Dashboard and Cloud Deployment (Optional, Weeks 7+):**
    -   Build a web-based dashboard using a Python web framework to visualize real-time system metrics.
    -   Evaluate the feasibility of migrating the entire solution to a cloud platform like Azure DevOps.

Design Process:
---------------

In designing this tool, I prioritized modularity and maintainability by creating separate functions for each resource type (CPU, memory, disk, network). This made the code easier to understand, test, and modify. I chose `psutil` for its comprehensive system information retrieval capabilities and cross-platform compatibility.

Robust error handling was crucial to ensure the script's reliability in diverse environments. I implemented `try-except` blocks in each function to catch potential errors such as permission issues or unexpected exceptions, allowing the script to recover gracefully and continue running.

For data storage, I chose dictionaries, as they provided a flexible and structured way to represent the collected metrics. Each resource type had its own dictionary, with keys representing specific metrics (e.g., "total," "used," "free") and their corresponding values.

Initially, I planned to have simple text output for the monitoring data. However, recognizing the potential value of visualizing this information in a more user-friendly way, I explored libraries like `tabulate` to format the data into tables. This is a stepping stone towards creating a web-based dashboard for real-time monitoring in the future.

Contributing
------------

Contributions are welcome! Feel free to open issues for bug reports or feature requests. If you'd like to contribute code, please fork the repository and submit a pull request.