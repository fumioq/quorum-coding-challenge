# quorum-coding-challenge

Repository that contains all project files for coding challenge

## Deliverables

You will be provided with a list of legislators, bills, votes, and vote results as specified above. You’ll be asked to answer the following questions:

1. For every legislator in the dataset,how many bills did the legislator support (voted for the bill)? How many bills did the legislator oppose?
2. For every bill in the dataset, how many legislators supported the bill? How many legislators opposed the bill? Who was the primary sponsor of the bill?

## Discussions:

1. Discuss your solution’s time complexity. What tradeoffs did you make?
2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?
3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?
4. How long did you spend working on the assignment?

## ER-Model

![ER-Model](https://raw.githubusercontent.com/fumioq/quorum-coding-challenge/refs/heads/main/images/quorum-er-model.jpeg)

# How to use

## Prepare your environment

- Make sure you have git and python installed. Install Miniconda or pyvenv as well.
- Clone repository:
  - Open terminal and run the command below
  - git clone https://github.com/fumioq/quorum-coding-challenge.git
- Make the new "quorum-coding-challenge" as current directory using:
  - cd quorum-coding-challenge/
- Create a new environment. Here, I'm using miniconda and setting the python version to 3.12, but you could also create a new environment with pyvenv.
  - conda create -n quorum python=3.12 -y
- Activate your environment (follow the steps to activate it according to your environment miniconda / pyvenv).
- Install dependencies. Using uv to make the installation faster. It is also great to reduce image build time on future CICD pipelines.
  - pip install uv
  - pip uv pip install -r requirements.txt

## How to run

- Make sure that your current directory is "quorum-coding-challenge"
- Run on your terminal
  - python generate_report.py

## Outputs

- Outputs are generated inside the "reports" folder
  - legislators-support-oppose-count.csv - All legislators' supported and opposed bills count.
  - bills-support-oppose-count-with-main-sponsor.csv - Bills with sponsors and number of legislators that opposed and supported them.

# Future features

- download data directly from the web. Data is publicly available, so making requests to the data directly will make maintainability of this code better.
- data quality check (cehck for duplicates or missing data).
- if data valume is considerable, implement parallel processing with threads.
  - if data is greater than 2GB, consider using Big Data tools like spark.
