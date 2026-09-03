# ML DevOps Project 🚀

A machine learning prediction API built with Flask and deployed using Docker, GitHub Actions, and Render.

## 📌 Project Overview

This project demonstrates how a machine learning model can be developed, exposed through an API, containerized with Docker, automatically tested using CI, and deployed to the cloud.

The project uses the Iris dataset and a Decision Tree Classifier to make predictions.

## 🛠️ Technologies Used

- Python
- Scikit-learn
- Flask
- Joblib
- Pytest
- Docker
- Git & GitHub
- GitHub Actions
- Render

## 🏗️ Project Architecture

```text
                ┌─────────────────┐
                │   Iris Dataset  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   ML Training   │
                │    train.py     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    model.pkl    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Flask API     │
                │    app.py       │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     Docker      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ GitHub Actions  │
                │  Test + Build   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     Render      │
                │    Deployment   │
                └─────────────────┘

## 📁 Project Structure

```text
ml-devops-project/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── tests/
│   └── test_app.py
│
├── app.py
├── train.py
├── model.pkl
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md