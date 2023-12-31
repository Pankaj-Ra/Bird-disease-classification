from src.cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx=====x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model stage"

try:
    logger.info(f"******************")
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = PrepareBaseModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx=====x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx=====x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Evaluation stage"

try:
    logger.info(f"***************")
    logger.info(f">>>>>>>>> {STAGE_NAME} starting <<<<<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e