import inspect

from django.test import TestCase

from .income_classifier.random_forest import RandomForestClassifier
from ..ml.registry import MLRegistry


class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
            "ph": 10.228,
            "Hardness": 203.361,
            "Solids": 28749.687,
            "Chloramines": 7.890,
            "Sulfate": 303.309,
            "Conductivity": 592.308,
            "Organic_carbon": 17.927,
            "Trihalomethanes": 84.603,
            "Turbidity": 4.075,
        }
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response["status"])
        self.assertTrue('label' in response)
        self.assertEqual('0', response['label'])

    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "water_classifier"
        algorithm_object = RandomForestClassifier()
        algorithm_name = "random forest"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "Dmitriy"
        algorithm_description = "Random Forest with simple pre- and post-processing"
        algorithm_code = inspect.getsource(RandomForestClassifier)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name, algorithm_status,
                               algorithm_version, algorithm_owner, algorithm_description, algorithm_code)
        self.assertEqual(len(registry.endpoints), 1)
