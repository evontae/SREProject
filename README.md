SREProject
==========

This project builds a containerized monitoring tool for IT infrastructure with a focus on system health, reliability testing, and DevOps best practices.

Plan
----

-   Build a system monitoring tool starting out with a small script utilizing Python to collect/monitor
    -   CPU Usage (overall and per-process)
    -   Memory Utilization (free, used, swap space)
    -   Disk Usage (available space, potential bottlenecks)
    -   Network Traffic (throughput, unusual spikes)
-   Containerize the script using Docker and deploy to a Raspberry Pi
-   Integrate Ansible to automate the setup and configuration of the monitoring application
-   Explore alerting by integrating a suitable notification tool
-   Introduce chaos engineering through reliability testing with "fake attacks"
    -   Stress test the system by introducing high loads
    -   Induce false failures (disk full, unresponsive processes) to test robustness
-   Capture logs and redirect outputs
-   (Optional) Move infrastructure to the cloud

Technologies
------------

-   **Containerization:** Docker
-   **Configuration Management:** Ansible
-   **System Monitoring:** Python (`glances`, `psutil`)
-   **Logging:** Python `logging` module
-   **Cloud Deployment:** Azure DevOps (Potential)

Project Roadmap:
----------------

-   **Phase 1:**
    1.  **Monitoring Script (psutil):**
        -   Begin with a minimal script collecting basic system metrics.
        -   Focus on extracting the essential metrics (CPU, memory, disk, network).
        -   Implement simple output formatting for readability.
        -   Include basic error handling.
    2.  **Initial Docker Container:**
        -   Choose a lightweight Python base image (e.g., `python:alpine`)
        -   Create a Dockerfile to package the script and dependencies.
        -   Investigate how to direct the script's output to the container's logs (`stdout`).
    3.  **Structured Logging:**
        -   Research how to integrate structured logging (e.g., JSON format) using Python's `logging` module.
    4.  **Customizable Thresholds:**
        -   Allow for some basic configuration of warning thresholds (e.g., get a notification when disk space usage exceeds 80%) through a simple config file or command-line arguments.

Learning Log:
-------------

Contributing
------------

-   If you're open to others collaborating later, a brief note on how people can contribute is helpful*