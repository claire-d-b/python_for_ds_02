source ~/.zshrc
python -m venv venv
source venv/bin/activate

echo alias python='./venv/bin/python' >> venv/bin/activate
source venv/bin/activate

pip uninstall pandas
pip uninstall matplotlib

pip install pandas
pip install matplotlib

python projection_life.py

deactivate

rm -rf __pycache__
rm -rf venv
