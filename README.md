# HyggeCo2CertificateVerificationPortal

## Using Docker

Make sure to have Docker and docker compose installed on your machine. You can download it from [here](https://www.docker.com/products/docker-desktop).

### Running the application

To run the application, navigate to the root directory of the project and run the following command:
```bash
docker-compose up
```

The application should now be visible on localhost:4000

### Stopping the application

To stop the application, you can run the following command:
```bash
docker-compose down
```

### Use data

The application doesn't have any data when starting up. You must 
```bash
docker ps # to get the container id of the db
CONTAINER_ID=<container_id> 
docker cp database<date>.dump $CONTAINER_ID:/your_database.dump # to copy the dump file to the container
docker exec -it $CONTAINER_ID psql -U <your_username> -d <your_database> # to access the database
```
Inside the database, you will need to drop the tables and restore the dump file. To do that, run the following commands:
```sql
DROP TABLE IF EXISTS "certificate";
DROP TABLE IF EXISTS "user";
DROP TABLE IF EXISTS "certificateverificationattempt";
<ctrl+d> # to exit the database
```

Inside your command line, run the following command:
```bash
docker exec -it $CONTAINER_ID pg_restore -U <your_username> -d <your_database> /your_database.dump
```

## Angular Local Development

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 17.3.7.

### Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

### Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

### Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

### Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

### Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

### Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.
