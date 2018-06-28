# Docker
### What is Docker ?

If you do NOT know  what Docker is, it is better to watch this first: https://www.youtube.com/watch?v=YFl2mCHdv24

### What is docker-compose ?

docker-compose is a tool to orchestrate multiple apps in a simple manner, this guide walks you through the basics of docker-compose:

https://www.youtube.com/watch?v=Qw9zlE3t8Ko

# Running the academy

Docker always strives for simplicity, you can simply run in your command line:

```
docker-compose up
```

Please make sure you do NOT have the following folders before running this command:
* **venv** in your src folder.
* **node_modules** in your src/spa folder.

### What are the urls of the apps ?

Use this command to know where docker is running in your machine:

```
docker-machine ip
```

Example:

```
> docker-machine ip
192.168.99.100
```
You will find the api on http://192.168.99.100:8000 and the spa on http://192.168.99.100:8081

### Troubleshooting

  #### `"<volume>" includes invalid characters for a local volume name`
  This is because you're running **docker tools on Windows**.
   
  You need to make docker-compose convert Windows paths, by running this command:
  ```
  $Env:COMPOSE_CONVERT_WINDOWS_PATHS=1
  ```
  
  #### `Cannot create container for service dockerapp`
    
  * **docker-tools**:
    If you're using docker-tools on Windows, cloning the repo into your desktop will do.

  * **DockerCE**:
    You would need to allow sharing drives in docker

    ![DockerCE-Share](https://cdn-enterprise.discourse.org/docker/uploads/default/original/2X/a/afd0f40b9df5ad7442ab9211e43339db0a610f8a.png)

  #### 'npm ERR! code EPROTO npm ERR! errno -71 npm ERR! syscall symlink`
  This happens because virtualbox is disabled by default "for security reasons". The way around this is document here:

  https://github.com/npm/npm/issues/992#issuecomment-289935776