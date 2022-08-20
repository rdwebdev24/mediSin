import pickle
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/")
def read_item(q: Union[str, None] = None):
    loaded_model = pickle.load(open('model.h5', 'rb'))
    predict = loaded_model.predict(q)
    return {'res' : predict}
