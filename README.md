# datafun-03-analytics
Repository for Module 3 of Data Analytics Fundamentals

## Create Project Virtual Environment

On Windows, create a project virtual environment in the .venv folder. 

```shell

py -m venv .venv
.venv\Scripts\Activate
py -m pip install -r requirements.txt

```

## Git add and commit 

```shell
git add .
git commit -m "add .gitignore, cmds to readme"
git push -u origin main
```

## Fetchers

miller_get_csv.py
    - Fetcher that fetches a CSV file about Obesity by State from the web
miller_get_excel.py
    - Fetcher that fetches an excel file about Titanic passengers from the web
miller_get_json.py
    - Fetcher that fetches a JSON file about NYC CitiBike stations from the web
miller_get_text.py
    - Fetcher that fetches a text file of the script of the Back to the Future trilogy from the web