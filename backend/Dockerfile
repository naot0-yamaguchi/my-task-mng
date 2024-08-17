# ベースイメージを指定
FROM python:latest

# 作業ディレクトリを指定
WORKDIR /app

# 必要なパッケージをインストール
COPY ./requirement.txt .
RUN pip install -r requirement.txt && \
    rm -rf /root/.cache/pip

# アプリケーションのファイルをコピー
COPY . .

# アプリケーションを実行
CMD ["flask", "run", "--host=0.0.0.0"]
