# Weather Prediction using Gaussian Naive Bayes

## Overview

This project implements a weather prediction model using the Gaussian Naive Bayes classification algorithm. The model predicts whether it will rain the next day based on four weather parameters: temperature, humidity, wind speed, and atmospheric pressure.

## Features

* Loads weather data from a CSV file
* Splits the dataset into training and testing sets
* Trains a Gaussian Naive Bayes classifier
* Evaluates the model using:

  * Accuracy Score
  * Classification Report
  * Confusion Matrix
* Predicts rainfall for new weather data

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Anaconda

## Requirements

* Anaconda
* Python 3.x
* Pandas
* Scikit-learn

## Dataset

The dataset consists of the following attributes:

| Feature      | Description                             |
| ------------ | --------------------------------------- |
| Temperature  | Temperature (°C)                        |
| Humidity     | Humidity (%)                            |
| WindSpeed    | Wind Speed (km/h)                       |
| Pressure     | Atmospheric Pressure (hPa)              |
| RainTomorrow | Target variable (0 = No Rain, 1 = Rain) |

## Project Structure

```text
weather_prediction/
│── weather_prediction.py
│── weather_prediction_dataset.csv
└── README.md
```

## How to Run

1. Open Anaconda Prompt.
2. Navigate to the project directory.
3. Run the following command:

```bash
python weather_prediction.py
```

## Output

The program displays:

* Dataset preview
* Accuracy Score
* Classification Report
* Confusion Matrix
* Prediction for a new weather sample

## Sample Input

| Temperature | Humidity | WindSpeed | Pressure |
| ----------- | -------: | --------: | -------: |
| 25          |       60 |        24 |      991 |

## Sample Output

```text
Prediction: Rain Expected Tomorrow
```

or

```text
Prediction: No Rain Tomorrow
```
