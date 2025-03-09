# php/Dockerfile
FROM php:8.2-cli

# Install system dependencies (e.g., unzip for Composer)
RUN apt-get update && apt-get install -y unzip
# Install Xdebug via PECL and enable it
RUN pecl install xdebug \
    && docker-php-ext-enable xdebug \
    && echo "xdebug.mode=coverage" > /usr/local/etc/php/conf.d/xdebug.ini

# Optionally set the environment variable to ensure coverage mode is active
ENV XDEBUG_MODE=coverage

# Install Composer globally
COPY --from=composer:2 /usr/bin/composer /usr/local/bin/composer

WORKDIR /usr/src/app

# Install dependencies if a composer.json exists, then keep the container running
CMD ["bash", "-c", "if [ -f composer.json ]; then composer install; fi && tail -f /dev/null"]