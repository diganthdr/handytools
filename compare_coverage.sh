#coverage_compare.sh

#Use status file to indicate and prevent overwrite of coverage.previous file. Else two consecutive fails will pass the script, as it makes previous and latest reports same.
STATUS_FILE=.coveragefailed

#creates previous file if not present
touch coverage.previous coverage.latest
if [ -f $STATUS_FILE ]; then
    echo "Last coverage yet to be fixed"
else
    echo "OK"
    mv coverage.latest coverage.previous
fi

coverage report --skip-covered --omit="*/test*" > coverage.latest #skip empty files which has 100% coverage, skip actual files which has coverage of 100%
python compare_coverage.py

if [ $? -eq 0 ]; then
    echo OK
    rm -f $STATUS_FILE
else
    echo FAIL
    touch $STATUS_FILE
fi

