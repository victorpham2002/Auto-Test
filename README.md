# Automation test website [bkel](https://e-learning.hcmut.edu.vn/)


![image](./selenium.gif)

## 📦 Installation

```
git clone https://github.com/loctvl842/Software-Testing--Proj3
cd Software-Testing--Proj3
python3 -m venv env
source env/bin/activate
pip install -r ./requirements.txt
```

## 🚀 Usage

Go to `src` folder and run the following commands

> Test login
```sh
python run.py test LoginSuite
```

> Test changing password
```sh
python run.py test ChangePasswordSuite
```

- Read the testcases in folder `testcases`
- Read the result of test in folder `solutions`

Create testcase by changing value in files `LoginSuite.py` and `ChangePasswordSuite.py`

