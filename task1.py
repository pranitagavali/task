from fastapi import Body, FastAPI

app = FastAPI()

INFO = [
    {'FirstName': 'Pranita', 'LastName': 'Gavali', 'Phone_Number': '8668470672', 'Country_code': '+91',
     'Email': 'pranitagavali01@gmail.com', 'UseId': '1'},
    {'FirstName': 'Priyal', 'LastName': 'Chawda', 'Phone_Number': '8668371672', 'Country_code': '+91',
     'Email': 'priyal@gmail.com', 'UseId': '2'},
    {'FirstName': 'Pranoti', 'LastName': 'Bharade', 'Phone_Number': '8764470672', 'Country_code': '+91',
     'Email': 'pranoti@gmail.com', 'UseId': '3'},
    {'FirstName': 'Somya', 'LastName': 'Bharade', 'Phone_Number': '8755470672', 'Country_code': '+91',
     'Email': 'somya@gmail.com', 'UseId': '4'},
    {'FirstName': 'Gaurav', 'LastName': 'Patil', 'Phone_Number': '8555470672', 'Country_code': '+91',
     'Email': 'gaurav@gmail.com', 'UseId': '5'},

]


@app.get("/api-endpoint")
async def first_api():
    return INFO


@app.get("/task1/")
async def read_country_code_by_query(country_code: str):
    info_to_return = []
    for info in INFO:
        if info.get('Country_code') == country_code:
            info_to_return.append(info)
    return info_to_return


@app.post("/task1/create_info")
async def create_book(new_info=Body()):
    INFO.append(new_info)


@app.put("/task1/update_info")
async def update_info(updated_info=Body()):
    for i in range(len(INFO)):
        if INFO[i].get('UseId') == updated_info.get('UseId'):
            INFO[i] = updated_info


@app.delete("/task1/delete_info/{info_useid}")
async def delete_book(info_useid: str):
    for i in range(len(INFO)):
        if INFO[i].get('UseId') == info_useid:
            INFO.pop(i)
            break
