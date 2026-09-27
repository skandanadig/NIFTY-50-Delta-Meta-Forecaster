from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge

def get_meta_learner(model_name):
    if model_name == 'RandomForest':
        return RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42)
    elif model_name == 'Ridge':
        return Ridge(alpha=1.0)
    else:
        raise ValueError(f"Unknown meta-learner: {model_name}")
