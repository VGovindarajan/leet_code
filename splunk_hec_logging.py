import logging
import splunk_handler
from splunk-handler import SplunkHandler
    splunk = SplunkHandler(
        host='splunk.example.com',
        port='8088',
        token='851A5E58-4EF1-7291-F947-F614A76ACB21',
        index='main'
        #allow_overrides=True # whether to look for _<param in log data (ex: _index)
        #debug=True # whether to print module activity to stdout, defaults to False
        #flush_interval=15.0, # send batch of logs every n sec, defaults to 15.0, set '0' to block thread & send immediately
        #force_keep_ahead=True # sleep instead of dropping logs when queue fills
        #hostname='hostname', # manually set a hostname parameter, defaults to socket.gethostname()
        #protocol='http', # set the protocol which will be used to connect to the splunk host
        #proxies={
        #           'http': 'http://10.10.1.10:3128',
        #           'https': 'http://10.10.1.10:1080',
        #         }, set the proxies for the session request to splunk host
        #
        #queue_size=5000, # a throttle to prevent resource overconsumption, defaults to 5000, set to 0 for no max
        #record_format=True, whether the log format will be json
        #retry_backoff=1, the requests lib backoff factor, default options will retry for 1 min, defaults to 2.0
        #retry_count=5, number of retry attempts on a failed/erroring connection, defaults to 5
        #source='source', # manually set a source, defaults to the log record.pathname
        #sourcetype='sourcetype', # manually set a sourcetype, defaults to 'text'
        #verify=True, # turn SSL verification on or off, defaults to True
        #timeout=60, # timeout for waiting on a 200 OK from Splunk server, defaults to 60s
    )

    logging.getLogger('').addHandler(splunk)

    logging.warning('hello!')