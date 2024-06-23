# PJA-ASI-12C-GR1

## Getting started

### Creating a Miniconda Environment

1. Download Miniconda from the official website.
2. Run the Script in Anaconda PowerShell Prompt: Navigate to the src/config directory.
   Ensure that the environments.yml file exists, as it contains the necessary data for installing required packages in the environment.
   Execute the script by entering ./create_env_conda.ps1.

### Running the Main Script (main.py)

1. To create, train, prepare, and save the model, run the main.py script.
2. main.py triggers smaller modules located in the "modules" folder.
3. These smaller modules are responsible for tasks like creating and evaluating the model, fetching datasets, etc.

### Running Kedro (Version 2 of the Project)

This project version, prepared as a Kedro pipeline, is placed in a separate folder. Follow these steps:

1. Complete all steps from the "Creating a Miniconda Environment" section.
2. Navigate to the asi-kedro folder located in the root directory of the repository.
3. Execute the command kedro run. The first time you run the project, you will be prompted for an authorization key for your Weights & Biases account.
   To generate a visualization of the pipeline, run the command kedro viz run in the same directory.

### Docker

To Run:

Execute docker run -v .:/home/kedro_docker -e pipeline={pipeline name} -e wbKey={your Weights & Biases key} pja-asi-12c-gr1.
To Build the Project:

Execute kedro docker build.

# ASI_KEDRO

## Overview

This is your new Kedro project, which was generated using `kedro 0.19.3`.

Take a look at the [Kedro documentation](https://docs.kedro.org) to get started.

## Rules and guidelines

In order to get the best out of the template:

- Don't remove any lines from the `.gitignore` file we provide
- Make sure your results can be reproduced by following a data engineering convention
- Don't commit data to your repository
- Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `requirements.txt` for `pip` installation.

To install them, run:

```
pip install -r requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
pytest
```

You can configure the coverage threshold in your project's `pyproject.toml` file under the `[tool.coverage.report]` section.

## Project dependencies

To see and update the dependency requirements for your project use `requirements.txt`. You can install the project requirements with `pip install -r requirements.txt`.

[Further information about project dependencies](https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, 'session', `catalog`, and `pipelines`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter

To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab

To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython

And if you want to run an IPython session:

```
kedro ipython
```

### How to ignore notebook output cells in `git`

To automatically strip out all output cell contents before committing to `git`, you can use tools like [`nbstripout`](https://github.com/kynan/nbstripout). For example, you can add a hook in `.git/config` with `nbstripout --install`. This will run `nbstripout` before anything is committed to `git`.

> _Note:_ Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://docs.kedro.org/en/stable/tutorial/package_a_project.html)
