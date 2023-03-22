# ChatGPT beyond 2021 🚀 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)

A minimalistic streamlt webapp using ChatGPT on steroids with google search capabilities since the model was trained with data till Sep 2021. 

![demo](https://user-images.githubusercontent.com/29462447/227014383-de92718a-faa2-4ee5-b3f2-f9484c226c26.gif)


## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. I am using Serper Free-Trial google search APIs. Navigate [here](https://serper.dev/) to create your account and save the API key as an environment variable in your system.
3. Similarly, navigate to the [OpenAI API section](https://platform.openai.com/) to create an account and generate your API key. Save this as well as another environment variable.
4. Simply run the command: 
```
streamlit run app.py
```
5. Navigate to http://localhost:8501 in your web-browser.

![demo](https://user-images.githubusercontent.com/29462447/227014431-fa62ae22-693d-4ff6-b4c5-319484fda118.png)


### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker 
