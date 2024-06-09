# PJA-ASI-12C-GR1

## Getting started

### Tworzenie środowiska miniconda

1. Pobrać miniconda z oficjalnej strony.
2. Uruchomić w Anaconda PowerShell Prompt skrypt create_env_conda.ps1 (wpisując ./create_env_conda.ps1, kiedy znajdujesz się w katalogu src/config).
   Przed uruchomieniem upewnij się czy plik environments.yml istnieje. W tym pliku znajdują się dane potrzebne do zainstalowania wymaganych pakietów w środowisku.

### Wykonanie głownego skryptu main.py (1 wersja projektu)

1. Aby utworzyć, wytrenować, przygotować i zapisać model należy urchomić skrypt main.py
2. main.py uruchamia pomniejsze moduły, które są w foldrze "modules".
3. Pomniejsze moduly sa odpowiedzialne za tworzenie, ewaluacje modelu, pobieranie datasetu itp.

### Uruchomienie kedro (2 wersja projektu)

Wersja projektu przygotowana jako pipeline kedro została umieszczona w osobnym folderze. Aby ją uruchomięc należy wykonać wszystkie kroki z sekcji "Tworzenie środowiska minicona", a następnie:

1. Przejść do folderu "asi-kedro" znajdującego się w głównym katalogu repozytorium
2. Wywołać komendę "kedro run"
   Przy pierwszym uruchomieniu projektu użytkownik zostanie poproszony o klucz autoryzacyjny do swojego konta w portalu Weights&Biases
   Aby wygenerować wizualizację pipeline'u należy w tym samym katalogu uruchomić polecenie "kedro viz run"

### Docker

Aby uruchomic: docker run -v .:/home/kedro_docker -e pipeline={nazwa pipeline'u} -e wbKey={twój klucz Weights&Biases} pja-asi-12c-gr1
Aby zbudowac projekt: kedro docker build

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
