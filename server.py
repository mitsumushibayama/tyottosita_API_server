from fastapi import FastAPI
import uvicorn
import charadb

app = FastAPI()

@app.get("/characters")
def get_all_characters():
	return charadb.get_all_characters()




if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port = 8000)
