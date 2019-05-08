# SafeConfig

## How to Run

Each application has its own parser and checker functions.

First, run the separate parser to parse the application's configuration file and output a json file.

Then, run the json filter to filter the security relevant information. When running jsonfilter.py, use the specific app name as the first argument input. (Choose from "redis", "mongodb", "nginx", "spark", "tomcat", "wordpress")

Finally, run the application's checker function. It will return the result true if the configuration is secure, and false if it is not.

```bash
python3 redisparse.py
python3 jsonfilter.py redis
python3 redischecker.py
```

## Research on Secure Container Configurations

To find out what are significant in a secure configuration, we studied the configuration of 7 of the most popular applications in docker. Except Joomla doesn't appear to have secure relevant configurations, we summarized the security relevant configuration information of the rest of the applications.

### Redis

Redis has a straightforward configuration file. 

To secure redis.conf securely, we consider the following keywords in the configuration file:

- **bind**: listen to just one or multiple selected interfaces using # the "bind" configuration directive, followed by one or more IP addresses
  e.g. 

  ```
  bind 192.168.1.100 10.0.0.1
  bind 127.0.0.1 ::1
  ```

- **protected-mode**: avoid that Redis instances left open on the internet are accessed and exploited
  e.g. 

  ```
  protected-mode yes
  ```

- **port**: accept connections on the specified port
  e.g. 

  ```
  port 6379
  ```

- **unixsocketperm**: specify the path for the Unix socket that will be used to listen for incoming connections
  e.g. 

  ```
  unixsocket /tmp/redis.sock
  unixsocketperm 700
  ```

- **requirepass**: require clients to issue AUTH <PASSWORD> before processing any other commands

  This should be a sensitive information because we don't want the clear text of password to appear in the configuration that we show.

  To check whether it's secure, we're applying the simple checking process whether the password contains at least a lowercase letter, an uppercase letter and a digit, and the length of the password should be greater than or equal to 8.

  e.g. 

  ```
  requirepass foobared
  ```

- **rename-command**: command renaming

  This should also be a sensitive information because we don't want to show what the new name of the command is.

  e.g. 

  ```
  rename-command CONFIG b840fc02d524045429941cc15f59e41cb7be6c52
  rename-command CONFIG ""
  ```

This is the sample configuration file we use:

[http://download.redis.io/redis-stable/redis.conf](http://download.redis.io/redis-stable/redis.conf)

### Tomcat

Tomcat has four configuration xml files: server.xml (Tomcat main configuration file), web.xml (global web application deployment descriptors), context.xml (global Tomcat-specific configuration options) and tomcat-users.xml (a database of user, password and role for authentication and access control). It's configuration has a complex nesting structure. This project hasn't dealt with the nesting structure well and cannot deal with parallel blocks. 

The main security concerned configuration files are server.xml and web.xml.

In **server.xml**:

- **Server**: removing Server Banner from HTTP Header
  e.g. 

  ```
  Server = " "
  ```

- **SSLEnabled**': make your web application accessible through HTTPS
  e.g. 

  ```xml
  SSLEnabled="true" scheme="https" keystoreFile="ssl/bloggerflare.jks" keystorePass="chandan" clientAuth="false" sslProtocol="TLS"
  ```

- **Shutdown**: By default, tomcat is configured to be shutdown on 8005 port. You can shutdown tomcat instance by doing a telnet to IP:port and issuing SHUTDOWN command
  e.g. 

  ```xml
  <Server port="8867" shutdown="NOTGONNAGUESS">
  ```

In web.xml:

- **Enforce HTTPS**:

  e.g.

  ```xml
  <security-constraint>
  <web-resource-collection>
  <web-resource-name>Protected Context</web-resource-name>
  <url-pattern>/*</url-pattern>
  </web-resource-collection>
  <user-data-constraint>
  <transport-guarantee>CONFIDENTIAL</transport-guarantee>
  </user-data-constraint>
  </security-constraint>
  ```

- **Default 404, 403, 500 page**

  e.g.

  ```xml
  <error-page> 
  <error-code>404</error-code>
  <location>/error.jsp</location> 
  </error-page> 
  <error-page> 
  <error-code>403</error-code> 
  <location>/error.jsp</location>
  </error-page>
  <error-page> 
  <error-code>500</error-code> 
  <location>/error.jsp</location>
  </error-page>
  ```

- **Cookie-config**: add Secure & HttpOnly flag to cookie

  e.g.

  ```xml
  <cookie-config>
  <http-only>true</http-only>
  <secure>true</secure>
  </cookie-config>
  ```
### MongoDB
Configuration is specified at run time, therefore no user centric sensitive information was found in example configs.
Therefore MongoDB config files only need parsing (and not filtering).

## Code Structure

We constructed a pipeline framework with three phases: parsing, filtering and checking.

### Parsing

Every application has its own parser. The use of parser is to generate a json file according to the input configuration file. This helps the next steps to deal with files with the same format.

### Filtering

We have a common filter jsonfilter.py that extracts security relevant information from the parsed json files and replaces the sensitive information. It includes the filters of applications that it covers.

For the application filters, they include a list of security relevant keywords for this application and a list of sensitive information in the security relevant configuration. It provides dealing functions for sensitive information, which mostly replace the sensitive information according to whether it's secure or not.

For example, dealPass in redisfilter.py returns six stars if the password contains at least a lowercase letter, an uppercase letter and a digit, and the length of the password should be greater than or equal to 8. It returns "not secure password" if it's considered as not secure.

###Checking

The checking functions vary for applications. But we're applying the most rigorous requirements: only when everything in the security relevant list are included in the configuration and the sensitive information are checked as secure, the checking function will return true.
