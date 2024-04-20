# PJA-ASI-12C-GR1

## Getting started

### Tworzenie środowiska miniconda
1.	Pobrać miniconda z oficjalnej strony.
2.	Uruchomić w Anaconda PowerShell Prompt skrypt create_env_conda.ps1 (wpisując ./create_env_conda.ps1, kiedy znajdujesz się w katalogu src/config).
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
