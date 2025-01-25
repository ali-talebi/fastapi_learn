from fastapi import FastAPI 
import uvicorn 
app = FastAPI() 

@app.get('/')
async def root() : 
    return {'message' : 'hello world!' , 'team' : 'olt' } 

@app.get('/base/{name}')
async def SayReport(name) : 
    return {'name' : name }


if __name__ =="__main__" :
    uvicorn.run("main:app" , host="127.0.0.1" , port=8000 , reload= True )  
    