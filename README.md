# youtube_crawly


crawler for youtube channels or playlists and scheduling crawlers to run periodically

### Prerequisites

install docker and docker compose

* [Docker](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) 
* [Docker Compose](https://docs.docker.com/compose/install/) 

### Installing

clone repo

```
git clone https://github.com/phawzy/youtube_crawly
```

start all services using docker compose

```
sudo docker-compose up --build -d --remove-orphans
```

### Technologies

* Scrapy: Crawling the playlist

* Splash: Handling pages with Javascript

* scrapyd: api for scrapy to start spiders remotly

* Mongodb: Storing saved items

* Celery: Scheduling the spiders instances to run periodically

* Rabbitmq: Message broker for celery


### Current State

You can fill the file called playlists in celery_app directory with playlists links
and then start the application as mentioned in installation section 
then celery will schedule spiders to run each 1 hour

### Issues 

* Scrapyd is exposed but doesn't run the spiders so i used scrapy shell command for now

* doesn't support channels links due to css selectors problem

* images do not get downloaded 

* every scrapped video gets new record in db not updating the original previously scrapped video