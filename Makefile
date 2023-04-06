
set:
    export COMPANY_NAME="some_company"

run: diagram.py
    python diagram.py

setup:
    pip install diagrams
    sudo apt update
    sudo apt install graphviz