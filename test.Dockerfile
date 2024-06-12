# Stage 1: Build the Angular app
FROM node:20 AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install

# Copy the Angular project files
COPY angular.json tsconfig.json tsconfig.app.json ./
COPY frontend/ frontend/

RUN npm run build-test

# Step 2: Serve the Angular application with NGINX
FROM nginx:alpine

# Copy custom NGINX configuration files
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Copy the built Angular app from the build stage
COPY --from=build /app/dist/hygge-co2-certificate-verification-portal/browser /usr/share/nginx/html

# Expose port 8080 such as in the deployment environment
EXPOSE 8080

# Start NGINX server
CMD ["nginx", "-g", "daemon off;"]
