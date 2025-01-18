from sensor.exception import SensorException
import os 
import sys
from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb_collection
''' def test_exception():
    try:
        logging.info("here will come error")
        a=1/0
    except Exception as e:
       raise SensorException(e,sys)
if __name__=="__main__":
    try:
        test_exception()
    except Exception as e:
        print(e) '''
if __name__ == "__main__":
    file_path = r"C:\Users\shrav\Desktop\sensor_fault_detection\aps_failure_training_set1.csv"
    database_name = "csvtu"
    collection_name = "sensor"
    try:
        dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)
        logging.info("Data inserted into MongoDB successfully.")
    except Exception as e:
        logging.error(f"Error occurred: {e}")