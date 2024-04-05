import os
import matplotlib.pyplot as plt
import modules.download_dataset as download_dataset
import modules.clean_data as clean_data
import modules.machine_learning as machine_learning
import modules.evaluate_model as evaluate_model
import modules.deploy_model as deploy_model

def main():
    # Downloadd dataset
    dataset_url = 'https://www.kaggle.com/datasets/bhavikjikadara/student-study-performance'
    data_destination = 'data'
    download_dataset.download_dataset(dataset_url, data_destination)

    # Read data and clean
    data_path = os.path.join(data_destination, 'student-study-performance/study_performance.csv')
    X, y = clean_data.clean_data(data_path)

    # Machine learning model
    model, X_test, y_test = machine_learning.train_model(X, y)

    # Evaluate model
    y_pred = model.predict(X_test)
    print(y_pred[:5])

    mae, rmse, r2 = evaluate_model.evaluate_model(y_test, y_pred)
    print('Model performance:')
    print("- Root Mean Squared Error: {:.4f}".format(rmse))
    print("- Mean Absolute Error: {:.4f}".format(mae))
    print("- R2 Score: {:.4f}".format(r2))

    # Save model
    output_dir = 'models'
    deploy_model.save_model(model, output_dir)

    # Plot scatter
    evaluate_model.plot_scatter(y_test, y_pred)

if __name__ == "__main__":
    main()
