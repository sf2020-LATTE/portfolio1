# Job Port
転職活動における情報を一元管理するためのアプリ。応募企業の情報管理機能とタスク管理機能と掲示板機能を実装しています。

# URL
http://18.176.56.82/jpapp/

# 制作背景
私は現在、未経験からwebエンジニアを目指し、転職活動をしております。
転職活動を進める中で、各企業の特徴や選考状況、面接の日程など、
それぞれの情報をEvernoteやスプレッドシートでバラバラに管理しており、管理が煩雑だなと感じていました。

そこで、転職活動の情報をまとめるアプリを探してみましたが、無いことがわかり、自分で作ろうと考えました。
その中で「ユーザーとしてこういうものが欲しい」という思いを、機能として盛り込みました。
* アプリ内で応募企業を一覧管理できる機能が欲しい
* 転職活動におけるタスク管理を行いたい
* 転職活動における日程を管理できる機能が欲しい
* 転職活動における、アドバイスが欲しい

# 使用技術
* Git   2.25.1
* Python  3.8.5
* Django 3.1.7
* PostgreSQL 12.6
* Nginx 1.18.0
* gunicorn  20.1.0
* AWS
    * EC2

# 機能一覧
* 基本機能
    * 会員登録・退会機能
    * ログイン機能
    * ユーザー設定変更機能
    * ゲストログイン機能
* 企業情報投稿機能
    * 企業情報投稿・編集・削除・一覧表示機能
    * 面接日程投稿・編集・削除・一覧表示機能
* タスク管理機能
    * タスク投稿・編集・削除・一覧表示機能
* 質問・相談機能
    * 質問&相談投稿・編集・削除機能
    * コメント投稿・編集・削除機能(Ajax)

# DB設計
![Uploading スクリーンショット 2021-04-22 21.55.13.png…]()

# インフラ構成図
![スクリーンショット 2021-04-22 21 48 49](https://user-images.githubusercontent.com/67609336/115716847-968a0300-a3b4-11eb-8d10-7922008785de.png)

# 今後追加したい機能等
## 機能面

*  GooglecalenderAPIとの連携
（登録した面接日がGooglecalenderに反映されるようにしたい。)
* レスポンシブ対応
* 登録した企業の検索機能
* 登録した企業のソート機能

## インフラ面
* EC2,ドメイン名取得、HTTPS化、RDSの冗長化
* Dockerを用いた開発・本番環境の構築
* CircleCIを用いたCI/CDパイプラインの構築
* セキュリティ対策
