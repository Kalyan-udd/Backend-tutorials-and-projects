from fastapi import FastAPI

# 1. create the App insatance ("The Server")
app = FastAPI()


# 2. Define the "Brain" (The ML logic)
def simple_ml_model(input_number: int):
    #In a real project, this is where your .pkl file would predick
    return input_number*2

# 3. Create the Endpoint ("the window")
@app.get("/predict")
def predict_valu(number: int):
    result = simple_ml_model(number)
    return {"input": number, "prediction": result}