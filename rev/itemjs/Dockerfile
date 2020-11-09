FROM node:14.11
WORKDIR /app
COPY . /app
RUN npm i
RUN chmod -R 775 /app
RUN useradd -u 1337 leetuser
USER leetuser

EXPOSE 7001

CMD ["node", "item_server.js"]