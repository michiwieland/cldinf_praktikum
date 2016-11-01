FROM kibana

# preconditions
RUN apt-get update && apt-get install -y netcat

# copy script from host to kibana container
COPY startup.sh /tmp/startup.sh

# mark as executable
RUN chmod +x /tmp/startup.sh 

# execute
CMD ["/tmp/startup.sh"] 

