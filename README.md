# What is this?
This repository contains the official website (www.coretabs.net) of Coretabs Academy, an online, modern, and open-source software development academy aims to provide clear learning-paths.

# Contribution

We would love any **pull request** to this repository as Coretabs Academy is a community project.

We are following our [Code of Conduct](CODE_OF_CONDUCT.md) to keep an awesome contribution spirit!

You can pick any **non-assigned** issue as follows:
1. [From the current milestone](https://github.com/coretabs-academy/website-v2/milestones) (recommended).

2. If you pick an issue **NOT from the current milestone**, please **be sure** that the solution of this issues **fits** into the academy current state (you can contact one of [our core contributors](#core-contributors)).

3. For creating a new issue, please follow [our style-guide for writing an issue](ISSUE_STYLE_GUIDE.md).

4. Please do **NOT** pick an **already assigned** issue as someone else is already doing it.


# Running locally

For the api, you can simply write in your command line (this will prepare the virtual environment, migrate the db, and run the server):

```
python run.py
```

To run the SPA project:
```
npm install
npm run serve
```

If you do not want to install the dev tools on your machine, <a href="./docs/docker-development.md" >this guide provides information for running the development environment on docker.</a>

# Connecting to development API

If you want to consume a ready-to-use API, we have it at [api-dev.coretabs.net](https://api-dev.coretabs.net)

Add this line into your host file:

```
127.0.0.1 local.coretabs.net
```

Depending on the OS you use, hosts file can be found on:

1. Windows `C:\Windows\System32\drivers\etc\host`

2. Linux `/etc/hosts`

3. MacOS X (v10.0 - v10.1.5) `/Applications/Utilities/NetInfo Manager`

4. MacOS X (v10.6 - v10.12) `/etc/hosts`

[Detailed information on how to edit your hosts file can be found here](https://support.rackspace.com/how-to/modify-your-hosts-file/)

Now that your PC can translate `local.coretabs.net` into 127.0.0.1, you can simply run:

```
npm run serve-api
```

You can now use your spa connected to the API via https://local.coretabs.net:8080

# Deploying
Docker orchestrated with docker-compose are the main tools used for deployment.

# Core Contributors

* Yaser (https://forums.coretabs.net/u/YaserAlnajjar/)
* Mohammed (https://forums.coretabs.net/u/Alhakem)
* Louay (https://forums.coretabs.net/u/LouayH)
* Hichem (https://forums.coretabs.net/u/hichem2h)
* Ahmed (https://forums.coretabs.net/u/ahmedalrifai)
* Ayman (https://forums.coretabs.net/u/Ayman97)

# Tech stack
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/5/53/Vue.js_Logo.svg" width="50"> <img src="https://www.djangoproject.com/m/img/logos/django-logo-negative.svg" width="80"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" width="48"> <img src="https://wiki.openwrt.org/_media/media/homepage-docker-logo.png" width="50"> <img src="https://www.nordicmakers.vc/wp-content/uploads/2017/05/scrimba-1.png" width="100"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/600px-Octicons-mark-github.svg.png" width="48"> <img src="https://cdn.worldvectorlogo.com/logos/heroku-1.svg" width="120"> <img src="https://dcnxfkgt2gjxz.cloudfront.net/Logos/Integration-Card-Logos/integrationcards-discourse.svg" width="100"> <img src="https://forums.coretabs.net/uploads/default/original/1X/193cd8725cf75433fc6ae1ab03ed7075ff12ddf5.png" width="100">
</p>
