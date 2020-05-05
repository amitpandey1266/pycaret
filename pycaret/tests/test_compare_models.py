import os, sys
sys.path.insert(0, os.path.abspath(".."))

#compare_models_test
import pytest
import pycaret.regression
import pycaret.datasets

def test_compare_models():
    data = pycaret.datasets.get_data('boston')
    reg1 = pycaret.regression.setup(data, target='medv',silent=True, html=False, session_id=123)
    models = pycaret.regression.compare_models(n_select=3)
    top_3 = len(models)
    assert top_3 == 3