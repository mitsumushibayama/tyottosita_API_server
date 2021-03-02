from fastapi import FastAPI
import uvicorn
import charadb

app = FastAPI()

@app.get("/characters")
async def get_all_characters():
	return charadb.get_all_characters()

@app.get("/characters/{color}")
async def get_specified_color_characters(color: str):
        return charadb.get_specified_color_characters(color)

@app.get("/characters/skill/type/{type}/cut/{cut}")
async def get_skill_characters(type: str, cut: int):
	return charadb.get_skill_characters(type, cut)


if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port = 8000)
