# common-crawl-toolkit
toolkit for building custom corpuses from Common Crawl data 

# Introduction
I've faced one problem common to all projects I've taken on as an AI Engineer, whether that project involves understanding market sentiment towards commodity prices, tagging news articles to multiple labels or building language models for languages such as Indonesian: we don't have a training corpus customised to the problem we want to solve. After trialling different approaches to solving this problem (and getting burned in the process!) I've settled on using Common Crawl as a primary source of data for building an NLP dataset that's specific to a particular domain or use case.  

However, leveraging Common Crawl can be a messy process. There are many examples of how others have used crawl data, but they can be rather scattered. Hence I've started to compile a toolkit for how to use Common Crawl data depending on your specific use case. So far, one tool I've added to this toolbox is a pipeline for building a corpus that

## build-language-specific-corpuses
Language annotations can be gotten from the metadata of the warc files that Common Crawl files are saved as. While there are different command-line utilities and python scripts for parsing WARC metadata, I've found the easiest way to filter for language-specific domains is to use the the columnar index for querying Common Crawl 

1. Setup Amazon Athena to query the columnar index as per `query-columnar-index-instructions.md` 
source: https://github.com/commoncrawl/cc-index-table
2. Query the columnar index using `get_languages.sql` 
source: https://github.com/commoncrawl/cc-index-table
2. Parse the resulting CSV with by running `python build_corpus.py` * this is still a WIP * 
source code modified from: https://www.bellingcat.com/resources/2015/08/13/using-python-to-mine-common-crawl/ 

![](images/custom-corpuses-1.png)
![](images/custom-corpuses-2.png)
![](images/custom-corpuses-3.png)
![](images/custom-corpuses-4.png)
![](images/custom-corpuses-5.png)
![](images/custom-corpuses-6.png)
![](images/custom-corpuses-7.png)
![](images/custom-corpuses-8.png)
![](images/custom-corpuses-9.png)