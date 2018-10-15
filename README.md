# Plagiarism_Detector
**A basic python API developed on django platform for calculating similarity percentage/plagiarism percentage between original and reference code.**

This is a simple plagiarism detection tool for python code, the basic idea is to normalize python AST representation and use difflib to get the modification from referenced code to candidate code. The plagiarism defined in pycode_similar is how many referenced code is plagiarized by candidate code, which means swap referenced code and candidate code will get different result.

- Clone the repo on to your system.
- Add all the requirements to your system as mentioned in requirements.txt.
- You can use a virtual environment if you want to keep your development environment seperate.

**Go to wecp_assignment/api/wecp_assign** and run -

```
python manage.py runserver

```
Now make **POST** request using POSTMAN or some other service to make a request to - **http://127.0.0.1:8000/api/show/**
and in the body of the request upload your two python files.

**NOTE**
- use **.txt** version of the files, don't upload .py files.
- make sure the files are compiled correctly, should not have syntactical errors.
- the first argument should be your **Source code** and the second should be **reference code** for which you want to check
plagiarism.
