# SSVEP-Interface-Navigation
Brain controlled game via SSVEP signal classification.

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/BrainwareITBA/SSVEP-Interface-Navigation.git
    cd SSVEP-Interface-Navigation
    ```
2. Create a virtual environment:
    ```
    python -m venv env
    ```
3. Activate the virtual environment and install the dependencies.
    * For Windows:
        ```
        ./env/Scripts/Activate.ps1
        pip install -r requirements.txt
        ```
    * For Linux / MacOS
        ```
        ./env/Scripts/activate
        pip install -r requirements.txt
        ```

> **WARNING**
>
> Pygame isn't updated for Python 3.11: If the previous step fails, install a pre-version ```pip install pygame --pre```

## Getting Started
To start the game, run:
```
python ./main.py [filename]
```

To change the configuration, go to `config.json`

### Monitor refresh rate 
* In Windows: https://support.microsoft.com/en-us/windows/change-your-display-refresh-rate-in-windows-c8ea729e-0678-015c-c415-f806f04aae5a

### Lab Streaming Layer
* GitHub repo: https://github.dev/chkothe/pylsl