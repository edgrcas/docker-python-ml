# set base image (host OS)
FROM python:3.9.2-alpine3.13

# set the working directory in the container
RUN mkdir /app
WORKDIR /app

# copy the dependencies file to the working directory
COPY . /app

RUN apk update
RUN apk --no-cache --update-cache add make automake gcc gfortran g++ \
    build-base python3-dev musl-dev linux-headers openblas-dev binutils
RUN pip install cython

# install dependencies
RUN pip install -r _packages.txt

