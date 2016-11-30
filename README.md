# eng

Set-up localhost:

1: add configuration file to /etc/apache2/sites-available, use "site_name".com, add lines below before the log directory:
<Directory /path/to/folder/>
        Require all granted
</Directory>

2:enable site: $ sudo a2ensite "site_name"

3: $ sudo nano /etc/hosts, add 127.0.0.1       "site_name".com

4: reload apache2 /etc/init.d/apache2 restart

#todo

devie a way of filling divs with (data-title="title") with appropiate story.
