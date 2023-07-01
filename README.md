# 参考
以下を参考にサンプルアプリを作成する。

https://aws.amazon.com/jp/blogs/news/developing-twelve-factor-apps-using-amazon-ecs-and-aws-fargate/

# リソース
- 実リソースはTerraformで作成する。
- 開発環境はlocalstackを利用する。
  - appconfigは有料だったためmock responseを作成することで対応
  - dynamodbは作成

# 開発環境の始め方
```bash
# sample-core-twelve-factor配下で実行
$ docker compose up --build
# 動作確認
$ curl -k http://localhost:8080/hello
"<html><body style=\"background-color:Brown;color:white;text-align:center\"><p><strong><h1>Hello from Twelve Factor App!</h1></strong></p><p><h2>Developed with Python, deployed with Docker and LocalStack</h2></p></body></html>"%                                        

$ curl -k http://localhost:8080/table-name
"TwelveFactorDatastore"%                                                                                                              

$ curl -k http://localhost:8080/refresh-config
"Nothing to refresh"%                                                                                                   

$ curl -k http://localhost:8080/              
"All good !"%
```

# Dockerのデバッグ方法
https://gendosu.jp/archives/2838
```bash
$ docker ps -a
CONTAINER ID   IMAGE                           COMMAND              CREATED          STATUS                      PORTS     NAMES
c511ede23aa0   sample-core-twelve-factor-app   "poetry run start"   15 minutes ago   Exited (1) 15 minutes ago             sample-core-twelve-factor-app-1
36b934b2cbea   amazonlinux:2023.0.20230607.0   "/bin/bash"          2 days ago       Exited (0) 2 days ago                 amazonlinux

$ docker commit c511ede23aa0 sample-core-debug
sha256:0709767c422bebdbde66b93715450ed05f4e6be0a52956e5731dcb6369a752b1

$ docker run --rm -it sample-core-debug /bin/bash
root@489ff2a0b049:/app# ls
poetry.lock  pyproject.toml  src
root@489ff2a0b049:/app# exit
```
