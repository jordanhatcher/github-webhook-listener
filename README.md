# Github Webhook Listener

## Setup

Clone the git repository:
`https://github.com/jordanhatcher/github-webhook-listener.git && cd github-webhook-listener`

Build the container:
`docker build -t listener .`

Edit the config.json file.
`secret`: the secret key from the webhook settings of the github repo
`host`: IP to listen on
`port`: Port to listen on
`route`: Route to listen on
`hook`: list of shell commands to run after receiving the hook

## Running

Example docker run command
```
docker run --name listener \
--expose 8080 \
-v $(pwd)/config.json:/src/config.json \
listener
```

additional volumes can be mounted to share the cloned files with other containers
