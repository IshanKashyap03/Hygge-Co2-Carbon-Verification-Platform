# Stage 1: Build the Angular app
FROM node:20 AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Serve the Angular app with Node.js
FROM node:20-alpine
WORKDIR /app
COPY --from=build /app/dist/hygge-co2-certificate-verification-portal /app/dist/hygge-co2-certificate-verification-portal
COPY package.json package-lock.json ./
RUN npm install --only=production

EXPOSE 4000
CMD ["npm", "run", "serve:ssr:hygge-co2-certificate-verification-portal"]
