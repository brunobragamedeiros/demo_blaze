
# Homework

## Set up

If you do not have Python installed, please install it.

To verify installation run

    python --version

Then clone this repository and 

    cd e2e

To install the project dependencies you have to create a virtual environment first

    python -m venv venv

Then you have to activate it

> If you use Windows 
-> `venv\Scripts\activate`

> If you use Mac
-> `source venv/bin/activate`

After activating the environment you can install all the dependencies

    python -m pip install --upgrade pip
    pip install -r requirements.txt

You also need to install playwright

    python -m playwright install

Now you can run the tests

    pytest tests/test_demo.py --html=report.html --self-contained-html

This command will run all the 5 tests and create a report that can be found inside e2e folder.

You can also access the execution of the tests in the pipeline. For that click on the tab Actions in this repository and open one of the executions. In the summary you will find the report generated. When clicking on the job title you'll find the pipeline and all the test execution.
