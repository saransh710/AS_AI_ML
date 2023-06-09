import unittest
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

class DiabetesPredictionTest(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv("/content/diabetes_1_05_06.csv")
        self.X = self.df.drop('diabetes', axis=1)
        self.y = self.df['diabetes']
        
        self.nb_model = GaussianNB()
        self.nb_model.fit(self.X, self.y)

        self.dt_model = DecisionTreeClassifier()
        self.dt_model.fit(self.X, self.y)
    
    def test_diabetes_positive(self):
        user_data = pd.DataFrame({
            'Glucose': [45],
            'bloodpressure': [63]
        })
        nb_prediction = self.nb_model.predict(user_data)
        dt_prediction = self.dt_model.predict(user_data)
        
        self.assertEqual(nb_prediction[0], 1)
        self.assertEqual(dt_prediction[0], 1)
    
    def test_diabetes_negative(self):
        user_data = pd.DataFrame({
            'Glucose': [40, 40, 20, -10],
            'bloodpressure': [92, 50, 200, -10]
        })
        nb_prediction = self.nb_model.predict(user_data)
        dt_prediction = self.dt_model.predict(user_data)
        
        self.assertEqual(nb_prediction.tolist(), [0, 0, 0, 0])
        self.assertEqual(dt_prediction.tolist(), [0, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()
