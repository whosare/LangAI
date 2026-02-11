# from fastapi import FastAPI, UploadFile, File
# from fastapi.responses import JSONResponse
# import whisper
# import tempfile
# import os


# app=FastAPI()

# # Load model once at startup (important for speed)
# model = whisper.load_model("base")  # try "small" later for better accuracy

# @app.post("/transcribe")
# async def transcribe_audio(file: UploadFile = File(...)):
#     # Save upload to a temp file Whisper can read
#     suffix = os.path.splitext(file.filename)[-1] or ".webm"
#     with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
#         audio_bytes = await file.read()
#         tmp.write(audio_bytes)
#         tmp_path = tmp.name

#     try:
#         # Transcribe (force Spanish if you want consistency)
#         result = model.transcribe(tmp_path, language="es")
#         return JSONResponse({"text": result["text"]})
#     finally:
#         # Cleanup temp file
#         os.remove(tmp_path)


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}