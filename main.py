from fastapi import FastAPI,Path,HTTPException,Query
import json

app = FastAPI()


@app.get('/')
def hello():
    return{'message':'patient management System API'}

def load_data():
    with open('patient.json','r') as f:
        data = json.load(f)

    return data
@app.get("/about")
def about():
    return{"message":"A fully functional API for patient record"}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str = Path(...,description = 'ID of the patient in DB', example= 'P001')):
    # load all the patient 
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='patient not found')

@app.get('/sort')
def sort_patients(sort_by: str =Query(..., description='sort on the basis of height, weight'),
                order: str = Query('asc', description='sort on the basis of order')):
    valid_fields = ['height', 'weight']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail='Invalid field, select from {valid_fields}')

    valid_orders = ['asc', 'dsc']
    if order not in valid_orders:
        raise HTTPException(status_code=400, detail='Invalid order, select from {valid_orders}')

    data = load_data()

    sort_order = True if order=='dsc' else False

    sorted_data = sorted(data.values(), key= lambda x: x.get(sort_by,0), reverse=sort_order)
    return sorted_data
        