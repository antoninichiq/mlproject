import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #C:\Users\anton\OneDrive\Documentos\mlproject\logs\06_21_2024_08_02_11.log
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #C:\Users\anton\OneDrive\Documentos\mlproject\logs\06_21_2024_08_02_11.log/\06_21_2024_08_02_11.log

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", #[ 2024-06-21 08:02:11,093 ] 18 root - INFO - Logging has starded
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has starded")
    
