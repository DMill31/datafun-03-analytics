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

miller_get_csv.py \
    - Fetcher that fetches a CSV file about Obesity by State from the web \
miller_get_excel.py \
    - Fetcher that fetches an excel file about Titanic passengers from the web \
miller_get_json.py \
    - Fetcher that fetches a JSON file about NYC CitiBike stations from the web \
miller_get_text.py \
    - Fetcher that fetches a text file of the script of the Back to the Future trilogy from the web 

## Processors

miller_process_csv.py \
    - Processor that processes a CSV file on Obesity and calculates statistics from Obesity percentages \
miller_process_excel.py \
    - Processor that processes an excel file on Titanic passengers and counts how many men and women there were from Column E \
miller_process_json.py \
    - Processor that processes a JSON file about NYC CitiBike stations and listing how many stations are from each region \
miller_process_text.py \
    - Processor that processes a text file of the scripts from the Back to the Future trilogy and counting how many times the phrase "Great Scott" is said 