# PJA-ASI-12C-GR1

## Getting started

### Tworzenie środowiska miniconda
1.	Pobrać miniconda z oficjalnej strony.
2.	Uruchomić w PowerShell skrypt create_env_conda.ps1 (wpisując ./ create_env_conda.ps1, kiedy znajdujesz się w katalogu z tym).
Przed uruchomieniem upewnij się czy plik environments.yml istnieje. W tym pliku znajdują się dane dotyczące env:
Dokładnie nazwa, wszystkie pakiety wraz z wersjami

### Wykonanie głownego skryptu main.py
1. Aby utworzyć, wytrenować, przygotować i zapisać model należy urchomić skrypt main.py
2. main.py uruchamia pomniejsze moduły, które są w foldrze "modules".
3. Pomniejsze moduly sa odpowiedzialne za tworzenie, ewaluacje modelu, pobieranie datasetu itp.
