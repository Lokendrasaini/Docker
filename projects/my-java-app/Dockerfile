# Use an official OpenJDK runtime as a parent image
FROM openjdk:17-jdk-slim

# Set the working directory in the container
WORKDIR /app

# Copy the source code into the container
COPY src /app/src

# Create a directory for compiled classes
RUN mkdir -p /app/bin

# Compile the Java program
RUN javac -d /app/bin /app/src/main/java/com/example/HttpServerExample.java

# Expose the port the server will run on
EXPOSE 8080

# Define the command to run the application
CMD ["java", "-cp", "/app/bin", "com.example.HttpServerExample"]

