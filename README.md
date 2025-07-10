# Enterprise-Level Plotly Dash App Template

## Newsletter
👉🏽 Do you enjoy our content and want to read super-detailed articles about AI? If so, subscribe to our [Tinz Twins Hub](https://tinztwinshub.com/blog/) and get our popular data science cheat sheets for FREE.

## General
This project contains a well structured dashboard application with Plotly Dash. Feel free to use this example as the basis for your next Web App.

## Local Development
* Create and activate a conda environment: 
    * `conda create -n dash-app python=3.9.12`
    * `conda activate dash-app`
* Please install the dependencies with the following command: `poetry install`
* Navigate to the dash-app folder. Execute the following command: `python index.py`
* Open the app at http://127.0.0.1:7000

## Dockerize the Dash App (Production Environment)
* Build the app with the following command: `docker build -t dash-app:latest .`
* Run the app with the following command: `docker run --name dashboard -d -p 7000:7000 dash-app`
* Open the app at http://0.0.0.0:7000.

## Detailed tutorial
* [Tutorial](/tutorial/)

## Support this project
👉🏽 [Support our work](https://digitalproducts.tinztwinshub.com/l/plotly-dash-template)

## Follow us for more content
* [X](https://x.com/tinztwins)
* [Tinz Twins Hub](https://tinztwinshub.com)

⭐️ Star the repo if you find it useful!