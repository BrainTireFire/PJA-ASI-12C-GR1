import os
import matplotlib.pyplot as plt
import modules.dataLoad as dataLoad
import modules.cleanData as cleanData
import modules.machineLearning as machineLearning
import modules.evaluateModel as evaluateModel
import modules.deployModel as deployModel

def main():
    # Downloadd dataset
    dataset_url = 'https://www.kaggle.com/datasets/bhavikjikadara/student-study-performance'
    data_destination = 'data'
    dataLoad.download_dataset(dataset_url, data_destination)

    # Read data and clean
    data_path = os.path.join(data_destination, 'student-study-performance/study_performance.csv')
    X, y = cleanData.clean_data(data_path)

    # Machine learning model
    model, X_test, y_test = machineLearning.train_model(X, y)

    # Evaluate model
    y_pred = model.predict(X_test)
    print(y_pred[:5])

    mae, rmse, r2 = evaluateModel.evaluate_model(y_test, y_pred)
    print('Model performance:')
    print("- Root Mean Squared Error: {:.4f}".format(rmse))
    print("- Mean Absolute Error: {:.4f}".format(mae))
    print("- R2 Score: {:.4f}".format(r2))

    # Save model
    output_dir = 'models'
    deployModel.save_model(model, output_dir)

    # Plot scatter
    evaluateModel.plot_scatter(y_test, y_pred)

if __name__ == "__main__":
    main()
