# EngineerBlogsServer

### ローカル環境構築手順

#### 手順１：サーバーレスフレームワークのインストール
npm install -g serverless

#### 手順2：関連するパッケージのインストール
npm install aws-sdk <br>
npm install --save-dev serverless-offline <br>
npm install --save-dev serverless-dynamodb-local <br>

#### 手順3：DynamoDB Local のインストール
sls dynamodb install

#### 手順4：DynamoDB Local の起動
sls dynamodb start

**ブラウザで http://localhost:8000/shell にアクセスし、テーブルの中身を確認します。左側のエディタに下記を記入し、再生ボタンを押します。**

`各テーブル名: Company,Article,User`


```
var params = {
    TableName: 'Company',
};
dynamodb.scan(params, function(err, data) {
    if (err) ppJson(err);
    else ppJson(data);
});
```


`デプロイ前にserverless.ymlの内容を以下に変更してください`

```
service: engineer-blogs

plugins: 
 - serverless-dynamodb-local
 - serverless-offline
 
provider:
  name: aws
  runtime: python3.6

functions:
  getRSS:
    handler: rss.getRSS
    events:
      - http:
          path: getrss
          method: post
          cors: true
          integration: lambda
          request:
            template:
              text/xhtml: '{ "stage" : "$context.stage" }'
              application/json: '{ "httpMethod" : "$context.httpMethod" }'

```

#### デプロイコマンド
sls deploy
