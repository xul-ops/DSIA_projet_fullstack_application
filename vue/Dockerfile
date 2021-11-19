FROM node:10

WORKDIR /app

# COPY ./vue /app/app

# RUN npm config set registry https://registry.npmjs.org

COPY . /app


COPY package.json /app/

RUN npm install

EXPOSE 5050

#RUN npm run serve
CMD ["npm", "run", "serve"]
