FROM node:alpine

WORKDIR .

COPY ./modules/frontend/package.json .
COPY ./modules/frontend/package-lock.json .

RUN npm install
RUN npm install react-scripts@3.4.3 -g

CMD ["pwd"]
COPY ./modules/frontend .

EXPOSE 3000

CMD ["npm", "start"]

