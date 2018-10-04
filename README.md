# jmeter-datadog-publisher
This is a simple python script to post your jmeter test results as datadog metrics. [Jmeter](http://jmeter.apache.org/) saves the test results into a jtl file (csv) by default. This script will parse that file and create datadog metrics for every transaction in your jmeter test plan. The data sent to datadog includes: Transaction name, timestamp, response time and success (true/false). 

## Usage:
````
python post_jmeter_results_to_datadog.py sample_result.jtl
````
## Requirements:
* [pandas](https://github.com/pandas-dev/pandas)
* [datadog api](https://github.com/DataDog/datadogpy)
