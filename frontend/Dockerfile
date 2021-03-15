FROM node:15.11.0-alpine
COPY package.json /data/
WORKDIR /data/
RUN npm install --force
ENV PATH /data/node_modules/.bin:$PATH

COPY . /data/app/
WORKDIR /data/app/