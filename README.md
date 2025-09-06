# AI Agents Team

AI consulting agency web card

## Setup

To run this project, you need to activate the virtual environment first.

### Windows

```bash
.\venv\Scripts\activate
```

### macOS & Linux

```bash
source venv/bin/activate
```

## Running the application

This project provides two ways to run the application:

### Development

To run the application in development mode, use the following command:

```bash
run-dev
```

This will start a Flask development server on `http://127.0.0.1:5000` with debugging and auto-reloading enabled.

### Production

To run the application in production mode, use the following command:

```bash
run-prod
```

This will start a production-ready Waitress server on `http://127.0.0.1:8080`.

## Deployment

### DigitalOcean App Platform

This application is ready to be deployed to DigitalOcean's App Platform. The platform will automatically detect the `requirements.txt`, `Procfile`, and `runtime.txt` to build and run the application.

The `runtime.txt` file specifies the Python version to be used.

1.  Create a new App on DigitalOcean.
2.  Connect your Git repository.
3.  The platform will automatically build and deploy the application.
