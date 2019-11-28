#run_coverage.sh
#Run coverage on only one dir. by default, it runs on everything
#as of now, I run only on one module
coverage run --source /abs/path/module/ -m unittest /abs/path/module/test/test_mymodule.py
