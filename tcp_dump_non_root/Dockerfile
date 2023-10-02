FROM ubuntu:20.04
RUN apt update && apt dist-upgrade -y && apt install tcpdump libcap2-bin -y
RUN useradd -m -s /bin/bash test-user
RUN setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump
RUN mkdir /pcap
RUN chown -R test-user /pcap
RUN chown test-user /usr/sbin/tcpdump
USER test-user
WORKDIR /pcap
#CMD ["tcpdump -i any -w /pcap/pcap.pcap"]
