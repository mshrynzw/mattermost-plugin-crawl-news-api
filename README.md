# How to
```
cd /opt/api_important_words_extraction/app/
python main.py --reload
```
```
vi /etc/systemd/system/api_important_words_extraction.service
################################################################
[Unit]
Description = api_important_words_extraction
[Service]
WorkingDirectory = /opt/api_important_words_extraction/app
ExecStart = /bin/python3.8 /opt/api_important_words_extraction/app/mai
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
