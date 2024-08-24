# Nutrition Based Food Health Classifier Using Machine Learning

### Project Description
<p align='justify'>
This project focuses on developing a machine learning model that classifies food items based on their nutritional content per 100g, determining whether they are healthy or not. By analyzing key nutritional factors such as fat, saturated fat, carbohydrates, sugars, fiber, proteins, and sodium, the model predicts the healthiness of food items. The primary objective is to assist users in making informed dietary choices by leveraging AI to provide instant feedback on the nutritional quality of food.
</p>

### ScreenShot
<img width="800" height="400" align="center" src="/screenshots/test_image.png">

### Technologies Used in This Project
* **Python** : Core programming language used for developing the model and application
* **Pandas** : For data manipulation and cleaning
* **Scikit-learn** : For building and evaluating the model
* **Flask** : for deploying the model as a web application
* **Jupyter-notebook** : For exploratory data analysis (EDA)
* **HTML/CSS** : For designing the web interface of the application
* **Git/Github** : For version control and hosting the project repository



### Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Sharan-vj/End2End_Nutrition_Based_Food_Health_Classifier_Using_ML.git
    cd End2End_Nutrition_Based_Food_Health_Classifier_Using_ML.git
    ```

2. **Create a Virtual Environment**:
    ```bash
    conda create --name <env name> python=3.10 -y
    ```
3. **Activate the Virtual Enviroment**
    ```bash
    conda activate <env name>
    ```
4. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask Application**:
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000/`.

### Usage
1. **Upload Nutritional Data**: Input the nutritional values (per 100g) in the web interface.
2. **Get Prediction**: The model will predict and display whether the food is healthy or not based on the input values.

### Dataset
The dataset used for training and testing the model contains nutritional information of various food items and a corresponding label indicating whether the food is healthy or not. The dataset is located in the `data/` directory.

### Model
The model is built using Scikit-learn and is trained to classify the healthiness of food based on the provided nutritional features. The trained model is saved in the `models/` directory as a pickle file (`foodhealth_classifier.pkl`).

### Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Acknowledgments
* Special thanks to the open-source community for the libraries used in this project.
