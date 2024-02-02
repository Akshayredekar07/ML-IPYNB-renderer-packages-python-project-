echo [$(date)]: "START"
echo [$(date)]: "Creating conda envirnment with python 3.11"
conda create --prefix ./env python=3.11 -y
echo [$(date)]: "Activate ./env"
source activate ./env
echo [$(date)]: "Installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END" 