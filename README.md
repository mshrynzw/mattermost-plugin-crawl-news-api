# How to
```
cd /opt/mattermost-plugin-crawl-news-api/app/
python main.py --reload
```
```
vi /etc/systemd/system/mattermost-plugin-crawl-news-api.service
################################################################
[Unit]
Description = api_important_words_extraction
[Service]
WorkingDirectory = /opt/mattermost-plugin-crawl-news-api/app
ExecStart = /bin/python3.8 /opt/mattermost-plugin-crawl-news-api/app/mai
Restart = always
Type = simple
User=root
[Install]
WantedBy = multi-user.target
################################################################
systemctl daemon-reload
systemctl enable api_important_words_extraction.service
systemctl start api_important_words_extraction.service
systemctl status api_important_words_extraction.service
```
