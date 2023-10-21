# FastAPI

![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=Cloudflare&logoColor=white)

````bash
pip install fastapi
pip3 install "uvicorn[standard]" --user
python -m uvicorn main:app --reload
pip freeze > requirements.txt
pip install websockets


docker build -t fastapi .

docker run -d --name fastapi_container -p 80:80 fastapi



````

## Without Docker

````bash

cd FastAPI\app

python -m uvicorn main:app --reload


INFO:     Will watch for changes in these directories: ['..\\FastAPI\\app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [6824] using WatchFiles
INFO:     Started server process [10152]
INFO:     Waiting for application startup.
INFO:     Application startup complete. 

#swagger
http://127.0.0.1:8000/docs

PORT=8000


````

````Code
echo "# FastAPI" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/joaosgomes/FastAPI.git
git push -u origin main
````
