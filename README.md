# Student Registry App

An introductory app for utilizing MySQL CRUD operations.

## Table of Contents

- [Student Registry App](#student-registry-app)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Getting Started

To get started, follow the instructions below.

### Prerequisites

- Python 3.10 & above
- MySQL Server

### Installation

1. Clone this repository to your local machine.

   ```bash
   git clone [repo-url]
   ```

1. Create virtual environment.
1. Install the necessary dependencies.

   ```bash
   pip install -r requirements.txt
   ```

1. Create an `.env` file containing the following:

    ```env
    DB_USER='[mysql-username]'
    DB_PASSWORD='[mysql-password]'
    ```

1. Execute the queries on the terminal.

    ```bash
    python create_db.py
    python create_table.py
    python insert_initial_data.py # optional
    ```

## Usage

To run the app, execute `python app.py` on the terminal.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository.
1. Create a new branch.
1. Make your changes and commit them.
1. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Thanks to [Python Foundation](https://www.python.org/) for the Python programming language.
