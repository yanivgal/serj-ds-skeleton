# Serj DS Skeleton
This repository provides a basic skeleton for data science projects, inspired by Serj's approach to organizing and running professional data science workflows.

## Features
- A modular and reusable structure for data science projects.
- Promotes collaboration, reproducibility, and maintainability.
- Includes placeholders for preprocessing, training, prediction, and result analysis scripts.
- Easily customizable for various project needs.

## Project Structure

The template generates the following structure:

- `app/`: Helper scripts and utilities.
- `models/`: Trained models for the current experiment.
- `archived_experiments/`: Archived experiments and their outputs.
- `data/`: Input datasets and preprocessed data.
- `results/`: Outputs like predictions, charts, and analysis results.
- `notebooks/`: Jupyter notebooks for exploration and experimentation.
- `tests/`: Unit tests to ensure code quality.

Core scripts include:
- `preprocess.py`: Handles data preprocessing tasks.
- `train.py`: A script to train machine learning models.
- `predict.py`: Generates predictions using trained models.
- `result.py`: Analyzes results and generates metrics/charts.
- `tasks.py`: Automates workflows using `invoke`.

## Usage

1. Install Cookiecutter (if not already installed):
```bash
pip install cookiecutter
```

1. Use the Template
```bash
cookiecutter https://github.com/yanivgal/serj-ds-skeleton
```

## Why This Exists
Inspired by Serj's practical lessons, this project aims to make it easier for data scientists to focus on their work without worrying about project setup.

Feel free to contribute or share feedback!
