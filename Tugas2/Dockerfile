# Gunakan Ubuntu sebagai base image
FROM ubuntu:latest

# Update package list dan install Nginx
RUN apt update && apt install -y nginx

# Expose port 80 agar bisa diakses dari luar container
EXPOSE 80

# Jalankan Nginx saat container dimulai
CMD ["nginx", "-g", "daemon off;"]
