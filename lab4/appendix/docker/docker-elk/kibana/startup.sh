#!/bin/bash

# wait for the Elasticsearch container to be ready before starting Kibana.
echo "Waiting for Elasticsearch"
while true; do
	nc -q 1 elasticsearch 9200 2>/dev/null && break
done

echo "Starting Kibana"
exec kibana
