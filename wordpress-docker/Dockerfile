# Gunakan PHP dan Apache
FROM php:8.2-apache

# Atur folder kerja
WORKDIR /var/www/html

# Install ekstensi yang dibutuhkan WordPress
RUN apt-get update && \
    apt-get install -y libpng-dev && \
    docker-php-ext-install pdo pdo_mysql gd && \
    docker-php-ext-install mysqli && docker-php-ext-enable mysqli && \
    pecl install redis && docker-php-ext-enable redis

# Buka port 80 untuk akses web
EXPOSE 80

# Jalankan Apache
CMD ["apache2-foreground"]
