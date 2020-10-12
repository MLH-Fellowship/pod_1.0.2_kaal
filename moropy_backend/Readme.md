# Flask Backend

The backend serves the CLI and Cloud Firestore. This follows the REST convention and is deployed on Heroku servers.

### API Routes

##### POST /updateactivities

Request Body:

```
{
  “userHash”:”some string”,
  “activities”: [
		  {
			  “activeWindow”: “code”,
			  “start_timestamp” : <time>,
			  “end_timstamp”: <time>,
		  }
                ]
}
```

##### POST /status

Request Body:

```
{
  "userHash": "<user-hash>",
  "status": "<away|available>"
}
```

##### GET /validate

Request Body:

```
{
  "userHash": "<user-hash>"
}
```

Response:

```
{
  "user": {
            "discordId": "<string>",
            "userName": "<string>",
            "userHash": "<string>"
          }
}
```

