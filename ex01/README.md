source ~/.zshrc
python -m venv venv
source venv/bin/activate

echo alias python='./venv/bin/python' >> venv/bin/activate
source venv/bin/activate

pip uninstall pandas
pip uninstall matplotlib

pip install pandas
pip install matplotlib

python aff_life.py

deactivate

rm -rf pycache
rm -rf venv
