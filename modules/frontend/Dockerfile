FROM node:alpine

WORKDIR .

COPY ./modules/frontend/package.json .
COPY ./modules/frontend/package-lock.json .

RUN rm -rf node_modules package-lock.json
RUN npm cache clean --force
RUN npm cache verify
RUN npm install
RUN npm install react-scripts@3.4.3 -g

CMD ["pwd"]
COPY ./modules/frontend .

EXPOSE 3000

CMD ["npm", "start"]

