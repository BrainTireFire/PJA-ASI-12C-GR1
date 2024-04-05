import os
import logging
import matplotlib.pyplot as plt
import modules.download_dataset as download_dataset
import modules.clean_data as clean_data
import modules.machine_learning as machine_learning
import modules.evaluate_model as evaluate_model
import modules.deploy_model as deploy_model

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        # Download dataset
        dataset_url = 'https://www.kaggle.com/datasets/bhavikjikadara/student-study-performance'
        data_destination = 'data'
        download_dataset.download_dataset(dataset_url, data_destination)
        logger.info('Dataset downloaded successfully')

        # Read data and clean
        data_path = os.path.join(data_destination, 'student-study-performance/study_performance.csv')
        X, y = clean_data.clean_data(data_path)
        logger.info('Data cleaning and preprocessing completed')

        # Machine learning model
        model, X_test, y_test = machine_learning.train_model(X, y)
        logger.info('Machine learning model trained successfully')

        # Evaluate model
        y_pred = model.predict(X_test)
        mae, rmse, r2 = evaluate_model.evaluate_model(y_test, y_pred)
        logger.info('Model performance:')
        logger.info("- Root Mean Squared Error: {:.4f}".format(rmse))
        logger.info("- Mean Absolute Error: {:.4f}".format(mae))
        logger.info("- R2 Score: {:.4f}".format(r2))

        # Save model
        output_dir = 'models'
        deploy_model.save_model(model, output_dir)
        logger.info('Model saved successfully')

        # Plot scatter
        evaluate_model.plot_scatter(y_test, y_pred)
        logger.info('Scatter plot generated')

    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    main()
