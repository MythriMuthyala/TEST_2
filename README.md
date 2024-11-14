# Heart-Disease-Prediction-using-Machine-Learning
Preventing Heart diseases has become more than necessary. Good data-driven systems for predicting heart diseases can improve the entire research and prevention process, making sure that more people can live healthy lives. This is where Machine Learning comes into play. Machine Learning helps in predicting the Heart diseases, and the predictions made are quite accurate.

The project involved analysis of the heart disease patient dataset with proper data processing. Then, different models were trained and and predictions are made with different algorithms KNN, Decision Tree, Random Forest,SVM,Logistic Regression etc
This is the jupyter notebook code and dataset I've used for my Kaggle kernel 'Binary Classification with Sklearn and Keras'

I've used a variety of Machine Learning algorithms, implemented in Python, to predict the presence of heart disease in a patient. This is a classification problem, with input features as a variety of parameters, and the target variable as a binary variable, predicting whether heart disease is present or not.

Machine Learning algorithms used:

1. Logistic Regression (Scikit-learn)
2. Naive Bayes (Scikit-learn)
3. Support Vector Machine (Linear) (Scikit-learn)
4. K-Nearest Neighbours (Scikit-learn)
5. Decision Tree (Scikit-learn)
6. Random Forest (Scikit-learn)
7. XGBoost (Scikit-learn)
8. Artificial Neural Network with 1 Hidden layer (Keras)
   
### Git and other commands used in the command prompt:
1. `mkdir <file_name>` to create the folder
2. `cd <file name>` to go inside the folder
3. `git init`, initializing folder as git repository
5. `git add .` to add all the files into git track
6. `git commit -m "<message>"`, it commits whatever is there in the track
7. `git remote add origin <GitHub repository link>`, builds connection between git and github
8. `git push --set-upstream origin master`, sends all the files from git to github.
   
Docker Commands:
1. `docker build -t folder_name> .`
2. `docker run <folder_name>`

### Steps:
1. Create the required files such as the dataset csv file(heart.csv), training model python file, requirements txt file, Dockerfile.
2. Create a new item under Freestyle Project item type
3. Select Git in Source Code Management and paste your github repository url
4. Add Execute Windows Batch Command step in Build Steps
5. Save configurations
6. Build now and visualize console output
7. Now open command prompt with the path of the folder containing the required files
8. Execute the Docker commands mentioned above
9. Visualize the output in the command prompt and in the Docker Desktop app

### Output:
![Screenshot 2024-10-27 193431](https://github.com/user-attachments/assets/90b68158-f2c7-49ef-b520-827ace204070)

![Screenshot 2024-10-27 193359](https://github.com/user-attachments/assets/54a2b570-8a14-4bc7-97e3-96ca04dd1d6d)

Accuracy achieved: 95% (Random Forest)




