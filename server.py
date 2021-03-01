from fastapi import FastAPI
import uvicorn
import charadb

app = FastAPI()

@app.get("/characters")
def get_all_characters():
	return charadb.get_all_characters()

@app.get("/characters/{color}")
def get_specified_color_characters(color : str):
        return charadb.get_specified_color_characters(color)



if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port = 8000)
