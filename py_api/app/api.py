from fastapi import FastAPI
from fastapi.responses import StreamingResponse 
app = FastAPI(root_path="/api")

# simple example
@app.get("//hello")
def hello(name: str = "anonimo"):
  try:
    if(name==""):
       name = "anonimo" 
    return {'Hello ' + name + '!'} 
  except Exception as e:
    return str(e)
    # if(type(e)==type(TypeError)):
    #    return {"detail": "name parameter cannot be None"}

# return image
@app.get("//plot-iris")
def plot_iris():

    import pandas as pd
    import matplotlib.pyplot as plt

    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('iris.png')
    __file = open('iris.png', mode="rb")

    return StreamingResponse(__file, media_type="image/png")

# example json
@app.get("//plot-iris-data")
def get_iris():

    import pandas as pd
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    return iris
