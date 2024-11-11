# Producer-Consumer Example with Multithreading

This project demonstrates a basic producer-consumer pattern using Python’s `threading` module. The producer generates random integers and places them into a shared queue, while the consumer retrieves and processes these integers. The application is designed to run for a fixed duration with controlled production and consumption rates.

## Getting Started

### Prerequisites

- Python 3.7 or later
- Docker (optional, if you want to run the application in a container)

### Installation

#### Running Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/veo1/multithreading.git
   cd <multithreading>
    ```

2. **Set up a virtual environment (recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On macOS and Linux
    venv\Scripts\activate      # On Windows
    ```

3. **Running the application**:

To start the Flask API, run the following command:
    ```bash
    python multithreading.py
    ```

#### Using Docker

You can also run this application in a Docker container.
1. **Build the Docker image**:

    ```bash
    docker build -t multithreading .
    ```
2. **Run the Docker image**: 
    ```bash
     docker run --rm multithreading
    ```


### Using the Script

This script initiates two threads:
- **Producer Thread**: Generates a random integer every 0.1 seconds and attempts to place it into the shared queue.
- **Consumer Thread**: Consumes an integer from the queue every 0.15 seconds if available.

The program runs for 10 seconds, during which the producer and consumer operate in tandem, logging their actions to the console.


### Directory Structure
    ```
    ├── multithreading.py   # Main application file containing the producer and consumer functions
    ├── requirements.txt    # List of Python dependencies
    ├── Dockerfile          # Docker configuration file (optional)
    ├── README.md           # Documentation file
    └── multithreading.gif  # GIF of the application running
    ```

#### File Descriptions

- `multithreading.py`: Main Python script containing producer and consumer functions
- `requirements.txt`: List of Python dependencies (optional, currently empty)
- `Dockerfile`: Docker configuration file.
- `README.md`: Documentation file.
- `multithreading.gif`: GIF of the application running.