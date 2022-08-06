FROM ubuntu:20.04
RUN apt-get update &&\
    apt-get install -y tzdata &&\
    apt-get install python3.7 -y &&\
    apt-get install python3-pip -y &&\
    apt-get install graphviz -y
EXPOSE 8501
WORKDIR /madden_project
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD streamlit run main.py

# streamlit-specific commands for config
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'