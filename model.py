import xgboost




model = xgboost.XGBClassifier()
model.load_model("trained_model.xgb")

model
