import requests
import argparse
import time
import json
import io
import gzip
import csv
import codecs
import pandas as pd 

# a = argparse.ArgumentParser()
# a.add_argument("--file_name",required=True,help="file containing warc paths with offsets")
# args = a.parse_args()

def download_page(record):
    offset, length = int(record['warc_record_offset']), int(record['warc_record_length'])
    offset_end = offset + length - 1

    # We'll get the file via HTTPS so we don't need to worry about S3 credentials
    # Getting the file on S3 is equivalent however - you can request a Range
    prefix = 'https://aws-publicdatasets.s3.amazonaws.com/'
    
    # We can then use the Range header to ask for just this set of bytes
    resp = requests.get(prefix + record['warc_filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})
    
    # The page is stored compressed (gzip) to save space
    # We can extract it using the GZIP library
    raw_data = io.BytesIO(resp.content
    f = gzip.GzipFile(fileobj=raw_data)
    # What we have now is just the WARC response, formatted:
    data = f.read()
    
    response = ""
    
    if len(data):
        try:
            warc, header, response = data.strip().split('\r\n\r\n', 2)
        except:
            pass
            
    return response

if __name__=='__main__':  
    df = pd.DataFrame()
    temp = pd.read_csv('test-warc.csv', iterator=True, chunksize=1000)
    df = pd.concat(temp, ignore_index=True)
    # records = (rec for rec in open(args.file_name, 'r'))
    for idx, row in df.iterrows():
        download = download_page(row)
        with open('warc%s.txt' %idx, 'w') as f:
            f.write(download)
