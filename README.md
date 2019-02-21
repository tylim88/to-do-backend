## create project

```
conda create -n todolist
```
create todolist environment

```
source activate todolist
```
activate environment

```
pip install -r requirments.txt
```
install packages 


## setup database

```
export FLASK_APP=app.py
```
flask sql alchemy want to know the main script
actually can skip this if your main script name is app.py

```
export ENV_PATH=config.dev
```
to setup database in dev mode

```
export ENV_PATH=config.prod
```
to setup database in prod mode

```
flask db init
```
setup migration files

```
flask db migrate -m "creat todolist table"
```
commit database migration
if you run this for the first time it will create database without any table
dont read the database when carrying this operation

```
flask db upgrade
```
apply database migration, dont read the database when carrying this operation

```
ENV_PATH=config.dev python app.py
```
Start in dev mode

```
ENV_PATH=config.prod python app.py
```
Start in prod mode