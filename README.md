# EngineerBlogsServer

#### サーバーレスフレームワークのインストール
npm install -g serverless

#### 関連するパッケージのインストール
npm install aws-sdk
npm install --save-dev serverless-offline
npm install --save-dev serverless-dynamodb-local

#### DynamoDB Local のインストール
sls dynamodb install

#### DynamoDB Local の起動
sls dynamodb start

**ブラウザで http://localhost:8000/shell にアクセスし、テーブルの中身を確認します。左側のエディタに下記を記入し、再生ボタンを押します。**

`各テーブル名: Company,Article,User`


```var params = {
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
