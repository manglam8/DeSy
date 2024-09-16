# Real-Time Network Traffic Monitoring with Machine Learning

This project provides a real-time network traffic monitoring tool that captures live network packets and classifies them using a pre-trained machine learning model. The model is trained on the NSL-KDD dataset to detect anomalies and categorize network traffic.

The project leverages **Scapy** for network traffic capture and **scikit-learn** for classification using a **Random Forest** model. The application is designed to run in real-time and logs network traffic, extracting features that match the NSL-KDD dataset for classification.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [Remarks](#remarks)

## Project Overview

This tool captures live network traffic and classifies it in real-time based on a machine learning model trained using the NSL-KDD dataset. It allows users to:
- Monitor live network traffic.
- Extract network traffic features.
- Apply a Random Forest classifier to detect anomalies or categorize the network flow.

The project is developed with:
- **Python 3.11**
- **Scapy** for packet sniffing
- **scikit-learn** for applying machine learning models

The tool also logs traffic in both `.txt` and `.pcap` formats for detailed analysis.

## Features
- Real-time network traffic monitoring using **Scapy**.
- Classification of network packets based on a pre-trained **Random Forest** model.
- Support for both IPv4 and IPv6 packet captures.
- Feature extraction based on NSL-KDD dataset fields.
- Logs network traffic in `.txt` and `.pcap` formats.

## Prerequisites

Before setting up the project, ensure you have the following installed on your system:

1. **Python 3.11 or higher**: The project is tested with Python 3.11.
2. **Scapy**: A powerful Python library used for packet capture.
3. **scikit-learn**: For using the pre-trained machine learning model.
4. **Admin privileges**: Required to run packet sniffing, as it interacts with the network interfaces.

To install the required Python libraries, run:
```bash
pip install -r requirements.txt
```

## Installation

### Clone the Repository

First, clone the repository to your local system:

```bash
git clone https://github.com/manglam8/DeSy.git
cd DeSy
```

### Install Dependencies

Install the necessary Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Run with Elevated Privileges (Ongoing development)

Packet sniffing requires elevated permissions. Run the Python script with `sudo`:

```bash
sudo python3 src/real_time_monitoring.py
```

## Usage

### Capture and Classify Packets (Ongoing development)

Run the monitoring tool to capture live traffic and classify packets in real-time. The captured traffic is logged in both `.txt` and `.pcap` formats.

```bash
sudo python3 src/real_time_monitoring.py
```

You shall review the traffic logs after the monitoring session is complete.

### Accuracy of Model

On running the train_model.py we see following output:

```
Accuracy: 0.9871377882909521
Classification Report:
               precision    recall  f1-score   support

           0       0.98      0.99      0.99      2922
           1       0.99      0.99      0.99      3842

    accuracy                           0.99      6764
   macro avg       0.99      0.99      0.99      6764
weighted avg       0.99      0.99      0.99      6764

Model saved at models/ml_model.pkl
```

### Packet Logs

- **Text Logs**: Logged in a human-readable `.txt` format.
- **PCAP Files**: Captured network traffic is stored in `.pcap` format for detailed analysis using tools like Wireshark.

## Dataset

The machine learning model used in this project is trained on the **NSL-KDD dataset**, a popular dataset for network intrusion detection. You can find the dataset [here](https://www.kaggle.com/datasets/hassan06/nslkdd).

To re-train the model or modify it, download the dataset and follow the instructions in the `model_training` directory.

## File Structure

```
DeSy/
│
├── data/                            # Directory to store datasets
│   ├── NSL-KDD-Dataset.csv          # Downloaded dataset
│
├── models/                          # Directory to save trained models
│   └── ml_model.pkl                 # Saved machine learning model
│
├── src/                             # Source directory for all scripts
│   ├── data_preprocessing.py        # Data preprocessing and feature engineering
│   ├── train_model.py               # Model training and evaluation script
│   ├── real_time_monitoring.py      # Script for real-time network monitoring
│   ├── utils.py                     # Utility functions for data processing
│
├── app/                             # Flask or Streamlit app for dashboard
│   ├── dashboard.py                 # Web interface for IDS alerts and logs
│
├── logs/                            # Directory for storing log files
│   └── ids_log.txt                  # Log file for intrusion alerts
│
├── README.md                        # Project documentation
├── requirements.txt                 # List of dependencies (libraries)
└── config.yaml                      # Configuration file for paths, parameters, etc.
```

## Contributing

Contributions are welcome! Please fork this repository, create a new branch, and submit a pull request with your changes.

### To contribute:
1. Fork the project
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request

## Remarks

This project is for educational purpose solely.
