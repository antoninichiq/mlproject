# End to End Machine Learning Project

### Student Performance Prediction
This project focuses on predicting student performance in math exams based on various demographic and academic factors. It employs a machine learning approach, leveraging historical student data to build and train a predictive model.
#### Dataset Variables

| **Variable** | Description |
|---|---|
| gender | Student's gender (male/female) |
| race_ethnicity | Student's racial or ethnic group (group A-E) |
| parental_level_of_education | Parent's education level |
| lunch | Lunch type (free/reduced, standard) |
| test_preparation_course | Completion of test preparation course (none, completed) |
| reading_score | Standardized reading test score (out of 100) |
| writing_score | Standardized writing test score (out of 100) |
| math_score | **_Target variable:_** Standardized math test score (out of 100) |
### Project Highlights
- **End-to-End ML Pipeline:** Includes data ingestion, transformation, model training, evaluation, and deployment using Flask.
- **Diverse Model Evaluation:** Explores and compares various regression models:
  - Linear Regression
  - Lasso
  - Ridge
  - Decision Tree
  - Random Forest
  - XGBoost
  - CatBoost
  - AdaBoost
  - Gradient Boosting.
- **Hyperparameter Tuning:** Employs GridSearchCV to optimize model parameters for enhanced performance.
- **Flask Web App:** Deploys a user-friendly web application allowing users to input student information and receive predicted math scores.
### Project Structure
```markdown
├── .ebextensions
│  └── python.config
├── artifacts
│   ├── data.csv
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── test.csv
│   └── train.pkl
├── notebook
│   ├── data
│   │   └── stud.csv
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
├── src
│   ├── components
│   │   ├── _init_.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline
│   │   ├── _init_.py
│   │   └── prediction_pipeline.py
│   ├── _init_.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
├── templates
│   ├── home.html
│   └── index.html
├── .gitignore
├── application.py
├── requirements.txt
└── setup.py
```
## How to Run

1. **Run the Flask App:**
   ```bash
   python application.py
2. **Access the Application:**
   ```markdown
   Open a web browser and navigate to http://127.0.0.1:5000/
