#!/usr/bin/env python3
import sys
import pandas as pd
from datadog import initialize, api

options = {
    'api_key': '<DATADOG_API_KEY>',
    'app_key': '<DATADOG_APPLICATION_KEY>'
}
metrics = []

def get_current_metric(timestamp, label, elapsed, success):
	metric = {}
	metric.update({'metric': 'test.metric'})
	metric.update({'points': [(timestamp, elapsed)]})
	curtags = {}
	curtags.update({'testcase': label})
	curtags.update({'success': success})
	metric.update({'tags': curtags})
	return metric

initialize(**options)

jtl_file = sys.argv[1]
df = pd.read_csv(jtl_file)

for index, row in df.iterrows():
	timestamp = row['timeStamp']/1000
	label = row['label']
	elapsed = row['elapsed']
	success = str(row['success'])
	metric = get_current_metric(timestamp, label, elapsed, success)
	metrics.append(metric)
	
api.Metric.send(metrics)
#print(metrics)
