#!/bin/bash 
curl -XDELETE http://$1:9200/$2
curl -XPUT http://$1:9200/$2/ -d '{"mappings":{"'$3'":{"date_detection":false}}}'
curl -XPUT http://$1:9200/$2/_settings -d '{"index.mapping.total_fields.limit":5000}'
