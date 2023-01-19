
import xgboost
model = xgboost.XGBClassifier()
model.load_model("trained_model.xgb")

def predict(data): 
    model = xgboost.XGBClassifier()
    model.load_model("trained_model.xgb")
    return model.predict(data)
    
