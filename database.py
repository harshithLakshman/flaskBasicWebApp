from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()


connection_string=os.environ['connectionString']
engine = create_engine(connection_string)



def load_job_openings():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        rows = result.fetchall()
        # Use the result.keys() to get column names
        column_names = result.keys()
        job_list = [dict(zip(column_names, row)) for row in rows]
        return job_list
    
def load_job_byId(id):
    with engine.connect() as conn:
        result=conn.execute(text("select * from jobs where id= :value"),{'value':id})
        job_openings=result.fetchall()
        column_names=result.keys()
        job_list=[dict(zip(column_names,row)) for row in job_openings]
        if len(job_list)<1:
            return None
        return job_list[0]