# Stage 1: Build the Angular application
FROM node:14 as build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build -- --output-path=./dist/out

# Stage 2: Serve the Angular application using NGINX
FROM nginx:alpine

COPY --from=build /app/dist/out /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

