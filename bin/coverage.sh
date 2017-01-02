py.test --cov-config .coveragerc \
        --cov-report html \
        --cov applicious/apps && \
python -c "import webbrowser, os; \
           webbrowser.open('file://' + os.getcwd() + \
                           '/htmlcov/index.html')"
