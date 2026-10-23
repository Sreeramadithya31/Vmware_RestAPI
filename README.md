**VMware Workstation REST API – Virtual Machine Management System**

Developed a RESTful API using **Python and FastAPI** to manage and automate virtual machines running on VMware Workstation. The system integrates VMware's `vmrun` command-line utility to perform virtual machine operations through HTTP endpoints, simplifying VM management without requiring manual interaction with the VMware graphical interface.

The project supports virtual machine lifecycle management, including starting, stopping, suspending, and resetting virtual machines. It also provides endpoints for checking VM status, listing available virtual machines, and retrieving host network information. FastAPI's automatic Swagger UI documentation enables users to test API endpoints interactively.

**Technologies Used:** Python, FastAPI, Uvicorn, VMware Workstation, Ubuntu Linux, REST API, `vmrun.exe`, subprocess, Pydantic, and Swagger UI.

**Key Features:**
- REST API endpoints for virtual machine lifecycle operations.
- VM status monitoring and virtual machine listing.
- Integration with VMware Workstation using `vmrun.exe`.
- Host network information retrieval.
- Input validation, error handling, and JSON responses.
- Interactive API documentation and testing through Swagger UI.

**Objective:** To demonstrate virtualization automation and backend API development by building a centralized interface for controlling VMware virtual machines programmatically.
