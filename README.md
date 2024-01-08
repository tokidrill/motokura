## Setup

### Docker 環境の構築

```
docker-compose build # 初回のみ
docker-compose up -d
```

### 開発サーバの起動

```
docker-compose exec django bash
cd noveltotanka

python manage.py runserver 0.0.0.0:8000

http://localhost:8080
```
