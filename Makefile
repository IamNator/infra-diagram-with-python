

run: diagram.py
    python diagram.py >> x_architecture.png

setup:
    pip install diagrams
    sudo apt update
    sudo apt install graphviz