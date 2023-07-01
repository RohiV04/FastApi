from fastapi import APIRouter
from models.note import Note
from config.db import con   
from schema.note import noteEntity,notesEntity
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates 
from fastapi.responses import JSONResponse
note=APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=  con.notes.notes.find()
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc":doc["desc"]
        })
        # print(doc)
    return templates.TemplateResponse("index.html", {"request": request,"newDocs":newDocs})


# @note.post("/")
# def add_note(note: Note):
#     inserted_note=con.notes.notes.insert_one(dict(note))
#     return noteEntity(inserted_note)


@note.post("/")
async def create_item(request: Request):
    form_data = await request.form()
    form_dict=dict(form_data)
    inserted_note = con.notes.notes.insert_one(form_dict)
    return JSONResponse(content={"Success": True})
