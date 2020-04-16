# bamboo-archiver
```shell
virtualenv env 
pip install -r requirements.txt
pip install flake8
pip install autopep8
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude env
```