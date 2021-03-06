images = {
    "1": """
    FROM ubuntu:16.04
    RUN apt-get update
    RUN apt-get install -y openssh-server
    RUN mkdir /var/run/sshd
    RUN echo 'root:%s' |chpasswd
    RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
    RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
    EXPOSE 22 80
    CMD    ["/usr/sbin/sshd", "-D"]
    """,

    "2": '''
    FROM ubuntu:16.04
    RUN apt-get update -y
    RUN apt-get upgrade -y
    RUN apt-get install -y openssh-server
    RUN apt-get install python3 -y && apt-get install python -y
    RUN mkdir /var/run/sshd
    RUN echo 'root:%s' | chpasswd
    RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
    RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
    EXPOSE 22 80
    CMD ["/usr/sbin/sshd", "-D"]
    ''',

    '3': '''
    FROM ubuntu:16.04
    RUN apt-get update -y
    RUN apt-get upgrade -y
    RUN apt-get install -y openssh-server
    RUN apt-get install nodejs -y && apt-get install nodejs-legacy -y && apt-get install npm -y
    RUN mkdir /var/run/sshd
    RUN echo 'root:%s' | chpasswd
    RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
    RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
    EXPOSE 22 80
    CMD ["/usr/sbin/sshd", "-D"]
    '''

}