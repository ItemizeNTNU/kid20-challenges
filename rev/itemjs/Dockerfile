FROM node:14.11
WORKDIR /app
COPY item.js item_server.js package.json /app/
RUN npm i
RUN chmod -R 775 /app
RUN useradd -u 1337 leetuser
USER leetuser

EXPOSE 7001

CMD ["node", "item_server.js"]