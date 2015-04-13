> Simple echo server used for debugging.

```sh
curl -X GET https://devcho.herokuapp.com/hello-world?langauge=english

GET 200

{
  "method": "GET",
  "headers": {...},
  "body": null,
  "query": {
    "language": ["english"]
  }
}
```

Deploy yours.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
