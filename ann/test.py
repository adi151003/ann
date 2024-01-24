import pandas as pd

# Load the dataset
url = "https://www.kaggle.com/datasets/saife245/english-premier-league"

try:
    data = pd.read_csv(url,error_bad_lines=False)
except Exception as e:
    print(f"Error loading the dataset: {e}")
    # Handle the error or exit the program as needed
    exit()

# Check for missing values
if data.isnull().any().any():
    # Handle missing values, for example:
    # data = data.dropna()
    print("Warning: Missing values detected. Data may need further cleaning.")

# Perform data transformation and preprocessing as needed

# Split the data into features and target variables
X = data.drop("target_column", axis=1)
y = data["target_column"]


from sklearn.neural_network import MLPClassifier

# Create a single-layer perceptron
single_layer_perceptron = MLPClassifier(hidden_layer_sizes=(1,), activation='relu')

# Create a two-layer perceptron
two_layer_perceptron = MLPClassifier(hidden_layer_sizes=(2,), activation='relu')

# Fit the models to your data
single_layer_perceptron.fit(X, y)
two_layer_perceptron.fit(X,y)